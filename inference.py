from findSimilar import similaritySearch
from llm_openai import get_openai_llm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

clear = lambda: os.system('clear')

prompt_template = "Answer this question: {question} based on following info: {information}"
inputQuestion = "test"

if inputQuestion:
    llm = get_openai_llm()
    clear()
    print("Talk with documents :) \n Write /exit to exit.")
    while inputQuestion != "/exit":
        print("\n")
        inputQuestion = input("Question: ")
        similarity_result = similaritySearch(inputQuestion)
        chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt_template))
        ans = chain({'question': inputQuestion, 'information': similarity_result})
        print(ans["text"])
else:
    print("No input question found.")
