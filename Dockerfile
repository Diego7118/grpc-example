# Usa una imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
COPY proto/hello.proto ./proto/
COPY server.py .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Genera código gRPC
RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/hello.proto

# Puerto expuesto (gRPC usa 50051 por defecto)
EXPOSE 50051

# Comando para iniciar el servidor
CMD ["python", "server.py"]