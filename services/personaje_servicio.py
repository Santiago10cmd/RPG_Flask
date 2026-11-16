def validar_personaje(nombre: str, nivel: int) -> bool:
    """Valida que el nombre no esté vacío y que el nivel esté entre 1 y 100."""
    nombre_limpio = (nombre or '').strip()

    if not nombre_limpio:
        return False

    try:
        nivel_int = int(nivel)
    except (TypeError, ValueError):
        return False

    return 1 <= nivel_int <= 100