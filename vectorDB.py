from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import chroma
import asyncio
from getKeys import OPENAI_KEY


# load, vectorize, and store documents
_raw_documents = TextLoader('./test.txt').load()
_text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
_documents = _text_splitter.split_documents(_raw_documents)

vector_db = chroma.Chroma.from_documents(_documents, OpenAIEmbeddings(openai_api_key=OPENAI_KEY))

