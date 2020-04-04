import json
import multiprocessing
import os
import socket
import ssl

from dotenv import load_dotenv

from src.server.sqlite import Database
from src.server.configuration import check_environment

base_path = os.path.join(os.path.dirname(os.getcwd()), "server")
load_dotenv(os.path.join(base_path, ".env"))

# Check configuration and exit if exist errors
config = check_environment()
db = Database()


def start_server():
    """
    Start socket server
    """
    # Init main socket
    main_socket = configure_main_socket()
    try:
        aux = True
        while aux:
            init_server_socket(main_socket)
    except KeyboardInterrupt:
        print("\n Socket servidor cerrado")
    except ssl.SSLError as e:
        print(e)
        main_socket.close()
        start_server()
    except Exception as e:
        print(e)
        main_socket.close()
        start_server()


def configure_main_socket():
    """
    Configure socket server
    :return: Socket
    """
    host = os.environ["SERVER_IP"]
    port = int(os.environ["SERVER_PORT"])
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    main_socket.bind((host, port))
    main_socket.listen(300)
    return main_socket


def init_server_socket(main_socket):
    (client_socket, (client_ip, client_port)) = main_socket.accept()
    print(
        f"Conexion aceptada {client_ip}: {client_port}. \
        \nProcesando la peticion..."
    )
    certificate_path = os.path.join(base_path, "certificates", "certificate.pem")
    private_path = os.path.join(base_path, "certificates", "key.pem")
    context = ssl.SSLContext(ssl.PROTOCOL_TLS,
                             ssl.OP_NO_SSLv2,
                             ssl.OP_NO_SSLv3,
                             ssl.OP_NO_TLSv1,
                             ssl.OP_NO_TLSv1_1,
                             ssl.OP_NO_TLSv1_2
                             )  # TLS 1.3

    ciphers = 'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:' \
              'TLS_AES_128_GCM_SHA256:TLS_AES_128_CCM_8_SHA256:TLS_AES_128_CCM_SHA256'
    context.set_ciphers(ciphers)

    context.load_cert_chain(
        certificate_path,
        private_path,
        os.environ["CERTIFICATE_PASSWORD"]
    )
    conn = context.wrap_socket(
        client_socket,
        server_side=True
    )

    # Multiprocessing requests to permit load 300 connections
    subprocess = multiprocessing.Process(target=process_request, args=(conn,))
    subprocess.start()


def process_request(sock):
    """
    Process message
    :param sock: Socket ssl
    """
    try:
        if "TLSv1.3" not in sock.cipher()[1]:
            raise Exception("La conexion no es TLSv1.3")

        message = json.loads(sock.recv(1024).decode('ascii'))

        if db.exist_user_and_pass(message["user"], message["password"]):
            sock.send(b"200")
        else:
            sock.send(b"403")

    except Exception as e:
        sock.send(b"500")
        print(e)
    finally:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()


if __name__ == "__main__":
    start_server()
