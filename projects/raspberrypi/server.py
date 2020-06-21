import socket

HOST = '192.168.0.38'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by ', addr)
        while True:
            data = conn.recv(1024)
            if data:
                print(data.decode("utf-8"))
            else:
                s.listen()
                conn, addr = s.accept()