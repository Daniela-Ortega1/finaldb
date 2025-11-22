"""
Versión manual de las funciones de métricas del proyecto MORITA.
Desarrollado sin ayuda de IA (para comparación con Codeium).
"""

def calcular_rendimiento(kg_fruta, kg_pulpa):
    if kg_fruta <= 0 or kg_pulpa < 0:
        raise ValueError("Entradas no válidas.")

    rendimiento = (kg_pulpa / kg_fruta) * 100
    return rendimiento


def calcular_merma(kg_fruta, kg_pulpa):
    if kg_fruta <= 0 or kg_pulpa < 0:
        raise ValueError("Entradas no válidas.")

    merma = kg_fruta - kg_pulpa
    porcentaje_merma = (merma / kg_fruta) * 100
    return porcentaje_merma


def riesgo_por_rendimiento(rendimiento):
    if rendimiento < 45:
        return "Alto riesgo"
    elif rendimiento >= 45 and rendimiento < 55:
        return "Riesgo medio"
    else:
        return "Bajo riesgo"
