import tkinter as tk
from Settings import *
from GameState import GameState
from TutorialState import TutorialState

menuSettings = settings['states']['menu']

class MenuState(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.playButton = tk.Button(self)
        self.playButton['text'] =               menuSettings['buttons']['play']['text']
        self.playButton['font'] =               menuSettings['buttons']['play']['font']
        self.playButton['pady'] =               menuSettings['buttons']['play']['pady']
        self.playButton['width'] =              menuSettings['buttons']['play']['width']
        self.playButton['activebackground'] =   menuSettings['buttons']['play']['activebackground']
        self.playButton['bd'] =                 menuSettings['buttons']['play']['bd']
        self.playButton['highlightcolor'] =     menuSettings['buttons']['play']['highlightcolor']
        self.playButton['relief'] =             menuSettings['buttons']['play']['relief']
        self.playButton['command'] = self.playButtonClick
        self.playButton.pack()

        self.tutorialButton = tk.Button(self)
        self.tutorialButton['text'] =               menuSettings['buttons']['tutorial']['text']
        self.tutorialButton['font'] =               menuSettings['buttons']['tutorial']['font']
        self.tutorialButton['pady'] =               menuSettings['buttons']['tutorial']['pady']
        self.tutorialButton['width'] =              menuSettings['buttons']['tutorial']['width']
        self.tutorialButton['activebackground'] =   menuSettings['buttons']['tutorial']['activebackground']
        self.tutorialButton['bd'] =                 menuSettings['buttons']['tutorial']['bd']
        self.tutorialButton['highlightcolor'] =     menuSettings['buttons']['tutorial']['highlightcolor']
        self.tutorialButton['relief'] =             menuSettings['buttons']['tutorial']['relief']
        self.tutorialButton['command'] = self.tutorialButtonClick
        self.tutorialButton.pack()

        self.quitButton = tk.Button(self)
        self.quitButton['text'] =               menuSettings['buttons']['quit']['text']
        self.quitButton['font'] =               menuSettings['buttons']['quit']['font']
        self.quitButton['pady'] =               menuSettings['buttons']['quit']['pady']
        self.quitButton['width'] =              menuSettings['buttons']['quit']['width']
        self.quitButton['activebackground'] =   menuSettings['buttons']['quit']['activebackground']
        self.quitButton['bd'] =                 menuSettings['buttons']['quit']['bd']
        self.quitButton['highlightcolor'] =     menuSettings['buttons']['quit']['highlightcolor']
        self.quitButton['relief'] =             menuSettings['buttons']['quit']['relief']
        self.quitButton['command'] = self.quitButtonClick
        self.quitButton.pack()

    def playButtonClick(self):
        root = tk.Tk()
        root.title(settings['states']['game']['window']['title'])
        GameState(master=root)
        self.master.destroy()

    def tutorialButtonClick(self):
        root = tk.Tk()
        root.title(settings['states']['tutorial']['window']['title'])
        TutorialState(master=root)

    def quitButtonClick(self):
        self.master.destroy()
