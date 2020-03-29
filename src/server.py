import multiprocessing
import os
import socket
import ssl


def process_request(sock):
    try:
        sock.send(b"Mensaje recibido")
    finally:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

main_socket.bind(('localhost', 9992))

main_socket.listen(300)

try:
    aux = True
    while aux:
        (client_socket, (client_ip, client_port)) = main_socket.accept()
        print("Conexion aceptada %s:%s. Procesando la peticion..." % (client_ip, client_port))

        conn = ssl.wrap_socket(
            client_socket,
            server_side=True,
            certfile=os.path.join(os.getcwd(), "src", "files", "server.crt"),
            keyfile=os.path.join(os.getcwd(), "src", "files", "server.key"),
            ssl_version=ssl.PROTOCOL_TLS_SERVER
        )

        subprocess = multiprocessing.Process(target=process_request, args=(conn,))
        subprocess.start()

    main_socket.close()
except KeyboardInterrupt:
    print("\n Socket servidor cerrado")
