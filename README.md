# 🚀 MCP Starter Kit: Tu primer Agente con Docker y Python

Este repositorio contiene el código fuente oficial del video de **Joaquin Ruiz Lite**: ["Si no usas MCP, tu IA está incompleta (Docker Toolkit + Python)"](https://youtu.be/fsyJK6KngXk?si=2MyCdO6WNCliIp9b).

Aquí encontrarás un ejemplo práctico y minimalista de cómo crear un **Servidor MCP (Model Context Protocol)** desde cero, dockerizarlo y conectarlo a **Claude Desktop**.

## 📺 Sobre el Proyecto
El objetivo de este proyecto es demostrar que no necesitas ser un experto en LLMs para dotar a la IA de herramientas.
En este ejemplo creamos un **Dado de 12 caras (D12)**. Si entiendes este código, entiendes la base para conectar bases de datos, APIs o scripts de automatización.

## 📂 Estructura del Proyecto

* `server.py`: El código del servidor usando `FastMCP` (Python).
* `Dockerfile`: La receta para empaquetar el servidor de forma aislada.
* `requirements.txt`: Dependencias necesarias.
* `claude_desktop_config.json`: Ejemplo de configuración para tu cliente.

## 🛠️ Requisitos

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y corriendo.
* [Claude Desktop](https://claude.ai/download) (o cualquier cliente compatible con MCP).

## ⚡ Guía de Inicio Rápido

### 1. Clonar el repositorio
```bash
git clone [https://github.com/JoaquinRuiz/mcp-docker-tutorial.git](https://github.com/JoaquinRuiz/mcp-docker-tutorial)
cd mcp-starter-kit
```

### 2. Construir la imagen de Docker
Vamos a crear la imagen de nuestro servidor.

```bash
docker build -t mcp-d12 .
```

### 3. Configurar Claude Desktop
Abre tu archivo de configuración de Claude.

* Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
* Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Añade el siguiente bloque dentro de mcpServers:

```json
{
  "mcpServers": {
    "d12-roller": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "mcp-d12"
      ]
    }
  }
}
```
Nota de Ingeniero: El flag -i es crucial porque MCP utiliza stdio (entrada/salida estándar) para comunicarse con el contenedor.

Version mas completa con el tutorial pasado, y no olvides eliminar procesos de claude y abrir nuevamente

```json
{
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": [
        "mcp",
        "gateway",
        "run"
      ],
      "env": {
        "LOCALAPPDATA": "C:\\Users\\Usuario\\AppData\\Local",
        "ProgramData": "C:\\ProgramData",
        "ProgramFiles": "C:\\Program Files"
      }
    },
    "d12-roller": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "mcp-d12"
      ]
    }
  }
}

### 4. ¡A probar!
Reinicia Claude Desktop. Verás un icono de un enchufe 🔌 o un martillo 🔨 indicando que las herramientas están cargadas. Prueba con el prompt:

> "Tira el dado de 12 caras y si sale más de 6, cuéntame un chiste corto."

## 📚 Aprende más con Jokioki
Si este código te ha servido, profundizar en la lógica detrás de la IA es lo que te diferenciará como ingeniero. Echa un vistazo a mis libros:

- 📖 [Explora la Inteligencia Artificial](https://amzn.eu/d/dSwYhue)
- 💻 [Programar con Inteligencia Artificial](https://amzn.eu/d/eK4f73N)

## 🤝 Contribuir
¿Se te ocurren más herramientas simples para empezar? ¡Haz un Pull Request! Vamos a construir el mejor repo de iniciación a MCP en español.

--- 

Hecho con ☕ y código por [JoaquinRuizLite](https://www.youtube.com/@jokioki?sub_confirmation=1). ¡No olvides suscribirte al canal!