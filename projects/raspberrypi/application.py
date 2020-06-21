import tkinter as tk
import socket
import time
import os

HOST = '127.0.0.1'  # '192.168.0.38'
PORT = 65432


def send(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(str.encode(message))
        time.sleep(0.5)


def push(message):
    os.system('cd /')
    os.system('cd Users/matus/OneDrive/Počítač/GIT/PYTHON')
    os.system('git commit -am "{}"'.format(message))
    os.system('git push')


class Launcher(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.pushButton = tk.Button(self)
        self.pushButton['text'] = "PUSH"
        # self.pushButton['font'] = ("Purisa", 20)
        # self.pushButton['pady'] = 12
        # self.pushButton['width'] = 15
        # self.pushButton['activebackground'] = '#afafaf'
        # self.pushButton['bd'] = 1
        # self.pushButton['highlightcolor'] = '#afafaf'
        # self.pushButton['relief'] = 'solid'
        self.pushButton['command'] = self.pushButtonClick
        self.pushButton.pack()

        self.pushEntry = tk.Entry(self)
        self.pushEntry.pack()

        self.label = tk.Label(self)
        self.label['text'] = 'Ready!'
        self.label.pack()

    def pushButtonClick(self):
        message = self.pushEntry.get()
        if message == '':
            self.label['text'] = 'Invalid push message'
        else:
            push(message)

root = tk.Tk()
root.title('Raspberry pi controller')
root.iconbitmap('C:\\Users\\matus\\OneDrive\\Počítač\\all\\icons\\Raspberry pi.ico')
app = Launcher(master=root)
app.mainloop()
