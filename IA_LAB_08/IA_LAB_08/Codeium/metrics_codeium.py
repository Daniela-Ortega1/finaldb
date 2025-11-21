# Implementar una función que calcule el índice de calidad para MORITA.
# Fórmula: (kg_pulpa / kg_fruta) * 100.
# Debe validar que los parámetros sean positivos.
# El índice se devuelve como un número float.

def calcular_indice_calidad_morita(kg_pulpa, kg_fruta):
    """
    Calcula el índice de calidad para MORITA.

    Parámetros:
    kg_pulpa (float): Cantidad de pulpa en kilogramos.
    kg_fruta (float): Cantidad de fruta en kilogramos.

    Retorna:
    float: Índice de calidad calculado.

    Lanza:
    ValueError: Si alguno de los parámetros es negativo o cero.
    """

    if kg_pulpa <= 0:
        raise ValueError("La cantidad de pulpa debe ser un número positivo.")
    if kg_fruta <= 0:
        raise ValueError("La cantidad de fruta debe ser un número positivo.")

    indice_calidad = (kg_pulpa / kg_fruta) * 100
    return float(indice_calidad)