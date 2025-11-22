# -------------------------------------------------------------------------
# Modelscope - Ejecución de un modelo de visión por computadora
# Laboratorio 8 - Inteligencia Artificial
# -------------------------------------------------------------------------

from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

def ejecutar_modelo():
    """
    Prueba básica usando un modelo de Modelscope.
    El propósito es mostrar cómo cargar y ejecutar un modelo real.
    """

    # Modelo de clasificación de imágenes (liviano y rápido)
    modelo = pipeline(
        Tasks.image_classification,
        model='damo/cv_resnet50_image-classification_imagenet'
    )

    # Imagen de prueba incluida en el repositorio oficial
    imagen = 'https://modelscope.cn/api/v1/models/damo/cv_resnet50_image-classification_imagenet/repo?path=test.jpg&revision=master'

    print("Ejecutando clasificación de imagen...")
    salida = modelo(imagen)

    print("\nResultado del modelo:")
    print(salida)


if __name__ == "__main__":
    ejecutar_modelo()
