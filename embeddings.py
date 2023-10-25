from langchain.embeddings import OpenAIEmbeddings
from getKeys import OPENAI_KEY

embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)

embeddings_multi_text = embedding_model.embed_documents(
    ["I enjoy walking with my cute dog.", "I love eating ice cream."]
)

embeddings_text = embedding_model.embed_query("I enjoy walking with my cute dog.")

print(embeddings_text)
