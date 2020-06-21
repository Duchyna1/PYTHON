import socket

HOST = '192.168.0.38'
PORT = 65432

def send(messange):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(str.encode(messange))

send('Hello')
send('Wait')
send('Hello2')