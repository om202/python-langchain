from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import faiss, chroma
from llm_openai import get_openai_embeddings

# load, vectorize, and store documents
_raw_documents = TextLoader("./test.txt").load()
_text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
_documents = _text_splitter.split_documents(_raw_documents)

# for chroma db use:
vector_chroma_db = chroma.Chroma.from_documents(documents=_documents, embedding=get_openai_embeddings(), persist_directory='chroma')
vector_chroma_db.persist()

@staticmethod
def get_chroma_vector_db():
  vector_db = chroma.Chroma(persist_directory='chroma', embedding_function=get_openai_embeddings())
  return vector_db
