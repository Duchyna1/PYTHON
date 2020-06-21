import socket

HOST = '127.0.0.1'  # '192.168.0.38'
PORT = 65432


def pull():
    print('pull')
    # os.system('cd Desktop/GIT/PYTHON')
    # os.system('git fetch --all')
    # os.system('git reset --hard origin/master')
    # os.system('git pull origin master')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if data:
                print(data.decode("utf-8"))
                if data == 'pull':
                    pull()
                    conn.sendall(b'done')
                s.listen()
                conn, addr = s.accept()
