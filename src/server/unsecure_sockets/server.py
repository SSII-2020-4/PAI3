import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 9992))

server_socket.listen(5)

while True:

    (clientsocket, address) = server_socket.accept()
    print("Nueva conexion establecida", address)

    peticion = clientsocket.recv(1024)
    print(peticion)
    clientsocket.close()
