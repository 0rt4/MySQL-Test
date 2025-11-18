# MySQL-Test: Complete CRUD User Management System

This is my first Python project implementing a **full CRUD (Create, Read, Update, Delete) application** with an interactive CLI interface for managing user data in a MySQL database.

The goal is to provide a robust, user-friendly tool for complete user data management with database persistence.

## Technologies
- Python 3.x
- mysql-connector-python (imported in code as `mysql.connector`)
- pydantic (for data validation)
- MySQL Server

## Features: CRUD Operations

### 1. **Create (INSERT)**
- Add new users to the database via interactive form
- Validates user data using Pydantic models
- Auto-generates creation timestamp for each user
- Function: `InsertUser()` in `Backend_SQL/SQLController.py`

### 2. **Read (SELECT)**
- **View all users**: Fetch and display complete user list with all attributes
  - Function: `ShowAllUsers()`
- **Search by name**: Find a specific user by their name
  - Function: `SearchByName(nombre: str)`
- **Search by ID**: Retrieve user details using their unique ID
  - Function: `SearchByID(id: int)`

### 3. **Update (UPDATE)**
- Modify existing user information (name, age, birth date)
- Preserves original creation timestamp
- Requires user ID and new data to proceed
- Function: `UpdateUser(id_usuario: int, usuario: Usuario)`

### 4. **Delete (DELETE)**
- Remove users from the database permanently
- Includes confirmation prompt before deletion
- Function: `DeleteUser(id)`

## Project Structure

The project is organized to separate concerns:

- **`RunApp.py`** — Entry point that launches the application.
- **`CLI.py`** — Main menu and CLI logic for user interaction.
- **`Backend_SQL/SQLController.py`** — Core database functions: `ConnectToBD()`, `InsertUser()`, `ShowAllUsers()`, `SearchByName()`, `SearchByID()`, `UpdateUser()`, `DeleteUser()`.
- **`Backend_SQL/Forms.py`** — Interactive forms for each CRUD operation: `FormINSERT()`, `FormSHOWALL()`, `FormSEARCHBYNAME()`, `FormUPDATE()`, `FormDELETE()`.

## Key Improvements Made

- ✅ Renamed functions for clarity: `ConectarDB()` → `ConnectToBD()`, `InsertarUser()` → `InsertUser()`
- ✅ Implemented complete CRUD operations with dedicated functions for each operation
- ✅ Created `Backend_SQL/Forms.py` to separate form logic from database logic
- ✅ Added a **main menu system** with a beautiful CLI interface
- ✅ Implemented **search functionality** (by name and by ID)
- ✅ Added **update capability** to modify existing user records
- ✅ Integrated **delete operations** with confirmation prompts for safety
- ✅ Improved error handling and user feedback throughout the application
- ✅ Used `dictionary=True` cursor mode for easier data manipulation and display

## How to run

1. Make sure you have Python 3 installed.
2. Install the required dependencies:

```bash
pip install mysql-connector-python pydantic
```

3. Configure the database connection in `Backend_SQL/SQLController.py` if needed:
   - By default, `ConnectToBD()` uses a Unix socket at `.mysql/mysql.sock` and connects as `root` to the `Users` database.
   - For a standard MySQL setup, modify the connection parameters:
     ```python
     return mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         user='root',
         password='your_password',
         database='Users'
     )
     ```

4. Run the application from the project root:

```bash
python RunApp.py
```

5. Follow the menu to perform CRUD operations:
   - **Option 1**: Create a new user
   - **Option 2**: View all users
   - **Option 3**: Search user by name
   - **Option 4**: Update user information
   - **Option 5**: Delete a user
   - **Option 6**: Exit

## Notes and recommendations
- **Data Validation**: The project uses `pydantic` for the `Usuario` model to ensure data integrity. Check the model in `Backend_SQL/SQLController.py`.
- **Security**: Never store database credentials in code for production. Use environment variables or a `.env` file with `python-dotenv`.
- **Connection Method**: The project currently uses a Unix socket. If your MySQL setup uses TCP, update the connection parameters in `ConnectToBD()`.
- **Error Handling**: The application includes try-except blocks to catch and display errors gracefully.
- **User Experience**: A clean menu-driven CLI with proper input validation and confirmation prompts for destructive operations (delete).

## Possible improvements (next steps)
- Add input validation to prevent SQL injection (beyond parameterized queries).
- Implement pagination for viewing large user lists.
- Add export functionality (CSV, JSON) for user data.
- Create a `.env` file for configuration and use `python-dotenv` to load it safely.
- Add unit tests for database functions.
- Implement role-based access control (admin vs user).
- Add a `requirements.txt` or `pyproject.toml` for dependency management.
- Consider adding a simple web interface using Flask or FastAPI in the future.

---

Contact: Ortal.Christopher@outlook.com

---

# MySQL-Test: Sistema Completo de Gestión de Usuarios con CRUD

Este es mi primer proyecto en Python implementando una **aplicación completa de CRUD (Crear, Leer, Actualizar, Eliminar)** con una interfaz CLI interactiva para gestionar datos de usuarios en una base de datos MySQL.

El objetivo es proporcionar una herramienta robusta y amigable para la gestión completa de datos de usuarios con persistencia en base de datos.

## Características: Operaciones CRUD

### 1. **Crear (INSERT)**
- Añade nuevos usuarios a la base de datos mediante un formulario interactivo
- Valida los datos del usuario usando modelos Pydantic
- Auto-genera marca de tiempo de creación para cada usuario
- Función: `InsertUser()` en `Backend_SQL/SQLController.py`

### 2. **Leer (SELECT)**
- **Ver todos los usuarios**: Obtiene y muestra la lista completa de usuarios con todos sus atributos
  - Función: `ShowAllUsers()`
- **Buscar por nombre**: Encuentra un usuario específico por su nombre
  - Función: `SearchByName(nombre: str)`
- **Buscar por ID**: Recupera los detalles del usuario usando su ID único
  - Función: `SearchByID(id: int)`

### 3. **Actualizar (UPDATE)**
- Modifica información existente del usuario (nombre, edad, fecha de nacimiento)
- Preserva la marca de tiempo de creación original
- Requiere el ID del usuario y los nuevos datos
- Función: `UpdateUser(id_usuario: int, usuario: Usuario)`

### 4. **Eliminar (DELETE)**
- Elimina usuarios de la base de datos de forma permanente
- Incluye un mensaje de confirmación antes de la eliminación
- Función: `DeleteUser(id)`

## Estructura del Proyecto

El proyecto está organizado para separar responsabilidades:

- **`RunApp.py`** — Punto de entrada que lanza la aplicación.
- **`CLI.py`** — Menú principal y lógica de CLI para interacción con el usuario.
- **`Backend_SQL/SQLController.py`** — Funciones centrales de base de datos: `ConnectToBD()`, `InsertUser()`, `ShowAllUsers()`, `SearchByName()`, `SearchByID()`, `UpdateUser()`, `DeleteUser()`.
- **`Backend_SQL/Forms.py`** — Formularios interactivos para cada operación CRUD: `FormINSERT()`, `FormSHOWALL()`, `FormSEARCHBYNAME()`, `FormUPDATE()`, `FormDELETE()`.

## Mejoras Clave Realizadas

- ✅ Renombré funciones para mayor claridad: `ConectarDB()` → `ConnectToBD()`, `InsertarUser()` → `InsertUser()`
- ✅ Implementé operaciones CRUD completas con funciones dedicadas para cada operación
- ✅ Creé `Backend_SQL/Forms.py` para separar la lógica de formularios de la lógica de base de datos
- ✅ Añadí un **sistema de menú principal** con una interfaz CLI atractiva
- ✅ Implementé **funcionalidad de búsqueda** (por nombre y por ID)
- ✅ Añadí **capacidad de actualización** para modificar registros de usuario existentes
- ✅ Integré **operaciones de eliminación** con mensajes de confirmación para mayor seguridad
- ✅ Mejoré el manejo de errores y la retroalimentación del usuario en toda la aplicación
- ✅ Usé modo cursor `dictionary=True` para una manipulación y visualización más fácil de datos

## Cómo ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Instala las dependencias necesarias:

```bash
pip install mysql-connector-python pydantic
```

3. Configura la conexión a la base de datos en `Backend_SQL/SQLController.py` si es necesario:
   - Por defecto, `ConnectToBD()` usa un socket Unix en `.mysql/mysql.sock` y se conecta como `root` a la base de datos `Users`.
   - Para una configuración estándar de MySQL, modifica los parámetros de conexión:
     ```python
     return mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         user='root',
         password='tu_contraseña',
         database='Users'
     )
     ```

4. Ejecuta la aplicación desde la raíz del proyecto:

```bash
python RunApp.py
```

5. Sigue el menú para realizar operaciones CRUD:
   - **Opción 1**: Crear un nuevo usuario
   - **Opción 2**: Ver todos los usuarios
   - **Opción 3**: Buscar usuario por nombre
   - **Opción 4**: Actualizar información del usuario
   - **Opción 5**: Eliminar un usuario
   - **Opción 6**: Salir

## Notas y recomendaciones
- **Validación de datos**: El proyecto usa `pydantic` para el modelo `Usuario` para asegurar integridad de datos. Revisa el modelo en `Backend_SQL/SQLController.py`.
- **Seguridad**: Nunca almacenes credenciales de base de datos en el código en producción. Usa variables de entorno o un archivo `.env` con `python-dotenv`.
- **Método de conexión**: El proyecto actualmente usa un socket Unix. Si tu configuración de MySQL usa TCP, actualiza los parámetros de conexión en `ConnectToBD()`.
- **Manejo de errores**: La aplicación incluye bloques try-except para capturar y mostrar errores de forma clara.
- **Experiencia del usuario**: Una CLI impulsada por menús limpios con validación de entrada adecuada y mensajes de confirmación para operaciones destructivas (eliminación).

## Posibles mejoras (próximos pasos)
- Añadir validación de entrada para prevenir inyección SQL (más allá de consultas parametrizadas).
- Implementar paginación para visualizar listas grandes de usuarios.
- Añadir funcionalidad de exportación (CSV, JSON) para datos de usuarios.
- Crear un archivo `.env` para configuración y usar `python-dotenv` para cargarlo de forma segura.
- Añadir pruebas unitarias para funciones de base de datos.
- Implementar control de acceso basado en roles (admin vs usuario).
- Añadir un `requirements.txt` o `pyproject.toml` para gestión de dependencias.
- Considerar añadir una interfaz web simple usando Flask o FastAPI en el futuro.

---

Contacto: Ortal.Christopher@outlook.com
