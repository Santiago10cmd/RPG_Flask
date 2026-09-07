"""
CONTROLADOR (controllers/personaje_controller.py)
Maneja las rutas GET /personajes y POST /personajes.
Es el intermediario entre la Vista (HTML con Jinja2) y el Modelo (personaje.py).
"""

from flask import Blueprint, render_template, request, redirect, url_for
from models.personaje import Personaje, lista_personajes

personaje_bp = Blueprint('personajes', __name__)

@personaje_bp.route('/', methods=['GET'])
def inicio():
    """Redirige la raíz automáticamente al listado de personajes."""
    return redirect(url_for('personajes.obtener_personajes'))


@personaje_bp.route('/personajes', methods=['GET'])
def obtener_personajes():
    """
    RUTA GET /personajes (Server-Side Rendering)
    Solicita la lista de personajes al Modelo y la envía a la plantilla
    index.html utilizando la función nativa render_template de Flask.
    """
    return render_template('index.html', personajes=lista_personajes)


@personaje_bp.route('/personajes', methods=['POST'])
def crear_personaje():
    """
    RUTA POST /personajes (Formulario tradicional)
    Lee campo por campo con request.form.get, crea la instancia del Modelo
    y aplica el patrón Post/Redirect/Get para recargar la vista actualizada.
    """
    try:
        nombre = request.form.get('nombre', '').strip()
        clase = request.form.get('clase', 'Guerrero')
        nivel = int(request.form.get('nivel', 1))
        vida = int(request.form.get('vida', 100))

        # Validación básica en el controlador / modelo
        if not nombre:
            return "Error: El nombre no puede estar vacío.", 400
        if nivel < 1:
            return "Error: El nivel debe ser mayor o igual a 1.", 400

        # Crear y almacenar en la lista en memoria
        nuevo_personaje = Personaje(nombre, clase, nivel, vida)
        lista_personajes.append(nuevo_personaje)

        # Post/Redirect/Get: Redirige a la ruta GET /personajes
        return redirect(url_for('personajes.obtener_personajes'))

    except ValueError:
        return "Error: El nivel y la vida deben ser números válidos.", 400
