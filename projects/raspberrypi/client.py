import socket
import time

HOST = '192.168.0.38'
PORT = 65432

def send(s, messange):
    s.sendall(str.encode(messange))
    time.sleep(0.5)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    send(s, 'Hello')
    send(s, 'Wait')
    send(s, 'Hello2')