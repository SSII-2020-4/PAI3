import socket


while True:
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_client.connect(('localhost', 9992))

    input1 = input()
    socket_client.send(bytes(input1, 'utf-8'))
    respuesta = socket_client.recv(1024)

    print(respuesta)
    socket_client.close()