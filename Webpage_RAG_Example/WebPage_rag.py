import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
import ollama

class RAGPipeline:
    def __init__(self, model: str, web_path: str, persist_directory: str, chunk_size: int = 1000, chunk_overlap: int = 200):
        # Set environment variable
        os.environ['USER_AGENT'] = 'myagent'
        
        self.model = model
        
        # Initialize web loader
        self.loader = WebBaseLoader(web_path=web_path, show_progress=True)
        
        # Load and split documents
        self.docs = self.loader.load()
        self.text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.splits = self.text_splitter.split_documents(self.docs)
        
        # Create Ollama embeddings and vector store
        self.embeddings = OllamaEmbeddings(model=model)
        self.vectorstore = Chroma(persist_directory=persist_directory, embedding_function=self.embeddings)
        
        # Create the retriever
        self.retriever = self.vectorstore.as_retriever(search_type="mmr", search_kwargs={'k': 1, 'fetch_k': 2})
    
    def format_docs(self, docs):
        """Format documents for display."""
        return "\n\n".join(doc.page_content for doc in docs)
    
    def ollama_run(self, question, context):
        """Query the Ollama LLM with a question and context."""
        formatted_prompt = f"""Answer the question based on the context below. If the question cannot be answered using the information provided, answer with "I don't know".

        Context: {context}

        Question: {question}
        """
        response = ollama.chat(model=self.model, messages=[{'role': 'user', 'content': formatted_prompt}])
        return response['message']['content']
    
    def rag_chain(self, question):
        """Run the RAG chain process for a given question."""
        print("Started invoking")
        retrieved_docs = self.retriever.invoke(question)
        formatted_context = self.format_docs(retrieved_docs)
        print("Completed invoke")
        return self.ollama_run(question, formatted_context)

# Example usage
query = "Explain about Python"
rag_pipeline = RAGPipeline(
    model="phi",
    web_path="https://en.wikipedia.org/wiki/Python_(programming_language)",
    persist_directory="./chroma_db"
)
result = rag_pipeline.rag_chain(query)
print(result)
