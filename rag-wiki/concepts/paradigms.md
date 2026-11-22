# RAG 的演進（範式）

- C60：Naive RAG 是最基本的「檢索 → 閱讀」流程：找到文件，直接拿去輔助生成。 [S2][S5]
- C61：Naive RAG 的限制：只靠詞彙比對容易缺乏語意理解、輸出可能零碎或過於籠統、資料量大時不易找到最相關的內容。 [S5]
- C62：Advanced RAG 加入稠密檢索、神經重排序與多跳（multi-hop）檢索，以提高精準度。 [S5]
- C63：Modular RAG 把流程拆成可替換的獨立元件，可混用稀疏與稠密檢索，並整合外部工具與 API。 [S5]
- C64：Graph RAG 利用圖結構表示實體與關係，適合需要關聯推理的任務；缺點是依賴高品質的圖資料、整合較複雜。 [S5]
- C65：Agentic RAG 讓自主代理決定要不要檢索、怎麼改寫查詢，以及證據是否已經足夠，並能反覆修正。 [S5]

## 相關頁面
[agentic-rag](agentic-rag.md) · [rag-definition](rag-definition.md)
