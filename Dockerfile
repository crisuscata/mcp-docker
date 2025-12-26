# Usamos una imagen ligera de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios
COPY requirements.txt .
COPY server.py .

# Instalamos la librería MCP
RUN pip install --no-cache-dir -r requirements.txt

# Comando que se ejecuta al levantar el contenedor
# IMPORTANTE: Docker Desktop usa stdio para comunicarse
ENTRYPOINT ["python", "server.py"]