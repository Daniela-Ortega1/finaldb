def calcular_rendimiento_lote(kg_fruta: float, kg_pulpa: float) -> float:
    """Versión manual sin ayuda de GitHub Copilot."""
    if kg_fruta <= 0 or kg_pulpa < 0:
        raise ValueError("Parámetros inválidos")
    return kg_pulpa / kg_fruta


def calcular_porcentaje_merma(kg_fruta: float, kg_pulpa: float) -> float:
    """Versión manual sin ayuda de GitHub Copilot."""
    rendimiento = calcular_rendimiento_lote(kg_fruta, kg_pulpa)
    merma = 1 - rendimiento
    return merma * 100


def clasificar_riesgo_produccion(rendimiento: float) -> str:
    """Versión manual sin ayuda de GitHub Copilot."""
    if rendimiento < 0 or rendimiento > 1:
        raise ValueError("El rendimiento debe estar entre 0 y 1")
    if rendimiento < 0.6:
        return "ALTO"
    elif rendimiento < 0.8:
        return "MEDIO"
    return "BAJO"