import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adress = ('localhost', 12345)
server_socket.bind(server_adress)

server_socket.listen(1)

client_socket, client_adress = server_socket.accept()
try:
    print('connect ', client_adress)

    while True:
        data = client_socket.recv(1024)
        if data:
            print(f"received, {data.decode('utf-8')}")
            client_socket.send('server'.encode('utf-8'))
        else:
            print('no data', client_adress)
            break
finally:
    client_socket.close()