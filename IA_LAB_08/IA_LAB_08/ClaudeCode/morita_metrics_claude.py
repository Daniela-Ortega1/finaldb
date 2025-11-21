"""
Módulo de métricas de producción para el proyecto MORITA.

Proporciona funciones para calcular rendimiento, merma y clasificación
de riesgo en la producción de pulpa de mora.
"""

from typing import Optional
from enum import Enum


class NivelRiesgo(Enum):
    """Niveles de riesgo en la producción."""
    ALTO = "ALTO"
    MEDIO = "MEDIO"
    BAJO = "BAJO"


# Constantes de umbrales de riesgo
UMBRAL_RIESGO_ALTO = 0.6
UMBRAL_RIESGO_MEDIO = 0.8


class ErrorValidacion(ValueError):
    """Excepción personalizada para errores de validación."""
    pass


def validar_peso(valor: float, nombre_campo: str) -> None:
    """
    Valida que un peso sea un número positivo válido.
    
    Args:
        valor: El valor a validar.
        nombre_campo: Nombre del campo para mensajes de error descriptivos.
    
    Raises:
        ErrorValidacion: Si el valor no es válido.
    
    Examples:
        >>> validar_peso(10.5, "kg_fruta")
        >>> validar_peso(-5, "kg_pulpa")
        Traceback (most recent call last):
        ...
        ErrorValidacion: kg_pulpa debe ser un número positivo, recibido: -5
    """
    if not isinstance(valor, (int, float)):
        raise ErrorValidacion(
            f"{nombre_campo} debe ser un número, recibido tipo: {type(valor).__name__}"
        )
    
    if valor < 0:
        raise ErrorValidacion(
            f"{nombre_campo} debe ser un número positivo, recibido: {valor}"
        )


def calcular_rendimiento(kg_fruta: float, kg_pulpa: float) -> float:
    """
    Calcula el rendimiento del lote de producción.
    
    El rendimiento se define como la proporción de pulpa obtenida
    respecto a la fruta procesada (kg_pulpa / kg_fruta).
    
    Args:
        kg_fruta: Kilogramos de fruta procesada (debe ser > 0).
        kg_pulpa: Kilogramos de pulpa obtenida (debe ser >= 0).
    
    Returns:
        float: Rendimiento como valor decimal entre 0 y 1.
               Por ejemplo, 0.75 indica 75% de rendimiento.
    
    Raises:
        ErrorValidacion: Si los valores de entrada no son válidos.
        ZeroDivisionError: Si kg_fruta es 0.
    
    Examples:
        >>> calcular_rendimiento(100, 75)
        0.75
        >>> calcular_rendimiento(50, 40)
        0.8
    """
    validar_peso(kg_fruta, "kg_fruta")
    validar_peso(kg_pulpa, "kg_pulpa")
    
    if kg_fruta == 0:
        raise ZeroDivisionError("kg_fruta no puede ser 0 (división por cero)")
    
    if kg_pulpa > kg_fruta:
        raise ErrorValidacion(
            f"kg_pulpa ({kg_pulpa}) no puede ser mayor que kg_fruta ({kg_fruta})"
        )
    
    return kg_pulpa / kg_fruta


def calcular_porcentaje_merma(kg_fruta: float, kg_pulpa: float) -> float:
    """
    Calcula el porcentaje de merma o pérdida en el proceso.
    
    La merma representa el porcentaje de fruta que no se convierte
    en pulpa aprovechable, calculado como (1 - rendimiento) * 100.
    
    Args:
        kg_fruta: Kilogramos de fruta procesada (debe ser > 0).
        kg_pulpa: Kilogramos de pulpa obtenida (debe ser >= 0).
    
    Returns:
        float: Porcentaje de merma (0-100).
               Por ejemplo, 25.0 indica 25% de pérdida.
    
    Raises:
        ErrorValidacion: Si los valores de entrada no son válidos.
    
    Examples:
        >>> calcular_porcentaje_merma(100, 75)
        25.0
        >>> calcular_porcentaje_merma(50, 40)
        20.0
    """
    rendimiento = calcular_rendimiento(kg_fruta, kg_pulpa)
    merma = (1 - rendimiento) * 100
    return merma


def clasificar_riesgo(rendimiento: float) -> NivelRiesgo:
    """
    Clasifica el nivel de riesgo operativo según el rendimiento.
    
    Criterios de clasificación:
    - ALTO: rendimiento < 60% (< 0.6)
    - MEDIO: rendimiento 60-79.99% (0.6 <= r < 0.8)
    - BAJO: rendimiento >= 80% (>= 0.8)
    
    Args:
        rendimiento: Valor de rendimiento entre 0 y 1.
    
    Returns:
        NivelRiesgo: Clasificación del riesgo (ALTO, MEDIO o BAJO).
    
    Raises:
        ErrorValidacion: Si el rendimiento no está entre 0 y 1.
    
    Examples:
        >>> clasificar_riesgo(0.5)
        <NivelRiesgo.ALTO: 'ALTO'>
        >>> clasificar_riesgo(0.75)
        <NivelRiesgo.MEDIO: 'MEDIO'>
        >>> clasificar_riesgo(0.85)
        <NivelRiesgo.BAJO: 'BAJO'>
    """
    if not isinstance(rendimiento, (int, float)):
        raise ErrorValidacion(
            f"rendimiento debe ser un número, recibido tipo: {type(rendimiento).__name__}"
        )
    
    if rendimiento < 0 or rendimiento > 1:
        raise ErrorValidacion(
            f"El rendimiento debe estar entre 0 y 1, recibido: {rendimiento}"
        )
    
    if rendimiento < UMBRAL_RIESGO_ALTO:
        return NivelRiesgo.ALTO
    elif rendimiento < UMBRAL_RIESGO_MEDIO:
        return NivelRiesgo.MEDIO
    return NivelRiesgo.BAJO


def generar_reporte_lote(
    kg_fruta: float, 
    kg_pulpa: float,
    id_lote: Optional[str] = None
) -> dict:
    """
    Genera un reporte completo de métricas para un lote de producción.
    
    Args:
        kg_fruta: Kilogramos de fruta procesada.
        kg_pulpa: Kilogramos de pulpa obtenida.
        id_lote: Identificador opcional del lote.
    
    Returns:
        dict: Diccionario con todas las métricas calculadas:
            - id_lote: Identificador del lote (si se proporcionó)
            - kg_fruta: Kilogramos de fruta
            - kg_pulpa: Kilogramos de pulpa
            - rendimiento: Rendimiento decimal (0-1)
            - rendimiento_porcentaje: Rendimiento como porcentaje
            - merma_porcentaje: Porcentaje de merma
            - nivel_riesgo: Clasificación de riesgo
    
    Examples:
        >>> reporte = generar_reporte_lote(100, 75, "LOTE-001")
        >>> reporte['rendimiento']
        0.75
        >>> reporte['nivel_riesgo']
        <NivelRiesgo.MEDIO: 'MEDIO'>
    """
    rendimiento = calcular_rendimiento(kg_fruta, kg_pulpa)
    merma = calcular_porcentaje_merma(kg_fruta, kg_pulpa)
    riesgo = clasificar_riesgo(rendimiento)
    
    reporte = {
        "kg_fruta": kg_fruta,
        "kg_pulpa": kg_pulpa,
        "rendimiento": round(rendimiento, 4),
        "rendimiento_porcentaje": round(rendimiento * 100, 2),
        "merma_porcentaje": round(merma, 2),
        "nivel_riesgo": riesgo.value
    }
    
    if id_lote:
        reporte["id_lote"] = id_lote
    
    return reporte


def formatear_reporte(reporte: dict) -> str:
    """
    Formatea un reporte de lote como texto legible.
    
    Args:
        reporte: Diccionario generado por generar_reporte_lote.
    
    Returns:
        str: Reporte formateado como texto.
    
    Examples:
        >>> reporte = generar_reporte_lote(100, 75, "LOTE-001")
        >>> print(formatear_reporte(reporte))
        === REPORTE DE PRODUCCIÓN ===
        Lote: LOTE-001
        Fruta procesada: 100.00 kg
        Pulpa obtenida: 75.00 kg
        Rendimiento: 75.00%
        Merma: 25.00%
        Nivel de riesgo: MEDIO
    """
    lineas = ["=== REPORTE DE PRODUCCIÓN ==="]
    
    if "id_lote" in reporte:
        lineas.append(f"Lote: {reporte['id_lote']}")
    
    lineas.extend([
        f"Fruta procesada: {reporte['kg_fruta']:.2f} kg",
        f"Pulpa obtenida: {reporte['kg_pulpa']:.2f} kg",
        f"Rendimiento: {reporte['rendimiento_porcentaje']:.2f}%",
        f"Merma: {reporte['merma_porcentaje']:.2f}%",
        f"Nivel de riesgo: {reporte['nivel_riesgo']}"
    ])
    
    return "\n".join(lineas)


if __name__ == "__main__":
    # Ejemplo de uso
    print("Ejemplo de uso del módulo MORITA Metrics\n")
    
    # Caso 1: Rendimiento alto
    reporte1 = generar_reporte_lote(100, 85, "LOTE-001")
    print(formatear_reporte(reporte1))
    print()
    
    # Caso 2: Rendimiento medio
    reporte2 = generar_reporte_lote(150, 105, "LOTE-002")
    print(formatear_reporte(reporte2))
    print()
    
    # Caso 3: Rendimiento bajo
    reporte3 = generar_reporte_lote(200, 110, "LOTE-003")
    print(formatear_reporte(reporte3))