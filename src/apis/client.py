import socket
import ssl


def cliente(message: tuple):
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        conn = context.wrap_socket(sock)

        conn.connect(('localhost', 8443))

        conn.send(bytearray(message))
        respuesta = conn.recv(1024)
        print(respuesta)
        if (respuesta == b"200"):
            message = "Message sent successfully", 200
        elif (respuesta == b"403"):
            message = "Invalid user and password", 403
        else:
            message = "Internal server error", 500
        conn.close()

        return message

    except KeyboardInterrupt:
        print("\nSocket cliente cerrado")


# if __name__ == "__main__":
#     cliente()
