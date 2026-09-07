# RPG - Arquitectura Modelo - Vista - Controlador (MVC) en Python con Flask

Implementación bilingüe del proyecto **RPG** utilizando **Python 3**, el microframework **Flask** y el motor de plantillas **Jinja2**, siguiendo estrictamente la arquitectura **Modelo - Vista - Controlador (MVC)** y el renderizado desde el servidor (Server-Side Rendering).

---

## 🏛️ Estructura del Proyecto

```text
rpg_flask/
├── app.py                          # Punto de entrada principal de la aplicación Flask
├── requirements.txt                # Dependencia de Flask
├── .gitignore                      # Filtro para entornos virtuales y bytecode
├── models/                         # CAPA MODELO
│   ├── __init__.py
│   └── personaje.py                # Clase Personaje y lista en memoria (list)
├── controllers/                    # CAPA CONTROLADOR
│   ├── __init__.py
│   └── personaje_controller.py     # Manejo de rutas GET y POST, lectura de formulario y renderizado
└── templates/                      # CAPA VISTA
    └── index.html                  # Plantilla HTML con formulario y tabla dinámica en Jinja2
```

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Crear y activar entorno virtual (Recomendado)
En PowerShell o Git Bash:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno en Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# O en Git Bash:
# source venv/Scripts/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Iniciar el servidor
```bash
python app.py
```

Abre tu navegador en:
👉 **`http://127.0.0.1:5000/personajes`** (o `http://localhost:5000`)

---

## 📋 Funcionamiento MVC

1. **Ruta `GET /personajes`:**
   El Controlador (`personaje_controller.py`) obtiene la lista de personajes del Modelo y utiliza la función nativa `render_template('index.html', personajes=lista_personajes)` para entregar la vista HTML ya renderizada al navegador.
2. **Ruta `POST /personajes`:**
   El formulario envía los datos mediante el método tradicional HTTP POST. El Controlador lee los valores con `request.form.get(...)`, crea el objeto del Modelo, lo agrega a la lista en memoria y redirige a la lista mediante `redirect(url_for('personajes.obtener_personajes'))`.
