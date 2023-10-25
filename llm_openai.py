from langchain.llms import OpenAI
from getKeys import OPENAI_KEY

def get_openai_llm():
    return OpenAI(openai_api_key=OPENAI_KEY)