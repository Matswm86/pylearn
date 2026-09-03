/* ===== Embeddings, Vector Search & Retrieval: 30 questions =====
 *
 * Source: the handbook "Embeddings, Vector Search & Retrieval - 30 Questions
 * Every AI Engineer Should Understand" by @techNmak. Questions and answers are
 * condensed from that handbook; the reference list is his.
 * Rebuilt here so each question can be self-rated and remembered.
 *
 * Progress lives in localStorage under QUESTIONS_STORAGE_KEY, separate from
 * pylearn_path and pylearn_checklist.
 */

const QUESTIONS_STORAGE_KEY = "pylearn_questions";
const QUESTIONS_AUTHOR = "@techNmak";

const QUESTION_REFS = [
  ["Reimers & Gurevych (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks", "https://arxiv.org/abs/1908.10084"],
  ["Wang et al. (2022). Text Embeddings by Weakly-Supervised Contrastive Pre-training (E5)", "https://arxiv.org/abs/2212.03533"],
  ["Su et al. (2023). One Embedder, Any Task: Instruction-Finetuned Text Embeddings (INSTRUCTOR)", "https://arxiv.org/abs/2212.09741"],
  ["Kusupati et al. (2022). Matryoshka Representation Learning", "https://arxiv.org/abs/2205.13147"],
  ["Karpukhin et al. (2020). Dense Passage Retrieval for Open-Domain Question Answering", "https://arxiv.org/abs/2004.04906"],
  ["Xiong et al. (2020). ANCE: Approximate Nearest Neighbor Negative Contrastive Learning", "https://arxiv.org/abs/2007.00808"],
  ["Robertson & Zaragoza (2009). The Probabilistic Relevance Framework: BM25 and Beyond", "https://doi.org/10.1561/1500000019"],
  ["Thakur et al. (2021). BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of IR Models", "https://openreview.net/forum?id=wCu6T5xFjeJ"],
  ["Formal et al. (2021). SPLADE v2: Sparse Lexical and Expansion Model for Information Retrieval", "https://arxiv.org/abs/2109.10086"],
  ["Cormack, Clarke & Buettcher (2009). Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods", "https://doi.org/10.1145/1571941.1572114"],
  ["Nogueira & Cho (2019). Passage Re-ranking with BERT", "https://arxiv.org/abs/1901.04085"],
  ["Khattab & Zaharia (2020). ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT", "https://arxiv.org/abs/2004.12832"],
  ["Santhanam et al. (2021). ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction", "https://arxiv.org/abs/2112.01488"],
  ["Malkov & Yashunin (2016/2018). Efficient and robust approximate nearest neighbor search using HNSW graphs", "https://arxiv.org/abs/1603.09320"],
  ["Jegou, Douze & Schmid (2011). Product Quantization for Nearest Neighbor Search", "https://doi.org/10.1109/TPAMI.2010.57"],
  ["Faiss documentation: guidelines to choose an index", "https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index"],
  ["Patel et al. (2024). ACORN: Performant and Predicate-Agnostic Search Over Vector Embeddings and Structured Data", "https://arxiv.org/abs/2403.04871"],
  ["Singh et al. (2021). FreshDiskANN: A Fast and Accurate Graph-Based ANN Index for Streaming Similarity Search", "https://arxiv.org/abs/2105.09613"],
  ["Shen et al. (2020). Towards Backward-Compatible Representation Learning", "https://arxiv.org/abs/2003.11942"],
  ["Muennighoff et al. (2022). MTEB: Massive Text Embedding Benchmark", "https://arxiv.org/abs/2210.07316"],
  ["Lee et al. (2024). NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models", "https://arxiv.org/abs/2405.17428"],
  ["Enevoldsen et al. (2025). MMTEB: Massive Multilingual Text Embedding Benchmark", "https://arxiv.org/abs/2502.13595"],
];

// Each question: n, level, q, a (array of paragraphs), refs (1-indexed into QUESTION_REFS)
const QUESTION_GROUPS = [
  {
    title: "What an embedding is",
    note: "Phase 2, level 2 of the escalating project: the vector store is the part you cannot debug without these seven.",
    questions: [
      {
        n: 1, level: "Beginner",
        q: "What is a text embedding, and what does it actually mean for two texts to be close in embedding space?",
        a: ["A text embedding is a fixed-length numerical representation produced by a model. The useful property is not that the vector holds a universal coordinate system for meaning: it is that the training objective shaped the space so a chosen similarity function tends to rank related inputs closer than unrelated ones, for the tasks the model was trained to support.",
            "Two texts being close therefore means they score high under that particular model and that particular scoring rule. The distance does not carry the same interpretation across different models, tasks, or domains."],
        refs: [1, 2],
      },
      {
        n: 2, level: "Intermediate",
        q: "How does an embedding model turn a variable-length sequence of token representations into one fixed-size vector, and why does the pooling strategy matter?",
        a: ["A Transformer produces one contextual representation per input position, but retrieval needs one vector for the whole input, so the model needs an aggregation step. Common choices are mean pooling over token representations, a designated token representation, last-token pooling, or a learned pooling module. SBERT evaluated pooling strategies; later models such as NV-Embed introduced learned latent-attention pooling.",
            "The engineering rule: follow the pooling method the model was trained and released with. Changing it changes the representation space and can materially hurt retrieval."],
        refs: [1, 21],
      },
      {
        n: 3, level: "Intermediate, math",
        q: "How do cosine similarity, dot product, and Euclidean distance differ, and under what conditions do they produce the same ranking?",
        a: ["For vectors x and y the dot product is xᵀy. Cosine similarity divides that by the product of the norms. Euclidean distance measures the straight-line distance between the points.",
            "If both vectors are L2-normalized their norms are 1, so cosine equals dot product, and squared Euclidean distance becomes ‖x − y‖² = 2 − 2xᵀy. Under those assumptions, ranking by larger cosine or dot product is the same ordering as ranking by smaller Euclidean distance. Without normalization the rankings can differ, because magnitude affects dot product and Euclidean distance."],
        refs: [15],
      },
      {
        n: 4, level: "Intermediate",
        q: "What changes when embeddings are L2-normalized, and when might removing vector magnitude discard useful information?",
        a: ["L2 normalization rescales each vector to unit norm, so similarity depends on direction rather than magnitude and cosine becomes equivalent to dot product. The trade-off is that every piece of information carried by the original norm is discarded.",
            "That is harmless or desirable for a model trained around cosine similarity, but it is not universally safe. If a model was trained so magnitude contributes to its scoring behaviour, normalizing at serving time changes the intended geometry. Use the convention the specific model recommends."],
        refs: [15],
      },
      {
        n: 5, level: "Intermediate",
        q: "Does increasing embedding dimensionality automatically improve retrieval? What are the quality, memory, and search-cost trade-offs?",
        a: ["No. A larger vector gives more representational capacity, but retrieval quality also depends on the model, data, objective, pooling, and domain. Higher dimensionality increases raw storage linearly, typically increases exact similarity-computation cost linearly, and can make ANN indexes larger or more expensive.",
            "Matryoshka Representation Learning is the evidence against 'more dimensions are always necessary': it trains one representation so prefixes of different lengths stay useful, which turns dimension into an explicit quality-versus-cost dial."],
        refs: [4],
      },
      {
        n: 6, level: "Intermediate",
        q: "Why is search often an asymmetric embedding problem, and why do some models require different prefixes or instructions for queries and documents?",
        a: ["The two sides play different roles: a short query asks for information, a document supplies it. Some models are trained with that asymmetry explicitly and expect query prefixes, document prefixes, or task instructions. INSTRUCTOR, for example, embeds text together with instructions describing the task.",
            "If a model's recipe expects a particular query/document format, ignoring it moves inputs away from the distribution the model learned and reduces retrieval quality. The exact prefixes are model-specific, not a standard."],
        refs: [3],
      },
      {
        n: 7, level: "Intermediate, production",
        q: "Are cosine or dot-product similarity scores probabilities? Can a threshold such as 0.8 be reused across embedding models or datasets?",
        a: ["No. These are scores in a learned vector space, not calibrated probabilities of relevance. A cosine score of 0.8 from one model cannot be assumed to mean the same thing for another model, corpus, language, or task.",
            "If a system needs a threshold for deduplication, semantic caching, or rejecting weak matches, calibrate it on representative labeled data and evaluate it against the actual false-positive and false-negative costs."],
        refs: [],
      },
    ],
  },
  {
    title: "How embedding models are trained",
    note: "The negatives decide what the model can tell apart.",
    questions: [
      {
        n: 8, level: "Intermediate",
        q: "How does contrastive learning train an embedding model to distinguish relevant from irrelevant pairs?",
        a: ["Contrastive training presents a positive pair alongside negative candidates and optimizes the model so the positive gets a higher similarity than the negatives. A softmax-style objective raises the relative score of the positive inside the candidate set rather than assigning an absolute semantic coordinate. DPR and E5 are representative systems trained this way.",
            "The negative distribution matters because the model learns the distinctions it is repeatedly forced to make."],
        refs: [2, 5],
      },
      {
        n: 9, level: "Advanced",
        q: "What are in-batch negatives and hard negatives, why are random negatives often too easy, and what happens when a supposed negative is actually relevant?",
        a: ["In-batch negatives reuse other examples in the same batch as negative candidates, which makes large candidate sets cheap. Hard negatives are chosen deliberately because they look plausible to the current retriever but are judged non-relevant; ANCE showed why informative negatives matter when random ones are too easy.",
            "The danger is false negatives: an unlabeled item may actually be relevant, and treating it as negative pushes a useful neighbour away and damages the representation. Negative mining needs relevance-aware filtering and good labels, not 'harder is always better'."],
        refs: [5, 6],
      },
    ],
  },
  {
    title: "Lexical, sparse, and hybrid retrieval",
    note: "Dense retrieval is not a replacement for keyword search, and BM25 is still the baseline that embarrasses people.",
    questions: [
      {
        n: 10, level: "Intermediate, mechanism",
        q: "How does BM25 rank documents, and what roles do term rarity, term-frequency saturation, and document-length normalization play?",
        a: ["BM25 sums a contribution per query term. The contribution grows with term frequency in the document but saturates rather than growing linearly; it is larger for rarer, more informative terms through an inverse-document-frequency factor; and it is adjusted for document length so long documents are not rewarded merely for holding more words.",
            "The parameters usually called k1 and b control saturation and length normalization. Variants differ in IDF and implementation details, so the mechanism matters more than one library's exact formula."],
        refs: [7],
      },
      {
        n: 11, level: "Intermediate, trade-off",
        q: "How does dense semantic retrieval differ from lexical retrieval such as BM25, and when can lexical retrieval outperform dense search?",
        a: ["BM25 scores explicit term overlap; dense retrieval compares learned vectors and can bridge vocabulary mismatch, recovering related text that shares few words with the query.",
            "Lexical search stays strong for exact identifiers, product codes, error messages, uncommon names, quoted phrases, and domain terms whose surface form matters. BEIR's heterogeneous evaluation showed BM25 remains a strong zero-shot baseline and that methods behave differently across domains. 'Dense always beats lexical' is not defensible."],
        refs: [8],
      },
      {
        n: 12, level: "Advanced",
        q: "What is learned sparse retrieval, and how does a model such as SPLADE differ from both BM25 and dense embeddings?",
        a: ["Learned sparse retrieval keeps a sparse vocabulary-aligned representation but learns the term weights and the expansion behaviour with a neural model. SPLADE produces sparse vectors over vocabulary dimensions, so it gets learned expansion while staying compatible with inverted-index retrieval.",
            "That makes it different from BM25, whose weights come from a hand-designed formula, and from dense embeddings, whose dimensions are latent and not interpretable as vocabulary terms."],
        refs: [9],
      },
      {
        n: 13, level: "Intermediate",
        q: "What is hybrid retrieval, and why can combining lexical and semantic systems improve robustness?",
        a: ["Hybrid retrieval combines systems that make different errors, most often lexical and dense. Exact matching recovers rare identifiers dense models miss; dense retrieval recovers paraphrases with no shared terms. They can be combined by score normalization, learned fusion, rank fusion, or a union of candidates followed by reranking.",
            "Hybrid is not automatically better: it adds compute and tuning, and its value has to be measured on queries where the components are genuinely complementary."],
        refs: [8, 10],
      },
      {
        n: 14, level: "Advanced",
        q: "If BM25 and dense retrieval produce scores on different scales, how can their rankings be combined? How does Reciprocal Rank Fusion work?",
        a: ["Raw BM25 scores and dense similarities are not calibrated to the same scale, so adding them directly lets one system dominate for arbitrary numerical reasons.",
            "Reciprocal Rank Fusion sidesteps that. For a document d a common RRF score is the sum over rankers of 1/(k + rank_i(d)), where each ranker contributes by rank position and k is a stabilizing constant. It combines order instead of assuming calibration. The original paper found it a strong simple baseline, but the best fusion method stays workload-dependent."],
        refs: [10],
      },
    ],
  },
  {
    title: "Reranking and late interaction",
    note: "Two stages, because the accurate scorer is too expensive to run on the whole corpus.",
    questions: [
      {
        n: 15, level: "Intermediate",
        q: "What is the difference between a bi-encoder retriever and a cross-encoder reranker?",
        a: ["A bi-encoder encodes query and document independently, so document vectors can be precomputed and searched efficiently. A cross-encoder processes the query-document pair jointly, allowing token-level interaction before producing a relevance score, but it must run once per candidate pair, which is far more expensive over a large corpus.",
            "SBERT illustrates the efficiency of independent embeddings; BERT passage reranking illustrates the accuracy of joint scoring on a smaller candidate set."],
        refs: [1, 11],
      },
      {
        n: 16, level: "Intermediate, system design",
        q: "Why do large search systems often retrieve candidates first and rerank only a subset? How should you choose rerank depth?",
        a: ["A fast first stage produces a high-recall candidate set, cutting millions of items to tens or hundreds, and the expensive reranker runs only on those.",
            "There is no universal correct depth. Too shallow hides relevant documents from the reranker; too deep buys diminishing returns at the cost of latency and compute. Choose it from recall-at-depth curves, measured reranker gains, QPS, and the latency budget, not from a copied default."],
        refs: [11],
      },
      {
        n: 17, level: "Advanced",
        q: "What is late interaction, and how does ColBERT occupy the space between single-vector retrieval and full cross-encoder reranking?",
        a: ["ColBERT encodes queries and documents independently but does not collapse a document to one vector: it keeps token-level vectors. At scoring time each query-token vector matches against document-token vectors, commonly through a MaxSim-style interaction, and those scores are aggregated.",
            "That preserves finer-grained interaction than single-vector retrieval while still allowing precomputed document representations. The cost is a much larger index, which is exactly why ColBERTv2 introduced compression."],
        refs: [12, 13],
      },
    ],
  },
  {
    title: "Vector indexes and ANN",
    note: "Start from the constraints, never from an index name.",
    questions: [
      {
        n: 18, level: "Intermediate",
        q: "What is the difference between exact nearest-neighbor search and approximate nearest-neighbor search, and when might exact search still be the right choice?",
        a: ["Exact search compares the query with every candidate under the chosen metric and returns the true nearest results for the stored representation. ANN does less work, or works on compressed structures, trading some recall for lower latency, memory, or both.",
            "ANN is not automatically necessary. With a small corpus, few searches, GPU-friendly batch workloads, or a requirement for exact results, a flat scan is simpler and fast enough. Faiss treats Flat search as the exact baseline and recommends choosing by workload."],
        refs: [15, 16],
      },
      {
        n: 19, level: "Advanced",
        q: "How does HNSW search work conceptually, and how do graph connectivity, construction effort, search effort, recall, latency, and memory interact?",
        a: ["HNSW builds a multi-layer proximity graph. Search starts in sparse upper layers to move quickly toward a promising region, then descends into denser layers to refine.",
            "Higher connectivity usually costs memory and can improve recall; more construction effort builds a better graph at higher indexing cost; more search effort explores more candidates, often improving recall at the cost of latency. Libraries expose M, efConstruction, and efSearch, but the good values are data- and implementation-dependent. Do not treat HNSW as carrying a universal O(log N) latency guarantee in production."],
        refs: [14, 16],
      },
      {
        n: 20, level: "Advanced",
        q: "How does an inverted-file (IVF) vector index narrow the search space, and what happens when you probe more or fewer partitions?",
        a: ["IVF uses a coarse quantizer to partition vectors into inverted lists. At query time the query is assigned to nearby coarse centroids and only a selected number of lists are searched.",
            "Probing more lists examines more of the corpus and generally recovers more true neighbours, at the cost of latency and compute; probing fewer is faster but misses neighbours that landed in unvisited cells. IVF makes the speed-recall trade-off explicit, and unlike a flat index it needs a trained coarse partition."],
        refs: [16],
      },
      {
        n: 21, level: "Advanced",
        q: "What is Product Quantization, and how does it trade vector-storage cost and search speed against approximation error?",
        a: ["PQ splits a high-dimensional vector into subspaces and quantizes each subvector with a small codebook, so the stored vector becomes a sequence of compact codeword IDs instead of full floats. Distances are then approximated with lookup tables; asymmetric distance computation compares the full query against compressed database codes.",
            "Memory drops dramatically and cache behaviour improves, but quantization error can reduce nearest-neighbour recall. PQ is index and vector compression: do not confuse it with quantizing LLM weights."],
        refs: [15],
      },
      {
        n: 22, level: "Advanced, judgment",
        q: "How would you choose among exact search, HNSW, IVF, IVF+PQ, or another ANN design?",
        a: ["Start from constraints, not an index name. Flat is right when exactness or simplicity matters and the workload is small enough. HNSW is attractive when memory is available and you need high recall at low latency. IVF helps when partitioning avoids scanning most vectors, especially at larger scale. PQ or IVF+PQ becomes attractive when vector memory is the limiting resource and approximation is acceptable.",
            "Also weigh update frequency, filter selectivity, QPS, hardware, dimensionality, and index-build cost. Faiss's own selection guidance is conditional for exactly this reason."],
        refs: [16],
      },
      {
        n: 23, level: "Advanced",
        q: "Why does metadata filtering interact awkwardly with ANN search, and what are the trade-offs between pre-filtering, post-filtering, and filter-aware ANN indexes?",
        a: ["ANN structures are optimized around geometric neighbourhoods, while a metadata filter imposes a separate eligibility constraint.",
            "Post-filtering retrieves nearest vectors then discards ineligible ones; with a selective filter it returns too few useful results unless the candidate pool is enlarged. Pre-filtering restricts the eligible set first, but the subset may not align with the ANN structure and can degrade into an expensive scan. Filter-aware indexes push the predicate into traversal; ACORN extends HNSW with predicate-aware traversal. The right choice depends on filter selectivity, correlation between attributes and vectors, the recall target, and the index design."],
        refs: [17],
      },
      {
        n: 24, level: "Advanced",
        q: "How do inserts, deletes, and updates affect ANN indexes, and why can freshness be a systems problem rather than simply a database write?",
        a: ["Freshness behaviour is index-specific. Some implementations support inserts and deletes directly; others handle mutations poorly, use tombstones, or need periodic compaction and rebuilds to stay efficient. Graph indexes carry structural relationships that are more complicated than updating an independent database row.",
            "FreshDiskANN is the useful systems example: it was designed for real-time inserts, deletes, and searches on large graph-based collections that earlier approaches treated as mostly static. The lesson is not 'ANN cannot update', it is that update semantics and maintenance cost must be evaluated per index."],
        refs: [18],
      },
    ],
  },
  {
    title: "Production: migration and memory",
    note: "The two questions that decide whether the system survives its second month.",
    questions: [
      {
        n: 25, level: "Advanced, production",
        q: "What happens when you upgrade an embedding model? Can new query embeddings safely be compared with document embeddings produced by the old model?",
        a: ["Usually no. Independently trained models define different representation spaces, so a query vector from the new model should not be assumed comparable with old document vectors.",
            "A production upgrade normally means re-embedding the corpus, rebuilding or backfilling the index, and validating retrieval before switching traffic. Backward-compatible representation-learning methods exist precisely because compatibility is not free. During migration, version the embedding model and the index together rather than silently mixing spaces."],
        refs: [19],
      },
      {
        n: 26, level: "Intermediate, calculation",
        q: "How would you estimate the raw memory footprint of an embedding corpus before adding ANN-index overhead?",
        a: ["For N vectors of dimension d at b bytes per component, raw vector memory is roughly N × d × b. Ten million 1,536-dimensional FP32 vectors need 10,000,000 × 1,536 × 4 = 61.44 GB, about 57.22 GiB.",
            "That is only the raw matrix. Real systems also store document IDs, metadata, allocator overhead, graph edges or IVF structures, quantizer codebooks, replicas, and sometimes the original vectors for reranking. Faiss's index documentation shows how differently index families add bytes per vector."],
        refs: [16],
      },
    ],
  },
  {
    title: "Evaluation, debugging, and design",
    note: "Question 30 is the interview: it is the whole handbook asked at once.",
    questions: [
      {
        n: 27, level: "Intermediate",
        q: "How do Precision@k, Recall@k, MRR, and nDCG measure different aspects of retrieval quality?",
        a: ["Precision@k is the fraction of the top k judged relevant. Recall@k is the fraction of all known relevant items recovered within the top k. MRR averages the reciprocal rank of the first relevant result, so it rewards putting at least one answer near the top. nDCG discounts lower ranks, can use graded relevance, and compares observed discounted gain against the ideal ordering.",
            "They answer different product questions, and all of them depend on the completeness and quality of the relevance judgments: a missing label makes a genuinely relevant result look like an error."],
        refs: [8, 20],
      },
      {
        n: 28, level: "Advanced, debugging",
        q: "How can you determine whether retrieval errors come from the embedding model or from the approximate index?",
        a: ["Hold the embeddings fixed and compare exact vector search against the ANN index. If exact search on the same vectors and metric does not rank the relevant document highly, no amount of HNSW or IVF tuning fixes it: the problem is the representation or the relevance definition.",
            "If exact search succeeds but ANN misses the neighbour, measure ANN recall and investigate search effort, partition probing, quantization, or index configuration. Verify the labels themselves too. That decomposition separates model quality from index approximation."],
        refs: [],
      },
      {
        n: 29, level: "Advanced, evaluation",
        q: "Why is choosing the embedding model with the highest leaderboard score insufficient, and how should you evaluate models for your real retrieval workload?",
        a: ["A leaderboard score summarizes one set of tasks, languages, domains, pooling conventions, and protocols. MTEB found no single embedding approach dominated all tasks; MMTEB widened evaluation to hundreds of tasks across 250+ languages and made the heterogeneity plainer.",
            "Select by evaluating representative queries against your own corpus and relevance judgments, then add systems constraints: embedding latency, vector dimension, memory, maximum input length, language coverage, deployment cost. The best leaderboard model can be the wrong production model."],
        refs: [20, 22],
      },
      {
        n: 30, level: "Advanced, system design",
        q: "Design retrieval for millions of documents containing exact identifiers and natural-language content, with permission filters, frequent updates, and a strict latency SLO. Where would you use lexical search, dense retrieval, ANN, fusion, filtering, and reranking, and how would you prove it works?",
        a: ["Do not force one retrieval primitive to solve every query. Exact identifiers and error codes get a lexical path; natural-language discovery gets dense retrieval; hybrid fusion combines them where evaluation shows the recall is genuinely complementary.",
            "Apply authorization as an eligibility constraint before anything can be exposed, using pre-filtering or a filter-aware ANN rather than unsafe post-hoc masking. Use ANN only where scale and latency justify approximation, and rerank a bounded candidate set when richer query-document interaction actually improves quality. Design a freshness path for updates and version embeddings together with the index.",
            "Prove it with exact-search baselines, lexical and dense ablations, Recall@k and nDCG, ANN recall, latency percentiles, filter-specific slices, update-lag metrics, and end-to-end permission tests."],
        refs: [],
      },
    ],
  },
];

// Quick checks for whether an answer shows mechanism-level understanding.
// Not hiring rules.
const QUESTION_SIGNALS = [
  [3, "Derives the normalized-vector equivalence instead of naming three metrics.", "What changes if the vectors are not normalized?", "Says cosine, dot product and Euclidean distance are always interchangeable."],
  [7, "Knows similarity is not a calibrated probability and would validate a threshold on representative labels.", "How would you choose a threshold for semantic deduplication?", "Treats 0.8 as a universal relevance cutoff."],
  [10, "Explains saturation, IDF and length normalization.", "Why should a repeated term saturate?", "Calls BM25 only keyword matching, or says term frequency grows without bound."],
  [14, "Recognises the score-scale mismatch and can explain rank-based fusion.", "Why can adding raw BM25 and cosine scores be unstable?", "Assumes all retrieval scores can simply be summed."],
  [19, "Explains hierarchical graph traversal and the recall/latency/memory knobs without promising a complexity bound.", "What does efSearch change?", "Says HNSW guarantees logarithmic latency in production."],
  [23, "Distinguishes post-filtering, pre-filtering and filter-aware search, and talks about selectivity.", "What happens when only 0.1% of documents are eligible?", "Assumes metadata filters are free after ANN retrieval."],
  [25, "Versions model and index together and expects re-embedding unless compatibility was engineered.", "How would you do a zero-downtime migration?", "Mixes old and new embedding spaces without validation."],
  [28, "Compares exact-vector retrieval with ANN on the same embeddings to isolate representation from index approximation.", "Which metric would you use for ANN recall?", "Tries to fix poor exact retrieval by raising efSearch or nprobe."],
];

const QUESTION_EXTRAS = [
  ["Multilingual retrieval", "Shared embedding spaces can support cross-lingual retrieval, but quality is not uniform across languages or domains. MMTEB covers hundreds of tasks in more than 250 languages: test your actual language mix rather than inferring from English results."],
  ["Multi-vector retrieval", "ColBERT shows retrieval need not mean one vector per document. Token-level vectors preserve fine-grained interaction, at the cost of index size and a different serving architecture."],
  ["Disk-backed ANN", "At very large scale, systems put substantial index state on SSD instead of keeping every vector and graph edge in RAM. DiskANN and FreshDiskANN are the graph-based examples built for that regime."],
  ["Chunking and long documents", "How you segment documents changes what the embedding model sees and what the retriever can return. There is no universal chunk-size recipe; it belongs to context engineering, Phase 3."],
];

// ===== Persistence =====
const questionsProgress = {
  _data: null,
  load() {
    try { this._data = JSON.parse(localStorage.getItem(QUESTIONS_STORAGE_KEY)) || {}; }
    catch { this._data = {}; }
  },
  save() {
    try { localStorage.setItem(QUESTIONS_STORAGE_KEY, JSON.stringify(this._data)); }
    catch { /* storage unavailable: progress lives for this page view only */ }
  },
  isDone(id) { if (!this._data) this.load(); return !!this._data[id]; },
  set(id, done) {
    if (!this._data) this.load();
    if (done) this._data[id] = true; else delete this._data[id];
    this.save();
  },
  reset() {
    this._data = {};
    try { localStorage.removeItem(QUESTIONS_STORAGE_KEY); } catch { /* ignore */ }
  },
};
questionsProgress.load();

// Ids follow the handbook numbering, so rewording never orphans a tick.
function questionId(n) { return `q_emb_${n}`; }

function questionsGroupIds(group) { return group.questions.map(q => questionId(q.n)); }

function questionsAllIds() {
  const ids = [];
  for (const g of QUESTION_GROUPS) ids.push(...questionsGroupIds(g));
  return ids;
}

function questionsCount(ids) {
  const done = ids.filter(id => questionsProgress.isDone(id)).length;
  return { done, total: ids.length, pct: ids.length ? Math.round(done / ids.length * 100) : 0 };
}

// ===== Event handlers (global, called from inline handlers) =====
function questionsSetDone(id, done) {
  questionsProgress.set(id, done);
  document.querySelectorAll(`[data-q="${id}"]`).forEach(el => el.classList.toggle("done", done));
  const strip = document.getElementById("questions-progress");
  if (strip) strip.innerHTML = renderQuestionsProgressStrip();
  document.querySelectorAll("[data-q-count]").forEach(el => {
    const c = questionsCount(el.getAttribute("data-q-count").split(","));
    el.textContent = `${c.done}/${c.total}`;
  });
}

function resetQuestionsProgress() {
  if (!confirm("Reset the 30 questions? This clears every self-rating. Nothing else on the site is affected.")) return;
  questionsProgress.reset();
  render();
}

// ===== Rendering =====
function renderQuestionsProgressStrip() {
  const c = questionsCount(questionsAllIds());
  return `
    <div class="path-progress-top">
      <strong>${c.done}/${c.total} you can answer out loud</strong>
      <span>${c.pct}%</span>
    </div>
    <div class="progress-bar"><div class="progress-fill" style="width:${c.pct}%"></div></div>`;
}

function renderQuestionRefs(refs) {
  if (!refs || !refs.length) return "";
  const links = refs.map(i => {
    const r = QUESTION_REFS[i - 1];
    if (!r) return "";
    return `<a href="${r[1]}" target="_blank" rel="noopener" title="${escapeHtml(r[0])}">[${i}]</a>`;
  }).join(" ");
  return `<p class="q-refs">Sources: ${links}</p>`;
}

function renderQuestion(q) {
  const id = questionId(q.n);
  const done = questionsProgress.isDone(id);
  const body = q.a.map(p => `<p>${escapeHtml(p)}</p>`).join("");
  return `
    <details class="q-card ${done ? "done" : ""}" data-q="${id}">
      <summary>
        <span class="q-num">${q.n}</span>
        <span class="q-text">${escapeHtml(q.q)}</span>
        <span class="q-level">${escapeHtml(q.level)}</span>
      </summary>
      <div class="q-body">
        ${body}
        ${renderQuestionRefs(q.refs)}
        <label class="q-rate"><input type="checkbox" ${done ? "checked" : ""} onchange="questionsSetDone('${id}', this.checked)"> I could answer this out loud, without reading it first</label>
      </div>
    </details>`;
}

function renderQuestionGroup(group) {
  const ids = questionsGroupIds(group);
  const c = questionsCount(ids);
  return `
    <details class="phase-card" open>
      <summary>
        <span class="phase-title">${escapeHtml(group.title)}</span>
        <span class="phase-count" data-q-count="${ids.join(",")}">${c.done}/${c.total}</span>
      </summary>
      <div class="phase-body">
        <p class="path-note">${escapeHtml(group.note)}</p>
        ${group.questions.map(renderQuestion).join("")}
      </div>
    </details>`;
}

function renderQuestionSignals() {
  const rows = QUESTION_SIGNALS.map(([n, strong, followup, weak]) => `
    <tr>
      <td class="q-sig-n">Q${n}</td>
      <td>${escapeHtml(strong)}</td>
      <td>${escapeHtml(followup)}</td>
      <td class="q-sig-weak">${escapeHtml(weak)}</td>
    </tr>`).join("");
  return `
    <details class="phase-card">
      <summary><span class="phase-title">Answer quality notes</span><span class="phase-count">8</span></summary>
      <div class="phase-body">
        <p class="path-note">Not hiring rules. Quick checks for whether an answer shows mechanism-level understanding rather than memorised vocabulary.</p>
        <div class="q-table-wrap">
          <table class="q-table">
            <thead><tr><th></th><th>Strong-answer signal</th><th>Useful follow-up</th><th>Weak-answer signal</th></tr></thead>
            <tbody>${rows}</tbody>
          </table>
        </div>
      </div>
    </details>`;
}

function renderQuestionExtras() {
  const items = QUESTION_EXTRAS.map(([t, d]) =>
    `<li><strong>${escapeHtml(t)}.</strong> ${escapeHtml(d)}</li>`).join("");
  return `
    <details class="phase-card">
      <summary><span class="phase-title">Additional concepts worth knowing</span><span class="phase-count">4</span></summary>
      <div class="phase-body"><ul class="path-items q-extras">${items}</ul></div>
    </details>`;
}

function renderQuestionReferences() {
  const items = QUESTION_REFS.map(([title, url], i) =>
    `<li><span class="q-ref-n">${i + 1}</span> <a href="${url}" target="_blank" rel="noopener">${escapeHtml(title)}</a></li>`).join("");
  return `
    <details class="phase-card">
      <summary><span class="phase-title">Primary references</span><span class="phase-count">${QUESTION_REFS.length}</span></summary>
      <div class="phase-body"><ol class="q-refs-list">${items}</ol></div>
    </details>`;
}

function renderQuestions(app) {
  const groups = QUESTION_GROUPS.map(renderQuestionGroup).join("");

  app.innerHTML = `
    <button class="back-btn" onclick="navigate('/path')">← The Path</button>

    <div class="path-hero">
      <h1>\u{1f9ee} Embeddings, Vector Search &amp; Retrieval</h1>
      <p>Thirty questions every AI engineer should be able to answer out loud. Questions and answers are condensed from the handbook by ${escapeHtml(QUESTIONS_AUTHOR)}; the reference list at the bottom is his.</p>
      <p class="path-note">This is the theory under Phase 2 level 2, the retrieval layer of the escalating project, and under the retrieval half of Phase 3. Read a question, answer it before you open it, then tick the box only if you got the mechanism right.</p>
      <div class="path-rule"><strong>The one thing to take away:</strong> almost every wrong answer here is a universal claim. Similarity is not a probability, dense does not always beat lexical, more dimensions is not better, and HNSW guarantees nothing in production.</div>
    </div>

    <div id="questions-progress" class="path-progress">${renderQuestionsProgressStrip()}</div>

    ${groups}
    ${renderQuestionSignals()}
    ${renderQuestionExtras()}
    ${renderQuestionReferences()}

    <div style="text-align:center;margin-top:32px;padding-top:24px;border-top:1px solid var(--border)">
      <button class="action-btn" onclick="resetQuestionsProgress()" style="color:var(--error)">\u{1f504} Reset self-ratings</button>
      <p style="font-size:0.75rem;color:var(--text-light);margin-top:6px">Progress is saved in this browser only.</p>
    </div>
  `;
}
