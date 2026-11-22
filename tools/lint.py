#!/usr/bin/env python3
"""Wiki + 簡報 檢查腳本（lint）。

用法：python3 -I tools/lint.py <wiki_dir> <slides_html>
檢查項目：
  W1 每條 claim 都有 [S#]，且 S# 對應到 sources/ 內存在的檔案
  W2 claim 編號不重複
  W3 來源頁宣稱支持的 claim 編號，必須真的存在於 concepts/
  W4 index.md 寫的來源數、概念頁數、claim 數與實際相符
  S1 簡報每頁（<section class="slide">）都有 data-claims 或 data-nosrc
  S2 簡報引用的 claim 編號都存在
  S3 簡報文字中出現的每個數字（含 % 與 $），都必須能在 wiki 中找到
  S4 「比喻」必須標示 （比喻，非來源）
  S5 簡報列出的參考來源 URL，必須與 sources/ 內的 url 一致
  S6 HTML 結構：標籤是否成對、是否有 script 載入外部資源
"""
import re, sys, json
from pathlib import Path
from html.parser import HTMLParser

wiki = Path(sys.argv[1])
slides_path = Path(sys.argv[2])
errors, warnings, info = [], [], []

# ---------- Wiki ----------
src_files = sorted((wiki / "sources").glob("s*.md"))
src_ids = {}
src_urls = {}
src_claims = {}
for f in src_files:
    t = f.read_text(encoding="utf-8")
    m = re.search(r"^id:\s*(S\d+)", t, re.M)
    u = re.search(r"^url:\s*(\S+)", t, re.M)
    if not m:
        errors.append(f"W0 {f.name}: 缺少 id")
        continue
    src_ids[m.group(1)] = f.name
    if u:
        src_urls[m.group(1)] = u.group(1)
    # 來源頁「支持的 claim」那一行
    sec = re.search(r"# 這個來源支持的 claim\n(.+)", t)
    if sec:
        src_claims[m.group(1)] = sec.group(1)

claims = {}
claim_text = {}
dup = []
concept_files = sorted((wiki / "concepts").glob("*.md"))
for f in concept_files:
    for line in f.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- (C\d+)：(.*)$", line)
        if not m:
            continue
        cid, body = m.group(1), m.group(2)
        refs = re.findall(r"\[(S\d+)\]", body)
        if cid in claims:
            dup.append(cid)
        claims[cid] = (f.name, refs)
        claim_text[cid] = body
for cid, (fn, refs) in claims.items():
    if not refs:
        errors.append(f"W1 {cid} ({fn}): 沒有來源標註")
    for r in refs:
        if r not in src_ids:
            errors.append(f"W1 {cid} ({fn}): 來源 {r} 不存在")
for d in dup:
    errors.append(f"W2 claim 編號重複：{d}")

# W3：來源頁宣稱支持的 claim 必須存在
def expand(text):
    out = set()
    for a, b in re.findall(r"C(\d+)\s*[–-]\s*C?(\d+)", text):
        out.update(f"C{n:02d}" for n in range(int(a), int(b) + 1))
    for c in re.findall(r"C\d+", text):
        out.add(c)
    return out
for sid, line in src_claims.items():
    for c in expand(line):
        if c not in claims:
            # 範圍展開時，不存在的中間編號只警告
            warnings.append(f"W3 {sid} 宣稱支持 {c}，但 concepts 內沒有這條")

# W4：index.md 計數
idx = (wiki / "index.md").read_text(encoding="utf-8")
m = re.search(r"來源 (\d+) 篇　｜　概念頁 (\d+) 頁　｜　claim 共 (\d+) 條", idx)
if m:
    a, b, c = map(int, m.groups())
    if a != len(src_ids):
        errors.append(f"W4 index 寫來源 {a} 篇，實際 {len(src_ids)}")
    if b != len(concept_files):
        errors.append(f"W4 index 寫概念頁 {b} 頁，實際 {len(concept_files)}")
    if c != len(claims):
        errors.append(f"W4 index 寫 claim {c} 條，實際 {len(claims)}")
else:
    errors.append("W4 index.md 找不到計數列")

# ---------- 簡報 ----------
html = slides_path.read_text(encoding="utf-8")

class P(HTMLParser):
    VOID = {"meta","link","br","hr","img","input","path","rect","line","circle","polygon","stop"}
    def __init__(self):
        super().__init__()
        self.stack, self.bad = [], []
        self.slides = []          # (attrs, text)
        self.cur = None
        self.text_all = []
        self.ext = []
        self.in_script = False
        self.in_style = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script","link","img") and (a.get("src","").startswith("http") or a.get("href","").startswith("http") and tag=="link"):
            self.ext.append((tag, a.get("src") or a.get("href")))
        if tag == "script": self.in_script = True
        if tag == "style": self.in_style = True
        if tag not in self.VOID:
            self.stack.append(tag)
        if tag == "section" and "slide" in a.get("class","").split():
            self.cur = [a, []]
    def handle_startendtag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):
        if tag == "script": self.in_script = False
        if tag == "style": self.in_style = False
        if tag in self.VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
            if tag == "section" and self.cur is not None:
                self.slides.append(self.cur); self.cur = None
        else:
            self.bad.append(f"</{tag}> 與堆疊頂端 {self.stack[-1] if self.stack else None} 不符")
    def handle_data(self, d):
        if self.in_script or self.in_style: return
        self.text_all.append(d)
        if self.cur is not None:
            self.cur[1].append(d)

p = P(); p.feed(html)
if p.bad: errors.extend(f"S6 {b}" for b in p.bad[:5])
if p.stack: errors.append(f"S6 未關閉的標籤：{p.stack[:5]}")
for tag, u in p.ext:
    warnings.append(f"S6 外部資源 {tag}: {u}（離線瀏覽可能失效）")

if not p.slides:
    errors.append("S1 找不到任何 <section class=\"slide\">")

# 只用「claim 本文」當作數字白名單：不含 claim 編號、來源編號，也不含 ⚠ 注意裡被判定為錯誤的數字
_clean = lambda s: re.sub(r"\[S\d+\]", "", s)
wiki_all = "\n".join(_clean(v) for v in claim_text.values())
# (?<![A-Za-z0-9]) 讓 "BM25"、"S3" 這類「英文夾數字」的名稱不被當成數字
NUM = r"(?<![A-Za-z0-9])\$?\d[\d,\.]*\s*%?"
def norm(n): return re.sub(r"\s", "", n).replace("$", "").strip(".,")
wiki_nums = set(re.findall(NUM, wiki_all))
wiki_nums_n = {norm(n) for n in wiki_nums}

used_claims = set()
for i, (attrs, texts) in enumerate(p.slides, 1):
    dc = attrs.get("data-claims", "")
    if not dc and "data-nosrc" not in attrs:
        errors.append(f"S1 第 {i} 頁：沒有 data-claims，也沒有 data-nosrc 說明")
    for c in [x.strip() for x in dc.split(",") if x.strip()]:
        used_claims.add(c)
        if c not in claims:
            errors.append(f"S2 第 {i} 頁：引用不存在的 claim {c}")
    body = "".join(texts)
    # 排除頁碼、投影片編號、footer 的 claim 編號
    body_clean = re.sub(r"C\d{2}", "", body)
    body_clean = re.sub(r"S\d", "", body_clean)
    body_clean = re.sub(r"\b\d+\s*/\s*\d+\b", "", body_clean)       # 頁碼 3 / 16
    if "data-nonum" in attrs:
        continue
    for n in re.findall(NUM, body_clean):
        n2 = norm(n)
        if not n2: continue
        if n2 in wiki_nums_n: continue
        if re.fullmatch(r"\d", n2):   # 單一數字（步驟 1、2…）略過
            continue
        errors.append(f"S3 第 {i} 頁：數字「{n2}」在 wiki 找不到")
    if "比喻" in body and "比喻，非來源" not in body:
        errors.append(f"S4 第 {i} 頁：有「比喻」但沒標示（比喻，非來源）")

# S5 參考來源
ref_urls = set(re.findall(r'data-ref-url="([^"]+)"', html))
for sid, u in src_urls.items():
    if u not in ref_urls:
        errors.append(f"S5 簡報參考頁沒有列出 {sid} 的網址 {u}")
for u in ref_urls:
    if u not in src_urls.values():
        errors.append(f"S5 簡報列出的網址不在 wiki：{u}")

unused = sorted(set(claims) - used_claims)
info.append(f"wiki: 來源 {len(src_ids)}、概念頁 {len(concept_files)}、claim {len(claims)}")
info.append(f"簡報: {len(p.slides)} 頁；使用 {len(used_claims)} 條 claim；未被簡報使用 {len(unused)} 條：{', '.join(unused)}")

print("== INFO ==");  [print(" ", x) for x in info]
print("== WARNINGS ==" , len(warnings)); [print(" ", x) for x in warnings]
print("== ERRORS ==", len(errors));  [print(" ", x) for x in errors]
sys.exit(1 if errors else 0)
