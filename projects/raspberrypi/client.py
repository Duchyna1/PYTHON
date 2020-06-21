import socket
import time

HOST = '127.0.0.1' #'192.168.0.38'
PORT = 65432


def send(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(str.encode(message))
        time.sleep(0.5)


send('Hello')
send('Wait')
send('Hello2')
