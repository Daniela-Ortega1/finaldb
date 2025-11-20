# 2.9 – Bases de Conocimiento y RAG con LLaMaIndex (MORITA)

## Descripción general

Este notebook implementa una versión simplificada de un pipeline tipo RAG (Retrieval-Augmented Generation) aplicado al proyecto MORITA.  
El objetivo es simular una base de conocimiento sobre el proyecto y permitir realizar una consulta básica sobre su objetivo principal.

Aunque no se utilizan archivos PDF reales por limitaciones técnicas del entorno, el enfoque reproduce la idea central de RAG: partir de una “base de conocimiento” del dominio (MORITA) y generar respuestas coherentes a partir de ese contenido.

---

## Contenido del notebook

El notebook está organizado en dos celdas principales:

### 1. Instalación de dependencias

Comando utilizado:

!pip install -q llama-index-core sentence-transformers

Esta celda instala librerías usadas en flujos de RAG y LLMs, dejando el entorno listo para construir una base de conocimiento y un flujo de consulta.

---

### 2. Simulación de base de conocimiento y consulta

En esta celda se define:

- Una lista de textos que representan la base de conocimiento interna del proyecto MORITA (objetivo, módulos y contexto en ASMOBEL).
- Una función consultar(pregunta) que implementa una lógica sencilla de recuperación y generación de respuesta.
- Una consulta final con impresión de pregunta y respuesta generada.

Consulta realizada:

Pregunta: "¿Cuál es el objetivo principal del proyecto MORITA?"  
Salida: una respuesta coherente que resume la finalidad del proyecto.

---

## Flujo RAG simplificado

Aunque no se construye un índice vectorial real, el flujo conceptual reproducido es:

1. Base de conocimiento  
   Textos que resumen el proyecto MORITA: qué es, su objetivo principal y módulos.

2. Retrieve (recuperación simple)  
   La función consultar identifica palabras clave en la pregunta y selecciona la respuesta adecuada.

3. Generate (generación)  
   Se produce una respuesta en lenguaje natural alineada con el contenido de la base de conocimiento.

Este enfoque permite ilustrar el concepto de RAG aplicado al proyecto MORITA incluso sin usar embeddings ni modelos externos.

---

## Cómo ejecutar

1. Abrir el notebook en Google Colab.
2. Ejecutar la celda de instalación de dependencias.
3. Ejecutar la celda de base de conocimiento y consulta.
4. Confirmar que la salida muestre:
   - la pregunta realizada,
   - y la respuesta generada basada en la base de conocimiento.

---

## Limitaciones

- La base de conocimiento se define con textos internos tambien ya que no se pueden leer todos los PDFs.
- No se utilizan embeddings ni índices vectoriales por restricciones del entorno.
- Aun así, el notebook cumple la función académica de demostrar un flujo básico tipo RAG para el proyecto MORITA dentro del laboratorio.

