"""
Módulo generado con Claude Code.
Simula un analizador de pedidos del sistema MORITA.
"""

def calcular_tiempo_promedio(pedidos):
    """
    Calcula el tiempo promedio (en días) de procesamiento de pedidos.

    Args:
        pedidos (list[dict]): Lista de pedidos, cada uno con 'dias_proceso'.

    Returns:
        float: Promedio en días.
    """
    if not pedidos:
        return 0
    
    total = sum(p["dias_proceso"] for p in pedidos)
    return round(total / len(pedidos), 2)


def clasificar_prioridad(pedido):
    """
    Determina la prioridad de un pedido según su cantidad.

    Args:
        pedido (dict): Debe contener 'cantidad_kg'.

    Returns:
        str: Nivel de prioridad.
    """
    kg = pedido.get("cantidad_kg", 0)

    if kg >= 200:
        return "Alta"
    elif kg >= 100:
        return "Media"
    else:
        return "Baja"
