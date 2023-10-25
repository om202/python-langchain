from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from getKeys import OPENAI_KEY

def get_openai_llm():
    return OpenAI(openai_api_key=OPENAI_KEY)

def get_openai_embeddings():
    return  OpenAIEmbeddings(openai_api_key=OPENAI_KEY)