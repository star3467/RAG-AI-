# RAG 流程（Pipeline）

- C10：RAG 可以分成兩個階段：離線的「索引階段」（載入文件 → 切塊 → 轉成嵌入向量 → 存進向量資料庫），以及線上的「檢索階段」（把問題轉成向量 → 相似度搜尋 → 取前 k 筆 → 交給 LLM 生成）。 [S6][S3]
- C11：問題和文件必須用同一個嵌入模型轉成向量，兩邊的向量才能互相比較。 [S6][S4]
- C12：用一句話走完線上流程：編碼問題、檢索相符文件、把文件附進提示詞、生成回答。 [S4]
- C13：錯誤會一路往下傳：嵌入品質差會讓檢索變差，檢索差會讓提示詞內容不佳，最後答案就不準。 [S4]
- C14：附進提示詞的內容受模型上下文窗口限制，太多就得截斷或精簡，設計時要在細節與篇幅之間取捨。 [S4]
- C15：Gao 等人把 RAG 的核心技術拆成三塊：檢索（Retrieval）、生成（Generation）、增強（Augmentation）。 [S2][S5]

## 相關頁面
[chunking](chunking.md) · [embeddings-vector-search](embeddings-vector-search.md) · [hybrid-search-reranking](hybrid-search-reranking.md)
