FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Generar código gRPC
RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/hello.proto

EXPOSE 50051
CMD ["python", "server.py"]