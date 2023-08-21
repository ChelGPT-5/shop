import socket
import telnetlib
from http.server import HTTPServer, BaseHTTPRequestHandler


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_adress = ('localhost', 12345)
client_socket.connect(server_adress)

try:
    while True:
        message = input('enter message -> ')

        print(f'sending {message}')
        client_socket.send(message.encode('utf-8'))
        data = client_socket.recv(1024)
        print('otvet server: ', data.decode('utf-8'))

finally:
    print('close')
    client_socket.close()
