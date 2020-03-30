import socket
import ssl


def cliente():
    try:
        aux = True
        while aux:

            context = ssl.SSLContext(ssl.PROTOCOL_TLS)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            conn = context.wrap_socket(sock)

            conn.connect(('localhost', 9992))

            input1 = bytes(input("Mensaje: "), 'utf-8')

            if(input1 == b'cierra'):
                raise KeyboardInterrupt

            while(input1 == b''):
                input1 = bytes(input("Mensaje (notblank): "), 'utf-8')

            conn.send(input1)
            respuesta = conn.recv(1024)
            print(respuesta)
            conn.close()

    except KeyboardInterrupt:
        print("\nSocket cliente cerrado")


if __name__ == "__main__":
    cliente()
