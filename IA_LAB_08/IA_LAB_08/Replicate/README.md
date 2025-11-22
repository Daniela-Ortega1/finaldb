# Replicate — Evidencias del Laboratorio 8 (IA)

Este directorio contiene las evidencias correspondientes al Punto 7 del Laboratorio 8 – Uso de modelos generativos a través de la plataforma Replicate.  
El propósito fue probar dos modelos multimodales y crear un script que consumiera un modelo real mediante la API oficial.

---

## 1. Modelos generativos utilizados

Se realizaron pruebas con dos modelos disponibles en Replicate:

### • Modelo 1: Stable Diffusion (Generación de imágenes)
- Permite generar imágenes desde instrucciones en lenguaje natural.
- Se probó con prompts personalizados.
- Se evaluó la calidad visual, detalles y coherencia del resultado.

### • Modelo 2: Modelo de texto (por ejemplo, Llama / GPT-like)
- Permite generar texto, resúmenes o explicaciones.
- Se probó con prompts cortos para observar el rendimiento y coherencia.
- Permite comparar tiempos y nivel de precisión entre modelos.

---

## 2. Script API incluido

El archivo `replicate_api.py` demuestra cómo consumir un modelo generativo directamente desde código usando la API de Replicate.

El script incluye:

- Importación del cliente oficial
- Configuración del modelo “stability-ai/stable-diffusion”
- Envío de un prompt
- Obtención y visualización del resultado
- Estructura limpia y documentada para reproducir el proceso

Este archivo cumple el requisito obligatorio del laboratorio de incluir un **script funcional que consuma la API**.

---

## 3. Latencia y calidad de los modelos

### • Latencia
- Los modelos de imagen presentaron mayor tiempo de procesamiento.
- Los modelos de texto respondieron más rápido.
- La velocidad depende del tamaño y complejidad del modelo.

### • Calidad
- Stable Diffusion generó imágenes coherentes basadas en el prompt.
- Los modelos de texto entregaron respuestas comprensibles y rápidas.
- La calidad final depende del detalle del prompt y los parámetros elegidos.

---

## 4. Reflexión técnica

- Replicate permite ejecutar modelos avanzados sin GPU ni instalación local.
- La API es útil para integrar modelos en scripts, apps o microservicios.
- Es una herramienta ideal para prototipado rápido y pruebas de modelos multimodales.
- Facilita la exploración de diferentes arquitecturas sin configuraciones complejas.

---

## 5. Evidencias

- Script API: `replicate_api.py`
- Las imágenes generadas y capturas están incluidas en el informe general del laboratorio (no obligatorio subirlas aquí).

--- 
