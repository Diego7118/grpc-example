import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc

class GreeterServicer(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("Server listening on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()


#GreeterServicer: Implementa la lógica del servicio (en este caso, responde con un saludo).

#grpc.server: Crea un servidor gRPC.

#add_insecure_port: Escucha en el puerto 50051 (sin cifrado, para desarrollo).

#server.start(): Inicia el servidor.