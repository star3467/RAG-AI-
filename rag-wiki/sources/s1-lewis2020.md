---
id: S1
title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
authors: Patrick Lewis 等 12 人（Facebook AI Research / UCL / NYU）
venue: NeurIPS 2020（arXiv:2005.11401，2020-05-22 首次提交）
url: https://arxiv.org/abs/2005.11401
type: primary（原始論文）
accessed: 2026-11-23
depth: 摘要與引言層級（透過搜尋結果摘錄閱讀，未逐章讀完）
---

# 摘要
提出把「參數記憶」（預訓練 seq2seq 模型）與「非參數記憶」（Wikipedia 的稠密向量索引，用預訓練的神經檢索器存取）結合的通用微調方法，稱為 RAG。檢索器是 DPR，生成器是 BART。論文比較了兩種形式：整段輸出都用同一批檢索段落，或每個 token 可用不同段落。

# 這個來源支持的 claim
C03、C04、C16

# 限制
只讀到摘要與引言，**實驗細節與數字沒有納入 wiki**。
