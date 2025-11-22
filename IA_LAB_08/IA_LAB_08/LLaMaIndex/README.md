# LLaMaIndex — Evidencias del Laboratorio 8 (IA)

Este directorio contiene las evidencias correspondientes al Punto 9 del Laboratorio 8 – Construcción de una base de conocimiento y pipeline RAG usando LLaMaIndex.  
El objetivo fue integrar documentos propios, indexarlos y permitir consultas basadas en evidencia.

---

## 1. Base de conocimiento creada

Se construyó una base de conocimiento con **5 documentos** relacionados con el proyecto MORITA.  
Los documentos incluyen:

- Objetivo general  
- Objetivos operativos  
- Beneficios esperados  
- Módulos del sistema  
- Justificación de digitalización  

---

## 2. Notebook de implementación

El archivo **rag_demo.ipynb** incluye:

- Creación de documentos locales  
- Lectura mediante SimpleDirectoryReader  
- Construcción de un VectorStoreIndex  
- Consulta con Query Engine  
- Validación del grounding (respuestas basadas en texto cargado)

Este notebook cumple con los requisitos del laboratorio para el pipeline RAG.

---

## 3. Script adicional del pipeline

Se incluye el archivo **rag_pipeline.py**, que demuestra cómo:

- Cargar documentos desde la carpeta `docs/`  
- Construir un índice vectorial  
- Consultar el sistema desde un script independiente  

---

## 4. Validación del Grounding

Las respuestas generadas fueron consistentes con los documentos cargados:

- No se detectaron invenciones (“alucinaciones”)  
- El modelo citó contenido presente en los textos  
- La respuesta a cada consulta se basó estrictamente en la evidencia disponible  

---

## 5. Evidencias

- `rag_demo.ipynb` — Pipeline RAG completo  
- `rag_pipeline.py` — Script del pipeline  
- Las capturas están en el informe general (no obligatorio subirlas aquí)

---


