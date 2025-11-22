# -------------------------------------------------------------------------
# Replicate API – Ejecución de un modelo generativo (Stable Diffusion)
# Laboratorio 8 - Inteligencia Artificial
# -------------------------------------------------------------------------

import replicate

def generar_imagen(prompt):
    """
    Función que genera una imagen usando Stable Diffusion desde Replicate.
    El propósito es demostrar el consumo de un modelo vía API.
    """
    
    # NOTA:
    # Este token no se incluye por seguridad.
    # El estudiante debe configurar manualmente su variable de entorno:
    #
    #   export REPLICATE_API_TOKEN="tu_token_aqui"
    #
    # Para el laboratorio basta con incluir el script.
    
    model = "stability-ai/stable-diffusion"

    # Solicitud a la API
    output = replicate.run(
        model,
        input={"prompt": prompt}
    )

    return output


if __name__ == "__main__":
    prompt_prueba = "A futuristic classroom powered by artificial intelligence, ultra-detailed"
    
    print("Prompt usado:", prompt_prueba)
    print("Generando imagen...")
    
    resultado = generar_imagen(prompt_prueba)
    
    print("\nResultado generado por el modelo:")
    print(resultado)
