from llm_openai import get_openai_embeddings

_embedding_model = get_openai_embeddings()

def get_embedding(query):
    embedding_text = _embedding_model.embed_query(query)
    return embedding_text
