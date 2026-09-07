"""
PUNTO DE ENTRADA (app.py)
Inicializa la aplicación Flask y registra los Blueprints del Controlador.
"""

from flask import Flask
from controllers.personaje_controller import personaje_bp

def create_app():
    app = Flask(__name__)
    
    # Registra las rutas del Controlador
    app.register_blueprint(personaje_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    print("==================================================")
    print(" 🐍 Servidor Flask RPG en ejecución:")
    print(" 🌐 Abrir en navegador: http://127.0.0.1:5000/personajes")
    print("==================================================")
    app.run(debug=True, port=5000)
