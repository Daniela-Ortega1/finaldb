# -------------------------------------------------------------------------
# RAG Pipeline con LLaMaIndex - Laboratorio 8
# -------------------------------------------------------------------------

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

def crear_rag():
    # Cargar documentos desde la carpeta docs
    docs = SimpleDirectoryReader("docs").load_data()

    # Crear índice vectorial
    index = VectorStoreIndex.from_documents(docs)
    return index.as_query_engine()

if __name__ == "__main__":
    print("Iniciando pipeline RAG...\n")
    
    engine = crear_rag()
    pregunta = "¿Qué beneficios ofrece MORITA?"
    respuesta = engine.query(pregunta)

    print("Pregunta:", pregunta)
    print("Respuesta generada:")
    print(respuesta)
