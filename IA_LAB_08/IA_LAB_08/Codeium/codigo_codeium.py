"""
Código generado con Codeium para el laboratorio 8.
Funciones básicas de métricas de producción del proyecto MORITA.
"""

def calcular_rendimiento(kg_fruta, kg_pulpa):
    """Calcula el rendimiento del lote en porcentaje."""
    if kg_fruta <= 0 or kg_pulpa < 0:
        raise ValueError("Los valores deben ser positivos.")
    return (kg_pulpa / kg_fruta) * 100


def calcular_merma(kg_fruta, kg_pulpa):
    """Calcula el porcentaje de merma del proceso."""
    if kg_fruta <= 0 or kg_pulpa < 0:
        raise ValueError("Entradas inválidas.")
    merma = kg_fruta - kg_pulpa
    return (merma / kg_fruta) * 100


def riesgo_por_rendimiento(rendimiento):
    """Clasifica el nivel de riesgo según el rendimiento."""
    if rendimiento < 45:
        return "Alto riesgo"
    elif rendimiento < 55:
        return "Riesgo medio"
    else:
        return "Bajo riesgo"
