import gradio as gr
from transformers import pipeline

# Pipeline con el modelo FLAN-T5-Small
qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

def responder(pregunta: str) -> str:
    """
    Recibe una pregunta y devuelve una respuesta generada
    por el modelo FLAN-T5-Small.
    """
    if not pregunta.strip():
        return "Por favor escribe una pregunta."
    
    salida = qa_pipeline(
        pregunta,
        max_new_tokens=128
    )[0]["generated_text"]
    
    return salida

# Interfaz en Gradio
iface = gr.Interface(
    fn=responder,
    inputs=gr.Textbox(label="Escribe una pregunta"),
    outputs=gr.Textbox(label="Respuesta del Modelo"),
    title="Lab 08 - Hugging Face Space (FLAN-T5)",
    description="Demo sencilla usando FLAN-T5-Small para Q&A."
)

if __name__ == "__main__":
    iface.launch()
