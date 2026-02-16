# Sentence Transformers: Embeddings, Retrieval, and Reranking

Sentence Transformers is a Python framework for computing dense and sparse embeddings for text and images, performing semantic search, reranking, and clustering. It provides easy access to over 15,000 pre-trained models from Hugging Face and supports training custom embedding models, reranker models, and sparse encoder models. The library is built on PyTorch and Hugging Face Transformers, offering state-of-the-art performance on semantic textual similarity tasks.

The framework consists of three main model types: SentenceTransformer for generating dense embeddings, CrossEncoder for reranking text pairs, and SparseEncoder for sparse embeddings. It supports multiple backends (torch, ONNX, OpenVINO), quantization for efficiency, and integrates with vector databases like FAISS and Elasticsearch. The library enables applications including semantic search, clustering, paraphrase mining, and information retrieval with minimal code.

## Installation and Basic Setup

```bash
# Install from PyPI
pip install -U sentence-transformers

# Install from conda
conda install -c conda-forge sentence-transformers

# Install from source
git clone https://github.com/UKPLab/sentence-transformers
cd sentence-transformers
pip install -e .
```

## Loading a Pre-trained SentenceTransformer Model

```python
from sentence_transformers import SentenceTransformer

# Load a pre-trained model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load with specific device
model = SentenceTransformer("all-mpnet-base-v2", device="cuda")

# Load with model configuration options
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={
        "torch_dtype": "auto",  # Use model's saved dtype
        "attn_implementation": "sdpa"  # Use scaled dot-product attention
    },
    truncate_dim=256  # Truncate embeddings to 256 dimensions
)

# The model is now ready for encoding text
print(f"Model dimension: {model.get_sentence_embedding_dimension()}")
# Model dimension: 384
```

## Computing Sentence Embeddings

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# Encode single sentence
sentence = "This is a test sentence."
embedding = model.encode(sentence)
print(f"Embedding shape: {embedding.shape}")
# Embedding shape: (384,)

# Encode multiple sentences
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]
embeddings = model.encode(sentences)
print(f"Embeddings shape: {embeddings.shape}")
# Embeddings shape: (3, 384)

# Encode with normalization (useful for cosine similarity)
normalized_embeddings = model.encode(sentences, normalize_embeddings=True)

# Encode with tensor output instead of numpy
import torch
tensor_embeddings = model.encode(sentences, convert_to_tensor=True)
print(f"Type: {type(tensor_embeddings)}, Device: {tensor_embeddings.device}")
# Type: <class 'torch.Tensor'>, Device: cpu

# Encode with batch size and progress bar
large_corpus = ["Sentence " + str(i) for i in range(1000)]
corpus_embeddings = model.encode(
    large_corpus,
    batch_size=32,
    show_progress_bar=True,
    normalize_embeddings=True
)
```

## Computing Query and Document Embeddings

```python
from sentence_transformers import SentenceTransformer

# Some models use different prompts for queries vs documents
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# For semantic search, encode queries and documents separately
queries = [
    "What is machine learning?",
    "How does deep learning work?"
]

documents = [
    "Machine learning is a field of study that gives computers the ability to learn.",
    "Deep learning is part of machine learning based on artificial neural networks.",
    "Python is a programming language.",
]

# Encode queries - optimized for query representation
query_embeddings = model.encode_query(queries, convert_to_tensor=True)

# Encode documents - optimized for document representation
doc_embeddings = model.encode_document(documents, convert_to_tensor=True)

# Compute similarity
similarities = model.similarity(query_embeddings, doc_embeddings)
print(similarities)
# tensor([[0.6234, 0.5891, 0.2145],
#         [0.5234, 0.7123, 0.1876]])
```

## Computing Similarity Between Embeddings

```python
from sentence_transformers import SentenceTransformer
import torch

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]
embeddings = model.encode(sentences, convert_to_tensor=True)

# Compute similarity matrix (all-to-all)
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.6660, 0.1046],
#         [0.6660, 1.0000, 0.1411],
#         [0.1046, 0.1411, 1.0000]])

# Compute pairwise similarity (one-to-one)
embedding1 = model.encode(["I love machine learning"], convert_to_tensor=True)
embedding2 = model.encode(["Deep learning is fascinating"], convert_to_tensor=True)
pairwise_sim = model.similarity_pairwise(embedding1, embedding2)
print(pairwise_sim)
# tensor([0.7234])

# Change similarity function
from sentence_transformers import SimilarityFunction
model.similarity_fn_name = SimilarityFunction.DOT
dot_similarities = model.similarity(embeddings, embeddings)
```

## Semantic Search

```python
from sentence_transformers import SentenceTransformer
import torch

model = SentenceTransformer("all-MiniLM-L6-v2")

# Corpus of documents
corpus = [
    "Machine learning is a field of study that gives computers the ability to learn.",
    "Deep learning is part of machine learning based on artificial neural networks.",
    "Neural networks are computing systems inspired by biological neural networks.",
    "Mars rovers are robotic vehicles designed to travel on the surface of Mars.",
    "The James Webb Space Telescope conducts infrared astronomy.",
]

# Encode corpus
corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

# Query
queries = [
    "How do artificial neural networks work?",
    "What technology is used for modern space exploration?",
]

# Find top 3 most similar documents for each query
top_k = 3
for query in queries:
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Compute similarity scores
    similarity_scores = model.similarity(query_embedding, corpus_embeddings)[0]
    scores, indices = torch.topk(similarity_scores, k=top_k)

    print(f"\nQuery: {query}")
    print("Top matches:")
    for score, idx in zip(scores, indices):
        print(f"  Score: {score:.4f} - {corpus[idx]}")

# Output:
# Query: How do artificial neural networks work?
# Top matches:
#   Score: 0.7234 - Neural networks are computing systems inspired by biological neural networks.
#   Score: 0.6891 - Deep learning is part of machine learning based on artificial neural networks.
#   Score: 0.5234 - Machine learning is a field of study that gives computers the ability to learn.
```

## Using CrossEncoder for Reranking

```python
from sentence_transformers import CrossEncoder

# Load a pre-trained CrossEncoder model
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

# Predict scores for sentence pairs
query = "How many people live in Berlin?"
passages = [
    "Berlin had a population of 3,520,031 registered inhabitants.",
    "Berlin has a yearly total of about 135 million day visitors.",
    "In 2013 around 600,000 Berliners were registered in sport clubs.",
]

# Predict similarity scores
scores = model.predict([(query, passage) for passage in passages])
print("Scores:", scores)
# Scores: [8.607139 5.506266 6.352977]

# Rank passages
ranked_results = model.rank(query, passages, return_documents=True, top_k=3)

print(f"Query: {query}\n")
for result in ranked_results:
    print(f"Rank #{result['corpus_id']} (score: {result['score']:.2f})")
    print(f"  {result['text']}\n")

# Output:
# Query: How many people live in Berlin?
#
# Rank #0 (score: 8.61)
#   Berlin had a population of 3,520,031 registered inhabitants.
#
# Rank #2 (score: 6.35)
#   In 2013 around 600,000 Berliners were registered in sport clubs.
#
# Rank #1 (score: 5.51)
#   Berlin has a yearly total of about 135 million day visitors.
```

## Retrieve and Rerank Pipeline

```python
from sentence_transformers import SentenceTransformer, CrossEncoder, util

# Step 1: Use BiEncoder (SentenceTransformer) for fast initial retrieval
bi_encoder = SentenceTransformer("all-MiniLM-L6-v2")
num_candidates = 100

# Step 2: Use CrossEncoder for accurate reranking
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

# Corpus of answers
answers = [
    "Python is a high-level programming language.",
    "Machine learning enables computers to learn from data.",
    "Deep learning uses neural networks with multiple layers.",
    # ... imagine thousands more documents
]

# Encode corpus once
answer_embeddings = bi_encoder.encode(answers, convert_to_tensor=True)

# Query
query = "What is machine learning?"

# Phase 1: Fast retrieval with bi-encoder
query_embedding = bi_encoder.encode(query, convert_to_tensor=True)
hits = util.semantic_search(query_embedding, answer_embeddings, top_k=num_candidates)
hits = hits[0]  # Get hits for first query

print(f"Bi-encoder found {len(hits)} candidates")

# Phase 2: Accurate reranking with cross-encoder
sentence_pairs = [[query, answers[hit['corpus_id']]] for hit in hits]
cross_scores = cross_encoder.predict(sentence_pairs)

# Sort by cross-encoder scores
for idx in range(len(cross_scores)):
    hits[idx]['cross-score'] = cross_scores[idx]

hits = sorted(hits, key=lambda x: x['cross-score'], reverse=True)

print("\nTop 5 results after reranking:")
for hit in hits[0:5]:
    print(f"  Score: {hit['cross-score']:.2f} - {answers[hit['corpus_id']]}")
```

## Using SparseEncoder for Sparse Embeddings

```python
from sentence_transformers import SparseEncoder

# Load a pre-trained SparseEncoder model
model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

# Encode sentences to sparse embeddings
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]

# Generate sparse embeddings
embeddings = model.encode(sentences)
print(f"Sparse embeddings shape: {embeddings.shape}")
# Sparse embeddings shape: [3, 30522]  # vocabulary size dimensions

# Calculate similarities (sparse dot product)
similarities = model.similarity(embeddings, embeddings)
print("Sparse similarities:")
print(similarities)
# tensor([[   35.629,     9.154,     0.098],
#         [    9.154,    27.478,     0.019],
#         [    0.098,     0.019,    29.553]])

# Check sparsity statistics
stats = SparseEncoder.sparsity(embeddings)
print(f"Sparsity ratio: {stats['sparsity_ratio']:.2%}")
print(f"Active dimensions: {stats['active_dims']:.1f}")
# Sparsity ratio: 99.84%
# Active dimensions: 48.7
```

## Clustering Embeddings

```python
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

model = SentenceTransformer("all-MiniLM-L6-v2")

# Corpus to cluster
corpus = [
    "A man is eating food.",
    "A man is eating a piece of bread.",
    "A man is eating pasta.",
    "The girl is carrying a baby.",
    "The baby is carried by the woman",
    "A man is riding a horse.",
    "A man is riding a white horse on an enclosed ground.",
    "A monkey is playing drums.",
    "Someone in a gorilla costume is playing a set of drums.",
]

# Encode all sentences
corpus_embeddings = model.encode(corpus)

# Perform K-means clustering
num_clusters = 3
clustering_model = KMeans(n_clusters=num_clusters, random_state=42)
clustering_model.fit(corpus_embeddings)
cluster_assignment = clustering_model.labels_

# Organize sentences by cluster
clustered_sentences = [[] for _ in range(num_clusters)]
for sentence_id, cluster_id in enumerate(cluster_assignment):
    clustered_sentences[cluster_id].append(corpus[sentence_id])

# Display clusters
for i, cluster in enumerate(clustered_sentences):
    print(f"Cluster {i + 1}:")
    for sentence in cluster:
        print(f"  - {sentence}")
    print()

# Output:
# Cluster 1:
#   - A man is eating food.
#   - A man is eating a piece of bread.
#   - A man is eating pasta.
#
# Cluster 2:
#   - The girl is carrying a baby.
#   - The baby is carried by the woman
# ...
```

## Paraphrase Mining

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

# Large list of sentences (can be tens of thousands)
sentences = [
    "The cat sits outside",
    "A man is playing guitar",
    "I love pasta",
    "The new movie is awesome",
    "The cat plays in the garden",
    "A woman watches TV",
    "The new movie is so great",
    "Do you like pizza?",
    "The cat is in the garden",
]

# Find paraphrases efficiently (uses chunking internally)
paraphrases = util.paraphrase_mining(
    model,
    sentences,
    top_k=100,  # Top-k similar sentences per sentence
    query_chunk_size=5000,  # Process queries in chunks
    corpus_chunk_size=100000,  # Compare against chunks of corpus
    max_pairs=500000  # Maximum paraphrase pairs to return
)

print("Top 10 paraphrase pairs:")
for idx, (score, i, j) in enumerate(paraphrases[0:10]):
    print(f"{idx + 1}. Score: {score:.4f}")
    print(f"   - {sentences[i]}")
    print(f"   - {sentences[j]}\n")

# Output:
# Top 10 paraphrase pairs:
# 1. Score: 0.8932
#    - The new movie is awesome
#    - The new movie is so great
#
# 2. Score: 0.7821
#    - The cat sits outside
#    - The cat plays in the garden
# ...
```

## Mining Hard Negatives

```python
from sentence_transformers import SentenceTransformer, mine_hard_negatives
from datasets import load_dataset

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load dataset with anchor and positive pairs
# Expected format: Dataset with "anchor" and "positive" columns
dataset = load_dataset("sentence-transformers/natural-questions", split="train[:1000]")

# Mine hard negatives from a corpus
corpus = [
    "Machine learning is a subset of artificial intelligence.",
    "Deep learning uses neural networks with multiple layers.",
    "Python is a popular programming language.",
    "The Eiffel Tower is located in Paris.",
    # ... thousands more documents
]

# Mine hard negatives for training
dataset_with_negatives = mine_hard_negatives(
    dataset=dataset,
    model=model,
    anchor_column_name="anchor",
    positive_column_name="positive",
    corpus=corpus,
    num_negatives=3,  # Number of hard negatives per sample
    sampling_strategy="top",  # "top" or "random"
    range_min=10,  # Exclude top 10 most similar (too easy)
    range_max=100,  # Only consider top 100 candidates
    batch_size=32,
    use_faiss=True,  # Use FAISS for faster search
    output_format="triplet"  # "triplet", "n-tuple", "labeled-pair", etc.
)

# The resulting dataset includes hard negative examples
print(dataset_with_negatives[0])
# {'anchor': '...', 'positive': '...', 'negative': '...'}

# Alternative: Use relative margin for filtering
dataset_with_negatives = mine_hard_negatives(
    dataset=dataset,
    model=model,
    corpus=corpus,
    num_negatives=5,
    relative_margin=0.1,  # Select negatives within 10% of positive score
    output_format="n-tuple"  # Returns multiple negatives per anchor
)
```

## Quantizing Embeddings for Efficiency

```python
from sentence_transformers import SentenceTransformer, quantize_embeddings
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
sentences = ["This is a sentence" for _ in range(100)]
embeddings = model.encode(sentences)

print(f"Original embeddings: {embeddings.shape}, dtype: {embeddings.dtype}")
# Original embeddings: (100, 384), dtype: float32

# Quantize to int8 (256 values)
int8_embeddings = quantize_embeddings(embeddings, precision="int8")
print(f"Int8 embeddings: {int8_embeddings.shape}, dtype: {int8_embeddings.dtype}")
# Int8 embeddings: (100, 384), dtype: int8
print(f"Memory reduction: {embeddings.nbytes / int8_embeddings.nbytes:.1f}x")
# Memory reduction: 4.0x

# Quantize to uint8 (256 values)
uint8_embeddings = quantize_embeddings(embeddings, precision="uint8")

# Quantize to binary (2 values per dimension: -1 or 1)
binary_embeddings = quantize_embeddings(embeddings, precision="binary")
print(f"Binary embeddings: {binary_embeddings.shape}, dtype: {binary_embeddings.dtype}")
# Binary embeddings: (100, 384), dtype: int8
print(f"Memory reduction: {embeddings.nbytes / binary_embeddings.nbytes:.1f}x")
# Memory reduction: 4.0x (values are -1/1 but stored as int8)

# Quantize to ubinary (unsigned binary: 0 or 1, packed as bits)
ubinary_embeddings = quantize_embeddings(embeddings, precision="ubinary")
print(f"Ubinary embeddings: {ubinary_embeddings.shape}, dtype: {ubinary_embeddings.dtype}")
# Ubinary embeddings: (100, 48), dtype: uint8  # 384 bits packed into 48 bytes
print(f"Memory reduction: {embeddings.nbytes / ubinary_embeddings.nbytes:.1f}x")
# Memory reduction: 32.0x

# Use calibration embeddings for better quantization
calibration_sentences = ["Sample sentence " + str(i) for i in range(1000)]
calibration_embeddings = model.encode(calibration_sentences)

int8_calibrated = quantize_embeddings(
    embeddings,
    precision="int8",
    calibration_embeddings=calibration_embeddings
)
```

## Training a SentenceTransformer Model

```python
from sentence_transformers import SentenceTransformer, losses
from sentence_transformers.trainer import SentenceTransformerTrainer
from sentence_transformers.training_args import SentenceTransformerTrainingArguments
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator
from sentence_transformers.similarity_functions import SimilarityFunction
from datasets import load_dataset

# Load a base transformer model
model = SentenceTransformer("bert-base-uncased")

# Load training dataset (NLI format: sentence1, sentence2, label)
train_dataset = load_dataset("sentence-transformers/all-nli", "pair-class", split="train")
eval_dataset = load_dataset("sentence-transformers/all-nli", "pair-class", split="dev")

# Define loss function
train_loss = losses.SoftmaxLoss(
    model=model,
    sentence_embedding_dimension=model.get_sentence_embedding_dimension(),
    num_labels=3  # 3 classes: entailment, contradiction, neutral
)

# Define evaluator
stsb_dataset = load_dataset("sentence-transformers/stsb", split="validation")
evaluator = EmbeddingSimilarityEvaluator(
    sentences1=stsb_dataset["sentence1"],
    sentences2=stsb_dataset["sentence2"],
    scores=stsb_dataset["score"],
    main_similarity=SimilarityFunction.COSINE,
    name="sts-dev"
)

# Training arguments
args = SentenceTransformerTrainingArguments(
    output_dir="output/my-model",
    num_train_epochs=1,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    warmup_ratio=0.1,
    fp16=True,
    evaluation_strategy="steps",
    eval_steps=100,
    save_strategy="steps",
    save_steps=100,
    save_total_limit=2,
    logging_steps=100,
    run_name="my-training-run"
)

# Create trainer and train
trainer = SentenceTransformerTrainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    loss=train_loss,
    evaluator=evaluator
)

trainer.train()

# Save the final model
model.save("output/my-model/final")

# Push to Hugging Face Hub (optional)
model.push_to_hub("my-username/my-sentence-transformer")
```

## Training a CrossEncoder Model

```python
from sentence_transformers import CrossEncoder
from sentence_transformers.cross_encoder import CrossEncoderTrainer, CrossEncoderTrainingArguments
from sentence_transformers.cross_encoder.evaluation import CEBinaryClassificationEvaluator
from datasets import load_dataset

# Load a base model
model = CrossEncoder("distilbert-base-uncased", num_labels=1)

# Load dataset (format: sentence1, sentence2, score)
train_dataset = load_dataset("sentence-transformers/stsb", split="train")
eval_dataset = load_dataset("sentence-transformers/stsb", split="validation")

# Define evaluator
evaluator = CEBinaryClassificationEvaluator(
    sentence_pairs=list(zip(eval_dataset["sentence1"], eval_dataset["sentence2"])),
    labels=eval_dataset["score"],
    name="sts-dev"
)

# Training arguments
args = CrossEncoderTrainingArguments(
    output_dir="output/cross-encoder",
    num_train_epochs=1,
    per_device_train_batch_size=16,
    warmup_ratio=0.1,
    fp16=True,
    evaluation_strategy="steps",
    eval_steps=100,
    save_steps=100,
    run_name="cross-encoder-training"
)

# Create trainer and train
trainer = CrossEncoderTrainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    evaluator=evaluator
)

trainer.train()

# Save model
model.save("output/cross-encoder/final")
```

## Multi-GPU and Multi-Process Encoding

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# Large corpus
sentences = ["This is sentence " + str(i) for i in range(100000)]

# Automatic multi-process encoding
# The pool parameter triggers multi-process encoding
embeddings = model.encode(
    sentences,
    batch_size=32,
    show_progress_bar=True,
    pool={
        "processes": 4,  # Number of processes to use
        "input": None,  # Input queue (auto-created)
        "output": None  # Output queue (auto-created)
    }
)

# Or specify device list for multi-GPU encoding
embeddings_multi_gpu = model.encode(
    sentences,
    batch_size=32,
    device=["cuda:0", "cuda:1"],  # Use multiple GPUs
    show_progress_bar=True
)

print(f"Encoded {len(embeddings)} sentences")
# Encoded 100000 sentences
```

## Using Prompts with Models

```python
from sentence_transformers import SentenceTransformer

# Load model with prompts
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    prompts={
        "query": "query: ",
        "passage": "passage: ",
        "clustering": "Identify the category: "
    },
    default_prompt_name="query"
)

# Encode with default prompt (query)
query_embedding = model.encode("What is Python?")

# Encode with specific prompt
passage_embedding = model.encode("Python is a programming language", prompt_name="passage")

# Encode with custom prompt
custom_embedding = model.encode("Machine learning topic", prompt="Classify this text: ")

# Different prompts for different use cases
queries = ["How to learn Python?", "Best practices for coding"]
documents = ["Python tutorial for beginners", "Clean code principles"]

query_embs = model.encode(queries, prompt_name="query")
doc_embs = model.encode(documents, prompt_name="passage")

similarities = model.similarity(query_embs, doc_embs)
print(similarities)
```

## Model Saving and Loading

```python
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Save to local directory
model.save("my-local-model")

# Load from local directory
loaded_model = SentenceTransformer("my-local-model")

# Save to Hugging Face Hub
model.push_to_hub(
    repo_id="my-username/my-model",
    private=False,
    commit_message="Initial model upload"
)

# Load from Hugging Face Hub
hub_model = SentenceTransformer("my-username/my-model")

# Save with specific components
model.save("my-model", safe_serialization=True)

# Export to ONNX for faster inference
from sentence_transformers import export_optimized_onnx_model

export_optimized_onnx_model(
    model_name="all-MiniLM-L6-v2",
    output_path="my-onnx-model"
)

# Load ONNX model
onnx_model = SentenceTransformer("my-onnx-model", backend="onnx")
```

## Summary

Sentence Transformers provides a complete toolkit for embedding-based NLP applications with three core functionalities: computing embeddings with SentenceTransformer, reranking with CrossEncoder, and generating sparse embeddings with SparseEncoder. The library supports semantic search, clustering, paraphrase mining, hard negative mining, and information retrieval out of the box. Training custom models is straightforward using the Trainer API with various loss functions for different tasks like classification, similarity learning, and contrastive learning. The framework includes built-in evaluation metrics and integrates seamlessly with the Hugging Face ecosystem.

Key integration patterns include using bi-encoders for fast initial retrieval followed by cross-encoders for accurate reranking, mining hard negatives for improved training data quality, quantizing embeddings for memory-efficient storage and faster search, and leveraging multi-GPU/multi-process encoding for large-scale applications. The library supports exporting models to ONNX and OpenVINO backends for production deployment, provides prompt engineering capabilities for instruction-based models, and integrates with vector databases like FAISS and Elasticsearch. With minimal code, developers can implement state-of-the-art semantic search systems, build recommendation engines, perform document clustering, and create conversational AI applications that understand semantic meaning beyond keyword matching.
