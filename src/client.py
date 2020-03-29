import socket
import ssl

# class SocketCliente:
#     def __init__(self, sock=None):
#         if sock is None:
#             self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         else:
#             self.sock = sock
            
#         self.context = ssl.SSLContext(ssl.PROTOCOL_TLS,
#         ssl.OP_NO_SSLv2,
#         ssl.OP_NO_SSLv3,
#         ssl.OP_NO_SSLv3,
#         ssl.OP_NO_TLSv1,
#         ssl.OP_NO_TLSv1_1,
#         ssl.OP_NO_TLSv1_2
#         )
    
#     def conectar(self, host, port):
#         wrap = self.context.wrap_socket(self.sock)
#         wrap.connect((host,port))
    
#     def enviar(self, msg):
#         total = 0
#         while total < len(msg):
#             enviado = self.sock.send(msg)
#             print(enviado)
#             if enviado == 0:
#                 raise RuntimeError("Conexion perdida con el socket")
#             total = total + enviado

#     def recibir(self):
#         msglen = len(self.sock.recv(1024))
#         trozos = []
#         bytes_rec = 0
#         while bytes_rec < msglen:
#             trozo = self.sock.recv(min(msglen - bytes_rec, 2048))
#             if trozos == '':
#                 raise RuntimeError("Conexion perdida con el socket")
#             trozos.append(trozo)
#             bytes_rec = bytes_rec + len(trozo)
#         return ''.join(trozos)

#     def cerrar(self, wrap):
#         wrap.close()


        
def cliente():
    try:
        aux = True
        while aux:

            context = ssl.SSLContext(ssl.PROTOCOL_TLS,
            ssl.OP_NO_SSLv2,
            ssl.OP_NO_SSLv3,
            ssl.OP_NO_SSLv3,
            ssl.OP_NO_TLSv1,
            ssl.OP_NO_TLSv1_1,
            ssl.OP_NO_TLSv1_2
            ) #TLS 1.3
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            conn = context.wrap_socket(sock)

            conn.connect(('46.234.133.44', 8443))

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

    
