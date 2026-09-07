"""
MODELO (models/personaje.py)
Define la entidad Personaje y mantiene la estructura en memoria (list).
"""

class Personaje:
    def __init__(self, nombre: str, clase: str, nivel: int, vida: int = 100):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.vida = vida

    def __repr__(self):
        return f"<Personaje {self.nombre} ({self.clase}) Nivel {self.nivel}>"


# Estructura en memoria solicitada (equivalente al ArrayList en Java)
lista_personajes = [
    Personaje("Arturo", "Guerrero", 5, 120),
    Personaje("Merlín", "Mago", 8, 80),
    Personaje("Robin", "Arquero", 4, 95)
]
