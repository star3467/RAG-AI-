# 混合搜尋與重排序

- C40：嵌入擅長抓語意，但可能漏掉必須精確吻合的字串。例子：搜尋「Error code TS-999」時，嵌入可能找到一般的錯誤代碼說明，卻漏掉剛好寫 TS-999 的那一份。 [S3]
- C41：BM25 是一種以關鍵字比對為主的排序函式，建立在 TF-IDF 的概念上，並考慮文件長度、避免常見字詞的詞頻佔太大優勢。 [S3]
- C42：混合搜尋的做法：用 BM25 與嵌入各自找出前幾名，再用排名融合（rank fusion）把兩份結果合併、去重，最後取前 K 塊放進提示詞。 [S3]
- C43：重排序（reranking）：先粗略撈出一大批（Anthropic 實驗取前 150 塊），讓重排序模型依相關度替每塊打分，再選出前 20 塊交給 LLM。 [S3]
- C44：名詞整理：dense（稠密）檢索＝依語意比對；sparse（稀疏）檢索＝依關鍵字比對；reranking＝把結果重新排序，讓最相關的排在前面。 [S4]
- C45：Anthropic 的實驗結論之一：「嵌入 + BM25」優於只用嵌入。 [S3]

## 相關頁面
[embeddings-vector-search](embeddings-vector-search.md) · [contextual-retrieval](contextual-retrieval.md)
