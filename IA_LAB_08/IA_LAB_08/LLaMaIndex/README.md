# 2.9 – Bases de Conocimiento y RAG con LLaMaIndex (MORITA)

## Descripción general

Este notebook implementa una versión simplificada de un pipeline tipo RAG (Retrieval-Augmented Generation) aplicado al proyecto **MORITA**.  
El objetivo es simular una base de conocimiento sobre el proyecto y permitir realizar una consulta básica sobre su objetivo principal.

Aunque no se utilizan archivos PDF reales por limitaciones técnicas del entorno, el enfoque reproduce la idea central de RAG:  
partir de una “base de conocimiento” del dominio (MORITA) y generar respuestas coherentes a partir de ese contenido.

---

## Contenido del notebook

El notebook está organizado en dos celdas principales:

### 1. Instalación de dependencias

```python
!pip install -q llama-index-core sentence-transformers

Esta celda instala librerías típicamente usadas en flujos de RAG y LLMs, dejando el entorno listo para construir una base de conocimiento y un flujo de consulta.

2. Simulación de base de conocimiento y consulta

En esta celda se define:

Una lista de textos que representan la base de conocimiento interna sobre el proyecto MORITA (objetivo, módulos, contexto en ASMOBEL).

Una función consultar(pregunta) que implementa una lógica sencilla de recuperación y generación de respuesta en función de la pregunta.

Una consulta final:

pregunta = "¿Cuál es el objetivo principal del proyecto MORITA?"
respuesta = consultar(pregunta)

print("Pregunta:")
print(pregunta)
print("\nRespuesta generada:")
print(respuesta)

La salida muestra la pregunta y una respuesta coherente con la definición del proyecto MORITA (sistema web integral para ASMOBEL, optimización de trazabilidad y procesos operativos).

Flujo RAG simplificado

Aunque no se indexan embeddings ni se usan modelos externos, el flujo conceptual es:

Base de conocimiento
Textos internos que resumen el proyecto MORITA (qué es, objetivo principal, módulos).

“Retrieve” (recuperación simplificada)
La función consultar() analiza la pregunta y decide qué fragmento de información devolver (por ejemplo, si contiene “objetivo”).

“Generate” (respuesta)
Se construye una respuesta en lenguaje natural, alineada con el contenido de la base de conocimiento.

Este enfoque permite ilustrar el concepto de RAG aplicado a un dominio específico (MORITA), incluso cuando el entorno no permite ejecutar una solución completa con índices vectoriales y embeddings reales.

Cómo ejecutar

Abrir el notebook en Google Colab.

Ejecutar la celda 1 (instalación de dependencias).

Ejecutar la celda 2 (base de conocimiento y consulta).

Verificar la salida que muestra:

La pregunta sobre el objetivo principal de MORITA.

Una respuesta generada a partir de la base de conocimiento interna.

Limitaciones

No se construye un índice vectorial real ni se usan embeddings en esta versión, debido a restricciones prácticas del entorno.

Sin embargo, el notebook cumple el propósito académico de ilustrar un flujo básico de consulta sobre información estructurada del proyecto MORITA, en el contexto de la actividad 2.9 del laboratorio.
