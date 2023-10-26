from vector_db import get_chroma_vector_db

_chroma_db = get_chroma_vector_db()


def retriever_chroma():
    retriever = _chroma_db.as_retriever()
    return retriever
