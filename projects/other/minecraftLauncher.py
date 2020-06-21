import tkinter as tk
import os


class Launcher(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.modButton = tk.Button(self)
        self.modButton['text'] = "Modded"
        self.modButton['font'] = ("Purisa", 20)
        self.modButton['pady'] = 12
        self.modButton['width'] = 15
        self.modButton['activebackground'] = '#afafaf'
        self.modButton['bd'] = 1
        self.modButton['highlightcolor'] = '#afafaf'
        self.modButton['relief'] = 'solid'
        self.modButton['command'] = self.modButtonClick
        self.modButton.pack()

        self.vanillaButton = tk.Button(self)
        self.vanillaButton['text'] = "Vanilla"
        self.vanillaButton['font'] = ("Purisa", 20)
        self.vanillaButton['pady'] = 12
        self.vanillaButton['width'] = 15
        self.vanillaButton['activebackground'] = '#afafaf'
        self.vanillaButton['bd'] = 1
        self.vanillaButton['highlightcolor'] = '#afafaf'
        self.vanillaButton['relief'] = 'solid'
        self.vanillaButton['command'] = self.vanillaButtonClick
        self.vanillaButton.pack()

        self.quitButton = tk.Button(self)
        self.quitButton['text'] = "QUIT"
        self.quitButton['font'] = ("Purisa", 20)
        self.quitButton['pady'] = 12
        self.quitButton['width'] = 15
        self.quitButton['activebackground'] = '#afafaf'
        self.quitButton['bd'] = 1
        self.quitButton['highlightcolor'] = '#afafaf'
        self.quitButton['relief'] = 'solid'
        self.quitButton['command'] = self.quitButtonClick
        self.quitButton.pack()

    def modButtonClick(self):
        self.master.destroy()
        os.system('picomc instance instancename launch')

    def vanillaButtonClick(self):
        self.master.destroy()
        os.system('picomc instance mod launch')

    def quitButtonClick(self):
        self.master.destroy()


root = tk.Tk()
root.title('Minecraft Launcher')
root.iconbitmap('C:\\Users\\matus\\OneDrive\\Počítač\\all\\icons\\MineCraft.ico')
app = Launcher(master=root)
app.mainloop()
