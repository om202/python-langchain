from findSimilar import similaritySearch
from llm_openai import get_openai_llm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

prompt_template = "Answer this question: {question}"
inputQuestion = "null"

if inputQuestion:
    llm = get_openai_llm()
    print("Write /exit to exit.")
    while inputQuestion != "/exit":
        if inputQuestion == "/exit":
            break
        print("\n")
        inputQuestion = input("Question: ")
        chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt_template))
        ans = chain(inputQuestion)
        print(ans["text"])
else:
    print("No input question found.")
