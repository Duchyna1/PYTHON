import tkinter as tk
import socket
import time
import os

HOST = '127.0.0.1'  # '192.168.0.38'
PORT = 65432


def send(s, message):
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
        self.pushEntry = tk.Entry(self)
        self.pushEntry.pack()

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

        self.pullButton = tk.Button(self)
        self.pullButton['text'] = "PULL"
        self.pullButton['command'] = self.pullButtonClick
        self.pullButton.pack()

        self.text = tk.StringVar()
        self.label = tk.Label(self, textvariable=self.text)
        self.text.set('Ready!')
        self.label.pack()

        self.quitButton = tk.Button(self)
        self.quitButton['text'] = "QUIT"
        self.quitButton['command'] = self.quitButtonClick
        self.quitButton.pack()

    def pushButtonClick(self):
        self.text.set('Wait...')
        self.update()
        message = self.pushEntry.get()
        if message == '':
            self.text.set('Invalid push message')
            self.update()
        else:
            push(message)
            self.text.set('DONE!')
            self.update()

    def pullButtonClick(self):
        self.text.set('Wait...')
        self.update()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            send(s, 'pull')
            data = s.recv(1024).decode("utf-8")
            if data == 'done':
                self.text.set('DONE!')
                self.update()

    def quitButtonClick(self):
        self.master.destroy()

root = tk.Tk()
root.title('Raspberry pi controller')
root.iconbitmap('C:\\Users\\matus\\OneDrive\\Počítač\\all\\icons\\Raspberry pi.ico')
app = Launcher(master=root)
app.mainloop()
