import socket
import ssl
import os 
from dotenv import load_dotenv

from configuration import check_environment

base_path = os.path.join(os.path.dirname(os.getcwd()), "client")
load_dotenv(os.path.join(base_path, ".env"))

# Check configuration and exit if exist errors
config = check_environment()


def cliente(message: tuple):
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        conn = context.wrap_socket(sock)

        conn.connect((os.environ['SEND_TO_IP'], int(os.environ['SEND_TO_PORT'])))

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
