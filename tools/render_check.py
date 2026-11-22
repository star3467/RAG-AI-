import sys, json
from playwright.sync_api import sync_playwright
path, outdir = sys.argv[1], sys.argv[2]
res = {"console_errors": [], "pageerrors": [], "slides": []}
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"])
    pg = b.new_page(viewport={"width":1280,"height":720})
    pg.on("console", lambda m: res["console_errors"].append(m.text) if m.type=="error" else None)
    pg.on("pageerror", lambda e: res["pageerrors"].append(str(e)))
    pg.goto("file://"+path)
    n = pg.evaluate("document.querySelectorAll('.slide').length")
    for i in range(n):
        info = pg.evaluate("""() => {
            const s = document.querySelector('.slide.active');
            const inner = s.querySelector('.inner');
            const foot = s.querySelector('.src-foot');
            return {scrollH: s.scrollHeight, clientH: s.clientHeight,
                    overflowX: s.scrollWidth > s.clientWidth + 1,
                    footer: foot ? foot.textContent : null,
                    count: document.getElementById('count').textContent};
        }""")
        res["slides"].append(info)
        if i in (0,4,9,15):
            pg.screenshot(path=f"{outdir}/slide{i+1}.png")
        pg.keyboard.press("ArrowRight")
    # quiz test
    pg.goto("file://"+path+"#16")
    pg.click(".quiz .q:nth-of-type(2) .opt:nth-of-type(1)")
    res["quiz_q2_wrong_marked"] = pg.evaluate("document.querySelectorAll('.quiz .q')[1].querySelectorAll('.opt.wrong').length")
    res["quiz_q2_right_marked"] = pg.evaluate("document.querySelectorAll('.quiz .q')[1].querySelectorAll('.opt.right').length")
    res["quiz_expl_shown"] = pg.evaluate("document.querySelectorAll('.quiz .q')[1].querySelector('.expl').classList.contains('show')")
    b.close()
print(json.dumps({k:v for k,v in res.items() if k!="slides"}, ensure_ascii=False, indent=1))
for i,s in enumerate(res["slides"],1):
    flag = "  <-- 內容超出一屏（可捲動）" if s["scrollH"] > s["clientH"]+2 else ""
    flag += "  <-- 橫向溢出" if s["overflowX"] else ""
    print(i, s["count"], s["footer"], flag)
