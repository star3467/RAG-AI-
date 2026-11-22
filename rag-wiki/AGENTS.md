# AGENTS.md — RAG LLM Wiki 員工手冊

> 建立日期：2026-11-23。**這份手冊是 Wiki 建好之後，依 SCHEMA.md 與補做的設計訪談整理出來的**，不是 ingest 前就存在的檔案。決策的理由與原始紀錄見 `SCHEMA.md`、需求摘要見 `requirements-summary.md`。

## 目標
以「RAG（檢索增強生成）」為主題，維護一個可追溯的 Wiki，並只用這個 Wiki 產出教學 HTML 簡報。

## 讀者與語言
- 讀者：修習 LLM 相關課程的學生、對 RAG 有興趣的初學者。
- 繁體中文為主，必要的英文技術名詞保留（Embedding、Chunking、Reranking 等）。

## 資料夾
- `sources/`：一篇來源一頁（front-matter：id / title / url / type / accessed / depth）
- `concepts/`：一個概念一頁，條列 `- Cxx：主張 [S#]`
- `index.md`：索引。計數由 lint 驗證，不手寫
- `log.md`：操作紀錄（做了什麼、發現什麼問題）
- 簡報與腳本放在 Wiki 外：`rag-teaching-slides.html`、`tools/`、`records/`

## Ingest 規則（逐篇，不批次）
1. 取得來源，優先原始來源（論文、官方文件）
2. 建立 `sources/sN-*.md`，寫摘要與**讀取深度**；讀不完整的來源不收錄數字
3. 抽出 claim，用自己的話改寫，寫進 `concepts/`
4. 更新 `index.md`、追加 `log.md`
5. 跑 Wiki lint（W1–W4），通過才收下一篇
6. 來源互相矛盾：不刪，記在 log，並在概念頁加「⚠ 注意」

## 不能做的事
- 數字、實驗結果只採 primary 來源；二手文章只能佐證
- 無法確認的差異要記錄不確定性，不能自己選一個數字
- 不貼原文長句
- 簡報不得使用 Wiki 以外的內容；比喻要標示「（比喻，非來源）」

## 簡報規則
- 每頁標註 `data-claims`，底部由腳本顯示對應 concept 頁與主張編號
- **每一句話都要對得到所引用 claim 的文字，對不到就刪**
- 只屬於某實驗或某公司的設定，要標出範圍（例如「Anthropic 實驗」）

## 完成的定義（由檢查說了算，不是 AI 說了算）
1. Wiki lint W1–W4 通過
2. 簡報 lint S1–S6 通過
3. AI 審查 R1–R3 通過（新對話，只給成品與來源）
4. 瀏覽器渲染檢查通過（無溢出、console 錯誤 0、小測驗可互動）

## 停止條件
- 全部通過
- 改滿 3 輪就停，交給人
- 相關概念頁少於 3 頁就一開始停下，不用自己的知識硬湊

## 退回路線
Wiki lint 失敗 → 重寫 Wiki 該頁；簡報文字問題 → 只修被指出的頁；Wiki 缺資料 → 回去取得並 ingest；排版問題 → 回逐頁產生。
