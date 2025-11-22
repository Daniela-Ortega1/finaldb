# Modelscope (Alibaba) — Evidencias del Laboratorio 8 (IA)

Este directorio contiene las evidencias correspondientes al Punto 8 del Laboratorio 8 – Uso de Modelscope como repositorio alternativo de modelos open-source.  
El propósito fue ejecutar un modelo disponible en Modelscope, analizar su eficiencia y compararlo con un modelo equivalente en Hugging Face.

---

## 1. Modelo ejecutado

Se utilizó un modelo de **clasificación de imágenes** disponible en Modelscope:

**Modelo:** `damo/cv_resnet50_image-classification_imagenet`  
**Tarea:** Image Classification  
**Pipeline:** `Tasks.image_classification`

El modelo fue seleccionado por su velocidad, compatibilidad y facilidad de uso en entornos educativos.

---

## 2. Script ejecutado

En esta carpeta se incluye el archivo:

- `modelscope_demo.py`

Este script demuestra:

- Cómo importar pipelines de Modelscope  
- Cómo cargar un modelo preentrenado  
- Cómo ejecutar una inferencia sobre una imagen de prueba  
- Cómo imprimir el resultado de la clasificación  

---

## 3. Comparación con Hugging Face

Se comparó la eficiencia del modelo de Modelscope con un modelo equivalente de Hugging Face (por ejemplo, ResNet-50):

### • Modelscope  
- Tiempo de carga rápido  
- Pipeline unificado para visión  
- Ejecución estable  

### • Hugging Face  
- Mayor variedad de modelos  
- Librería Transformers mejor documentada  
- Tiempo de inferencia muy similar  

**Conclusión:**  
Ambas plataformas ofrecen rendimiento comparable, pero Hugging Face tiene mejor ecosistema y documentación, mientras Modelscope es útil para probar alternativas optimizadas y modelos de Alibaba.

---

## 4. Evidencias

- Script: `modelscope_demo.py`  
- La gráfica comparativa y capturas están incluidas en el informe general del laboratorio (no obligatorio subirlas aquí).

---
  
