# Hugging Face — Evidencias del Laboratorio 8 (IA)

Este directorio contiene las evidencias correspondientes al Punto 1 del Laboratorio 8 – Exploración y uso avanzado de plataformas IA.
Las actividades realizadas corresponden al uso del ecosistema Hugging Face para búsqueda de modelos, ejecución de inferencias y creación de un Space funcional.

Evidencias Incluidas
1. Notebook ejecutado en Google Colab

Archivo: 1_HuggingFace_FLAN_T5_Small.ipynb

Se ejecuta el modelo google/flan-t5-small usando la librería transformers.

Se realizan dos pruebas de inferencia (concepto técnico y mensaje motivacional contextualizado al proyecto MORITA).

Se evidencia la carga del modelo, creación del pipeline y generación de texto.

2. Código del Hugging Face Space

Archivo: app.py

Implementa una interfaz desarrollada con Gradio.

La función responder() usa el modelo FLAN-T5-Small para contestar preguntas.

El archivo está listo para un despliegue real en Hugging Face Spaces.

3. Dependencias del Space

Archivo: requirements.txt
Incluye las dependencias necesarias para ejecutar la aplicación (transformers, torch, accelerate y gradio).

4. Descripción general de la actividad

El objetivo de este punto fue:

Explorar modelos en el catálogo de Hugging Face.

Ejecutar un modelo en un notebook.

Construir y documentar un Space funcional.

Subir las evidencias completas al repositorio GitHub.
