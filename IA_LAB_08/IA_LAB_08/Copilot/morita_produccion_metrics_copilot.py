"""
Módulo de métricas de producción para el sistema MORITA.

Este módulo calcula:
- Rendimiento por lote (kg de pulpa / kg de fruta fresca).
- Porcentaje de merma.
- Clasificación de riesgo de producción según el rendimiento.

Este archivo fue creado para el Laboratorio 8 de IA (GitHub Copilot).
"""
# Implementar una función en Python que calcule el rendimiento de un lote de producción
# de pulpa de mora. La función se debe llamar calcular_rendimiento_lote y recibir dos
# parámetros: kg_fruta (float) y kg_pulpa (float). Debe retornar el rendimiento como
# un número flotante entre 0 y 1. Si los parámetros son inválidos (cero o negativos),
# debe lanzar un ValueError con un mensaje descriptivo.

def calcular_rendimiento_lote(kg_fruta: float, kg_pulpa: float) -> float:
    if kg_fruta <= 0 or kg_pulpa <= 0:
        raise ValueError("Los valores de kg_fruta y kg_pulpa deben ser mayores que cero.")
    return kg_pulpa / kg_fruta


# Implementar la función calcular_porcentaje_merma(kg_fruta, kg_pulpa) que retorne
# el porcentaje de merma como un valor entre 0 y 100. Debe reutilizar la función
# calcular_rendimiento_lote y documentar el comportamiento con un docstring.
def calcular_porcentaje_merma(kg_fruta: float, kg_pulpa: float) -> float:
    """
    Calcula el porcentaje de merma en la producción de pulpa de mora.

    El porcentaje de merma se calcula como:
    Merma (%) = (1 - Rendimiento) * 100

    Parámetros:
    kg_fruta (float): Cantidad de fruta fresca en kilogramos.
    kg_pulpa (float): Cantidad de pulpa producida en kilogramos.

    Retorna:
    float: Porcentaje de merma entre 0 y 100.

    Lanza:
    ValueError: Si los parámetros son inválidos (cero o negativos).
    """
    rendimiento = calcular_rendimiento_lote(kg_fruta, kg_pulpa)
    porcentaje_merma = (1 - rendimiento) * 100
    return porcentaje_merma             

# Implementar la función clasificar_riesgo_produccion(rendimiento) que clasifique
# el riesgo del lote según el rendimiento:
# - "ALTO" si rendimiento < 0.6
# - "MEDIO" si 0.6 <= rendimiento < 0.8
# - "BAJO" si rendimiento >= 0.8
# La función debe validar que rendimiento esté entre 0 y 1.
def clasificar_riesgo_produccion(rendimiento: float) -> str:
    if rendimiento < 0 or rendimiento > 1:
        raise ValueError("El rendimiento debe estar entre 0 y 1.")
    if rendimiento < 0.6:
        return "ALTO"
    elif rendimiento < 0.8:
        return "MEDIO"
    else:
        return "BAJO"       
