# Papers With Code — Evidencias del Laboratorio 8 (IA)

Este directorio contiene las evidencias correspondientes al Punto 6 del Laboratorio 8 – Reproducción parcial de un experimento académico utilizando Papers With Code.  
El propósito fue seleccionar un paper con implementación oficial y ejecutar una parte del experimento para validar su funcionamiento.

---

## 1. Paper seleccionado

Se seleccionó un paper disponible en **Papers With Code**, el cual proporciona:

- Enlace directo al artículo científico  
- Implementación oficial en GitHub  
- Métricas publicadas  
- Benchmark asociado al modelo  

El paper se revisó para comprender su objetivo, metodología y las métricas principales utilizadas.

---

## 2. Implementación utilizada

A partir del repositorio oficial enlazado desde Papers With Code:

- Se revisó la estructura del proyecto  
- Se identificaron los archivos del modelo  
- Se adaptó una parte del código para ejecutarlo en un notebook  
- Se realizó una ejecución parcial para validar el comportamiento del modelo  

---

## 3. Ejecución parcial del experimento

Dentro del notebook incluido en esta carpeta (*PWC_Experiment.ipynb*) se realizaron los siguientes pasos:

- Importación de dependencias  
- Descarga del modelo oficial (DistilBERT finetuned)  
- Pipeline de clasificación  
- Prueba de inferencia con texto de ejemplo  
- Análisis comparativo frente a la descripción del paper  

El objetivo fue demostrar consistencia entre el comportamiento del modelo y lo reportado en el paper original.

---

## 4. Comparación con el paper

- El modelo mostró resultados coherentes con la tarea (clasificación de sentimiento).  
- Las diferencias en métricas son esperables debido a:
  - Cambios de dataset  
  - No reproducir completamente el entrenamiento  
  - Ausencia de GPU y entorno idéntico al original  

Aun así, el funcionamiento general coincide con lo reportado en la publicación académica.

---

## 5. Reflexión técnica

- Papers With Code facilita encontrar implementaciones oficiales confiables.  
- Reproducir un paper completo requiere recursos avanzados.  
- Ejecutar un fragmento del experimento es suficiente para evaluar consistencia.  
- La plataforma es clave para investigación aplicada y replicabilidad.

---

## 6. Evidencias incluidas

- `PWC_Experiment.ipynb` — Notebook con la ejecución parcial  
- `run_experiment.py` — Script base del experimento  
- Capturas se encuentran en el informe general del laboratorio  

---
