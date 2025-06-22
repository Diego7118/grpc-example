import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = hello_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(hello_pb2.HelloRequest(name="World"))
    print("Server response:", response.message)

if __name__ == "__main__":
    run()


#grpc.insecure_channel: Conexión no cifrada al servidor (válido para desarrollo).

#GreeterStub: Cliente que llama al servicio Greeter.

#stub.SayHello: Envía una solicitud y recibe la respuesta.