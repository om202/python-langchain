from vector_db import vector_db


def similarity_search(query):
    """
    Search for the most similar document to the query string
    Args:
        query (str): query string to search for
    Returns:
        str: most similar document
    """
    result = vector_db.similarity_search(query)
    return result[0].page_content
