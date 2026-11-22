---
id: S6
title: RAG Pipeline Deep Dive: Ingestion, Chunking, Embedding, and Vector Search
authors: Ryan Giggs（DEV Community 個人文章）
venue: 技術部落格（以 Oracle Database 23ai 為範例）
url: https://dev.to/derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-2877
type: tutorial（實作教學，個人作者）
accessed: 2026-11-23
depth: 全文（WebFetch 取得完整頁面）
---

# 摘要
把 RAG 拆成離線的「索引階段」和線上的「檢索階段」，逐步說明文件載入、清理、metadata、切塊策略與重疊、嵌入模型、向量索引（HNSW、IVF）、top-k 與重排序。

# 這個來源支持的 claim
C10、C11、C20、C22–C24、C30–C33、C95

# 限制
- 個人教學文章，**數字型建議（chunk 大小、重疊比例、k 值）屬於經驗法則，不是實驗結論**；簡報中呈現時要用「常見做法」的語氣。
- 文中 Oracle 專屬語法與索引參數不納入。
