# 📚 Biblioteca Digital MCP

Un servidor **Model Context Protocol (MCP)** que implementa una biblioteca digital interactiva con funcionalidades para gestionar libros, buscar títulos y generar reseñas literarias.

## 🎯 Características

- **🔍 Búsqueda de libros**: Busca libros por título o autor
- **📖 Agregar libros**: Agrega nuevos libros a la biblioteca
- **📄 Información detallada**: Obtén información completa de cualquier libro
- **✍️ Generación de reseñas**: Genera prompts para crear reseñas literarias profesionales
- **💾 Base de datos en memoria**: Almacena libros con información completa

## 🛠 Prerrequisitos

- **Python 3.12+**
- **uv** (Ultra-fast Python package installer)
- **macOS, Linux o Windows**

## 🚀 Instalación y Configuración

### 1. Instalar uv

Si estás en macOS:
```bash
brew install uv
```

Para otros sistemas operativos, consulta la [documentación oficial de uv](https://docs.astral.sh/uv/).

### 2. Configurar el proyecto

```bash
# Clonar o descargar el proyecto
cd basic-mcp

# Inicializar el proyecto uv (si no está inicializado)
uv init

# Crear entorno virtual
uv venv

# Activar entorno virtual
source .venv/bin/activate

# Instalar dependencias MCP
uv pip install "mcp[cli]"
```

### 3. Ejecutar el servidor

```bash
# Ejecutar en modo desarrollo
mcp dev server.py
```

## 📋 Funcionalidades Disponibles

### 🔧 Tools (Herramientas)

1. **`buscar_libro(termino: str)`**
   - Busca libros por título o autor
   - Ejemplo: `buscar_libro("García Márquez")`

2. **`agregar_libro(titulo: str, autor: str, año: int, genero: str)`**
   - Agrega un nuevo libro a la biblioteca
   - Ejemplo: `agregar_libro("1984", "George Orwell", 1949, "Distopía")`

### 📚 Resources (Recursos)

- **`biblioteca://libro/{libro_id}`**
  - Proporciona información detallada en formato JSON de un libro específico
  - Ejemplo: `biblioteca://libro/1`

### 💭 Prompts

- **`generar_reseña(libro_id: str)`**
  - Genera un prompt profesional para crear reseñas literarias
  - Incluye análisis de estilo, temas, contexto histórico y valoración crítica

## 📊 Base de Datos Inicial

El servidor incluye dos libros precargados:

1. **"Cien años de soledad"** - Gabriel García Márquez (1967)
2. **"Don Quijote de la Mancha"** - Miguel de Cervantes (1605)

## 🏗 Estructura del Proyecto

```
basic-mcp/
├── server.py          # Servidor MCP principal
├── main.py           # Script de entrada básico
├── pyproject.toml    # Configuración del proyecto
├── uv.lock          # Archivo de bloqueo de dependencias
├── README.md        # Documentación del proyecto
├── .gitignore       # Archivos ignorados por Git
├── .python-version  # Versión de Python
└── .venv/          # Entorno virtual (ignorado por Git)
```

## 🔄 Flujo de Trabajo

1. **Iniciar el servidor**: `mcp dev server.py`
2. **Conectar un cliente MCP** compatible
3. **Utilizar las herramientas**:
   - Buscar libros existentes
   - Agregar nuevos títulos
   - Consultar información detallada
   - Generar reseñas literarias

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Puedes:

- Agregar nuevas funcionalidades
- Mejorar la base de datos de libros
- Optimizar las búsquedas
- Expandir los prompts de reseñas

## 📝 Notas Técnicas

- Utiliza **FastMCP** para simplificar la implementación del servidor
- La base de datos es **en memoria**, los datos se pierden al reiniciar
- Compatible con el estándar **Model Context Protocol**
- Diseñado para ser usado con clientes MCP como Claude Desktop

---

*Desarrollado con ❤️ usando Model Context Protocol y uv*
