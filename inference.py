from find_similar import retriever_chroma
from llm_openai import get_openai_llm
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os

# check https://colab.research.google.com/drive/1gyGZn_LZNrYXYXa-pltFExbptIe7DAPe?usp=sharing#scrollTo=LZEo26mw8e5k

clear = lambda: os.system("clear")

prompt_template = (
    "Answer this question: {question} based on following document text: {information}. Use your creativity and answer in interesting way."
)

llm = get_openai_llm()

chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever_chroma(),
    return_source_documents=True,
)

def chat():
    input_question = "test"
    clear()
    print("Welcome! \t Write /exit to exit.")
    while True:
        print("\n")
        input_question = input("Question: ")
        if input_question == "q" or input_question == "Q":
            print("Goodbye! \n")
            break

        llm_response = chain(input_question)
        print('\n'+llm_response["result"])


if __name__ == "__main__":
    chat()
