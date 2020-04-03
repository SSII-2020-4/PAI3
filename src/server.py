import multiprocessing
import os
import socket
import ssl


def process_request(sock):
    try:
        print(sock.recv(1024))
        sock.send(b"200")
    finally:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()


main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

main_socket.bind(('localhost', 9992))

main_socket.listen(300)

certificate_path = os.path.join(os.path.dirname(os.getcwd()),"certificates", "certificate.pem")
private_path = os.path.join(os.path.dirname(os.getcwd()),"certificates", "key.pem")
certificate_password = "grupo4"
try:
    aux = True
    while aux:
        (client_socket, (client_ip, client_port)) = main_socket.accept()
        print("Conexion aceptada %s:%s. Procesando la peticion..." % (client_ip, client_port))

        context = ssl.SSLContext(ssl.PROTOCOL_TLS,
                                     ssl.OP_NO_SSLv2,
                                     ssl.OP_NO_SSLv3,
                                     ssl.OP_NO_TLSv1,
                                     ssl.OP_NO_TLSv1_1,
                                     ssl.OP_NO_TLSv1_2
                                     )  # TLS 1.3

        ciphers = 'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_AES_128_CCM_8_SHA256:TLS_AES_128_CCM_SHA256'
        context.set_ciphers(ciphers)

        context.load_cert_chain(certificate_path, private_path, certificate_password)

        conn = context.wrap_socket(
            client_socket,
            server_side=True
        )

        subprocess = multiprocessing.Process(
            target=process_request, args=(conn,))
        subprocess.start()

    main_socket.close()
except KeyboardInterrupt:
    print("\n Socket servidor cerrado")
