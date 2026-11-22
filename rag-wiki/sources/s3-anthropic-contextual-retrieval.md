---
id: S3
title: Introducing Contextual Retrieval
authors: Anthropic Engineering（Research and writing by Daniel Ford）
venue: Anthropic 官方工程文章（2024-09-19 發表）
url: https://www.anthropic.com/research/contextual-retrieval
type: primary（原始實驗報告；也是 RAG 基礎流程的清楚說明）
accessed: 2026-11-23
depth: 全文（WebFetch 取得完整頁面）
---

# 摘要
先用一節說明標準 RAG（切塊 → 嵌入 → 向量資料庫），再指出傳統做法會在切塊時丟失上下文。提出 Contextual Retrieval：用 LLM 替每個塊產生一小段情境說明，附在塊前面，再做嵌入與 BM25 索引。接著報告實驗結果，並討論重排序（reranking）與成本。

# 這個來源支持的 claim
C02、C21、C25、C33（部分）、C40–C45、C50–C57

# 注意
- 實驗指標：1 − recall@20（前 20 塊沒撈到相關內容的比例）。
- 搜尋結果中有第三方網頁引用不同數字（見 log.md L-04），**一律以本頁原文為準**。
