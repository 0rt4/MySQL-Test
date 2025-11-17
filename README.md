# MySQL-Test (English)

This is my first Python project for creating, managing, and inserting data into a MySQL database.

The goal of the project is to provide a small CLI tool that captures user information and stores it in a MySQL database.

## Technologies
- Python 3.x
- mysql-connector-python (imported in code as `mysql.connector`)
- pydantic (for data validation)
- MySQL Server

## Key files
- `RunApp.py` — application entry point that runs the CLI.
- `CLI.py` — functions for capturing input from the terminal and sending it to the controller.
- `Backend_SQL/SQLController.py` — database helper functions: `ConectarDB()` and `InsertarUser()`.

## How to run
1. Make sure you have Python 3 installed.
2. Install the required dependencies:

```bash
pip install mysql-connector-python pydantic
```

3. Configure the database connection if needed. By default, `ConectarDB()` in `Backend_SQL/SQLController.py` uses a specific `unix_socket` and connects as user `root` to the `Users` database.

- If your MySQL uses a different socket or you prefer a host/port connection, edit `ConectarDB()` and update the parameters (`host`, `port`, `user`, `password`, `database`, or `unix_socket`).

4. Run the application from the project root:

```bash
python RunApp.py
```

Follow the on-screen prompts to add users.

## Notes and recommendations
- Validation: the project uses `pydantic` for the `Usuario` model; check types in `Backend_SQL/SQLController.py`.
- Security: do not store credentials in code for production. Use environment variables or a configuration file excluded from version control.
- MySQL socket: the project currently points to a local socket at `.mysql/mysql.sock`. If you do not use sockets, switch to `host='127.0.0.1'`, `port=3306`, and add `password`.

## Possible improvements (next steps)
- Add more robust error handling and retry logic for connections and transactions.
- Extract database configuration into a `.env` file and use `python-dotenv` to load it.
- Add unit tests and a `requirements.txt` for reproducibility.

---

Contact: Ortal.Christopher@outlook.com

---

# MySQL-Test (Español)

Este es mi primer proyecto en Python para crear, gestionar e insertar datos en una base de datos MySQL.

El objetivo del proyecto es ofrecer una pequeña herramienta CLI que permita capturar información de usuarios y almacenarla en una base de datos MySQL.

## Tecnologías usadas
- Python 3.x
- mysql-connector-python (importado en el código como `mysql.connector`)
- pydantic (para validación de datos)
- MySQL Server

## Archivos clave
- `RunApp.py` — punto de entrada de la aplicación que ejecuta la CLI.
- `CLI.py` — funciones para capturar la entrada desde la terminal y enviarla al controlador.
- `Backend_SQL/SQLController.py` — funciones auxiliares para la base de datos: `ConectarDB()` y `InsertarUser()`.

## Cómo ejecutar
1. Asegúrate de tener Python 3 instalado.
2. Instala las dependencias necesarias:

```bash
pip install mysql-connector-python pydantic
```

3. Configura la conexión a la base de datos si es necesario. Por defecto, `ConectarDB()` en `Backend_SQL/SQLController.py` usa un `unix_socket` específico y se conecta como el usuario `root` a la base `Users`.

- Si tu MySQL usa un socket diferente o prefieres conexión por host/puerto, edita `ConectarDB()` y actualiza los parámetros (`host`, `port`, `user`, `password`, `database` o `unix_socket`).

4. Ejecuta la aplicación desde la raíz del proyecto:

```bash
python RunApp.py
```

Sigue las indicaciones en pantalla para agregar usuarios.

## Notas y recomendaciones
- Validación: el proyecto usa `pydantic` para el modelo `Usuario`; revisa los tipos en `Backend_SQL/SQLController.py`.
- Seguridad: no almacenes credenciales en el código en producción. Usa variables de entorno o un archivo de configuración excluido del control de versiones.
- Socket MySQL: el proyecto apunta actualmente a un socket local en `.mysql/mysql.sock`. Si no usas sockets, cambia a `host='127.0.0.1'`, `port=3306` y añade `password`.

## Posibles mejoras (próximos pasos)
- Añadir manejo de errores y reintentos más robustos para conexiones y transacciones.
- Extraer la configuración de la base de datos a un archivo `.env` y usar `python-dotenv`.
- Añadir pruebas unitarias y un `requirements.txt` para reproducibilidad.

---

Contacto: Ortal.Christopher@outlook.com
