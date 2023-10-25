from vectorDB import vector_db

def similaritySearch(query):
  result = vector_db.similarity_search(query)
  return result[0].page_content