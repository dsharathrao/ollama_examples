
# WEB RAG Example

The **RAGPipeline** is a Python class for implementing a Retrieval-Augmented Generation (RAG) process. It combines document retrieval and large language model (LLM) capabilities to answer questions based on retrieved context. This class encapsulates the entire workflow, including document loading, splitting, embedding, storing, and querying.

## Features

- **Web Document Loading**: Load documents from the web using a URL.
- **Document Splitting**: Split documents into manageable chunks for better context handling.
- **Embedding and Vector Store**: Utilize embeddings and vector stores for efficient retrieval.
- **RAG Chain**: Perform retrieval and answer generation in a seamless workflow.

## Installation

To use the RAGPipeline, you need to have the following packages installed:

- `langchain`
- `langchain_community`
- `ollama`
- `os`

You can install these packages using pip:

```bash
pip install langchain langchain_community ollama
```

## Usage

### Initializing the Pipeline

To initialize the pipeline, create an instance of the `RAGPipeline` class with the required parameters such as model, web path, and persist directory.

```python
from rag_pipeline import RAGPipeline

# Initialize the pipeline with the desired model and web path
rag_pipeline = RAGPipeline(
    model="phi",
    web_path="https://en.wikipedia.org/wiki/Python_(programming_language)",
    persist_directory="./chroma_db"
)
```

### Running the RAG Chain

To run the RAG chain process, use the `rag_chain` method with a specific question. The method will return an answer based on the retrieved documents.

```python
# Define a question
query = "Explain about Python"

# Get the answer using the RAG chain
result = rag_pipeline.rag_chain(query)
print(result)
```

### Example Output

The output will provide an answer to the question based on the context retrieved from the documents:

```
Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms...
```

## Customization

You can easily customize the RAGPipeline by changing the model, web path, chunk size, chunk overlap, and other parameters during initialization. This allows for flexibility in handling different types of documents and queries.

## TODO
- GUI
- Error handling
- Add LlamaIndex, Haystack, RAGatouille, EmbedChain etc., based option.
- Benchmark results
- more