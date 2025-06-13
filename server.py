from mcp.server.fastmcp import FastMCP
from typing import Dict, List
import json

# Create an MCP server para biblioteca digital
mcp = FastMCP("Biblioteca Digital")

# Base de datos simulada de libros
libros_db: Dict[str, Dict] = {
    "1": {
        "id": "1",
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967,
        "genero": "Realismo mágico",
        "descripcion": "Una obra maestra de la literatura latinoamericana que narra la historia de la familia Buendía."
    },
    "2": {
        "id": "2", 
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año": 1605,
        "genero": "Novela",
        "descripcion": "La historia del ingenioso hidalgo que soñaba con ser caballero andante."
    }
}

# Tool 1: Buscar libros
@mcp.tool()
def buscar_libro(termino: str) -> str:
    """Busca libros por título o autor en la biblioteca."""
    resultados = []
    termino_lower = termino.lower()
    
    for libro in libros_db.values():
        if (termino_lower in libro["titulo"].lower() or 
            termino_lower in libro["autor"].lower()):
            resultados.append(f"📖 {libro['titulo']} - {libro['autor']} ({libro['año']})")
    
    if resultados:
        return f"Libros encontrados:\n" + "\n".join(resultados)
    else:
        return f"No se encontraron libros que coincidan con '{termino}'"

# Tool 2: Agregar nuevo libro
@mcp.tool()
def agregar_libro(titulo: str, autor: str, año: int, genero: str = "Sin clasificar") -> str:
    """Agrega un nuevo libro a la biblioteca."""
    # Generar nuevo ID
    nuevo_id = str(len(libros_db) + 1)
    
    nuevo_libro = {
        "id": nuevo_id,
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "genero": genero,
        "descripcion": f"Libro agregado por el usuario: {titulo} de {autor}"
    }
    
    libros_db[nuevo_id] = nuevo_libro
    
    return f"✅ Libro agregado exitosamente:\n📖 {titulo} - {autor} ({año})\nID: {nuevo_id}"

# Resource: Información detallada de libros
@mcp.resource("biblioteca://libro/{libro_id}")
def informacion_libro(libro_id: str) -> str:
    """Proporciona información detallada de un libro específico."""
    if libro_id in libros_db:
        libro = libros_db[libro_id]
        return json.dumps({
            "titulo": libro["titulo"],
            "autor": libro["autor"],
            "año": libro["año"],
            "genero": libro["genero"],
            "descripcion": libro["descripcion"],
            "disponible": True
        }, indent=2, ensure_ascii=False)
    else:
        return json.dumps({"error": f"Libro con ID {libro_id} no encontrado"}, 
                         indent=2, ensure_ascii=False)

# Prompt: Generar reseña de libro
@mcp.prompt()
def generar_reseña(libro_id: str) -> str:
    """Genera un prompt para crear una reseña literaria de un libro."""
    if libro_id in libros_db:
        libro = libros_db[libro_id]
        return f"""Eres un crítico literario experto. Escribe una reseña profesional y detallada del libro:

Título: {libro['titulo']}
Autor: {libro['autor']}
Año de publicación: {libro['año']}
Género: {libro['genero']}

Descripción: {libro['descripcion']}

Por favor, incluye en tu reseña:
1. Un análisis del estilo narrativo
2. Los temas principales de la obra
3. El contexto histórico y cultural
4. Tu opinión crítica sobre la relevancia de la obra
5. Una calificación del 1 al 10

Mantén un tono académico pero accesible."""
    else:
        return f"Error: No se puede generar reseña para el libro ID {libro_id} - libro no encontrado."

# Run the server
if __name__ == "__main__":
    mcp.run()
