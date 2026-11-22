# RAG Wiki — 索引

主題：**RAG（檢索增強生成）**　｜　建立日期：2026-11-23　｜　來源 6 篇　｜　概念頁 10 頁　｜　claim 共 60 條

規則見 [SCHEMA.md](SCHEMA.md)，操作紀錄見 [log.md](log.md)。

## 來源（sources/）
| ID | 標題 | 類型 | 讀取深度 |
|---|---|---|---|
| S1 | [Lewis et al. 2020 — RAG 原始論文](sources/s1-lewis2020.md) | primary | 摘要＋引言 |
| S2 | [Gao et al. 2023 — RAG 綜述](sources/s2-gao2023-survey.md) | primary | 摘要＋引言 |
| S3 | [Anthropic — Contextual Retrieval](sources/s3-anthropic-contextual-retrieval.md) | primary | 全文 |
| S4 | [Palo Alto Networks — RAG 概覽](sources/s4-paloalto-overview.md) | secondary | 全文 |
| S5 | [Singh et al. — Agentic RAG 綜述](sources/s5-singh-agentic-rag.md) | primary | 約 86% |
| S6 | [DEV — RAG Pipeline 深入解析](sources/s6-devto-pipeline.md) | tutorial | 全文 |

## 概念（concepts/）
| 頁面 | 內容 | claim 範圍 |
|---|---|---|
| [rag-definition](concepts/rag-definition.md) | 定義與動機 | C01–C06, C16 |
| [pipeline](concepts/pipeline.md) | 兩階段流程 | C10–C15 |
| [chunking](concepts/chunking.md) | 切塊 | C20–C25 |
| [embeddings-vector-search](concepts/embeddings-vector-search.md) | 嵌入與向量搜尋 | C30–C33 |
| [hybrid-search-reranking](concepts/hybrid-search-reranking.md) | 混合搜尋與重排序 | C40–C45 |
| [contextual-retrieval](concepts/contextual-retrieval.md) | 情境化檢索 | C50–C57 |
| [paradigms](concepts/paradigms.md) | 範式演進 | C60–C65 |
| [agentic-rag](concepts/agentic-rag.md) | 代理式 RAG | C70–C76 |
| [rag-vs-finetuning](concepts/rag-vs-finetuning.md) | RAG／微調／提示工程 | C80–C83 |
| [risks](concepts/risks.md) | 風險與維運 | C90–C95 |

## 已知缺口
- S1、S2 只讀到摘要與引言，實驗細節未納入。
- 「RAG vs 微調」只有單一來源（S4）。
- 沒有涵蓋評估指標（如 RAGAS）與多模態 RAG。
