from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def ejecutar_experimento():
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    
    clf = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    texto_prueba = "This system improves the overall efficiency of the production workflow."
    resultado = clf(texto_prueba)

    print("Texto analizado:", texto_prueba)
    print("Resultado del modelo:", resultado)

if __name__ == "__main__":
    ejecutar_experimento()
