# Hugging Face — Evidencias del Laboratorio 8 (IA)

Este directorio contiene las evidencias correspondientes al Punto 1 del Laboratorio 8 – Exploración y uso avanzado de plataformas IA.  
Las actividades realizadas corresponden al uso del ecosistema **Hugging Face** para búsqueda de modelos, ejecución de inferencias y creación de un Space funcional.

---

## Evidencias Incluidas

### 1. Notebook ejecutado en Google Colab  
**Archivo:** *1_HuggingFace_FLAN_T5_Small.ipynb*  
- Se ejecuta el modelo **google/flan-t5-small** usando la librería *transformers*.  
- Se realizan dos inferencias:  
  - Explicación de un concepto técnico.  
  - Mensaje motivacional contextualizado en el proyecto MORITA.  
- Se evidencia la carga del modelo, creación del pipeline y generación de texto.

---

### 2. Código del Hugging Face Space  
**Archivo:** *app.py*  
- Implementa una interfaz desarrollada con **Gradio**.  
- La función `responder()` utiliza el modelo **FLAN-T5-Small** para contestar preguntas.  
- El archivo está listo para desplegarse como un Space funcional.

---

### 3. Dependencias del Space  
**Archivo:** *requirements.txt*  
Incluye las dependencias necesarias:  
- transformers  
- torch  
- accelerate  
- gradio  

---

### 4. Descripción general de la actividad  
El objetivo de este punto fue:  
- Explorar modelos en el catálogo de Hugging Face.  
- Ejecutar un modelo en un notebook.  
- Construir y documentar un Space funcional.  
- Subir todas las evidencias al repositorio GitHub.

---

## Estado del entregable

✔ Notebook ejecutado  
✔ Código del Space  
✔ Archivo de dependencias  
✔ Carpeta documentada  
