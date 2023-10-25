from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import chroma
import asyncio
from getKeys import OPENAI_KEY

async def search(query):
  found_docs = await db.amax_marginal_relevance_search(query, k=2, fetch_k=10)
  return found_docs

# load, vectorize, and store documents
raw_documents = TextLoader('./test.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db = chroma.Chroma.from_documents(documents, OpenAIEmbeddings(openai_api_key=OPENAI_KEY))

query = "What is area of birgunj?"

# Similarity search
# docs = db.similarity_search(query)
# print(docs[0].page_content)

# MMR Search
found_docs = asyncio.run(search(query))
for i, doc in enumerate(found_docs):
    print(f"{i + 1}.", doc.page_content, "\n")
