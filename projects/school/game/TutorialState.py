import tkinter as tk
from Settings import *

tutorialSettings = settings['states']['tutorial']

class TutorialState(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self)
        self.canvas['width'] =  tutorialSettings['canvas']['width']
        self.canvas['height'] = tutorialSettings['canvas']['height']
        self.canvas['bg'] =     tutorialSettings['canvas']['bg']
        self.canvas.pack()

        self.text = self.canvas.create_text(tutorialSettings['canvas']['width']//2,
                                            tutorialSettings['canvas']['height']//2,
                                            text=tutorialSettings['text']['text'],
                                            fill=tutorialSettings['text']['color'],
                                            font=tutorialSettings['text']['font'])
        self.canvas.update()

        self.backButton = tk.Button(self)
        self.backButton['text'] =               tutorialSettings['backButton']['text']
        self.on['font'] =               tutorialSettings['backButton']['font']
        self.backButton['pabackButtdy'] =               tutorialSettings['backButton']['pady']
        self.backButton['width'] =              tutorialSettings['backButton']['width']
        self.backButton['activebackground'] =   tutorialSettings['backButton']['activebackground']
        self.backButton['bd'] =                 tutorialSettings['backButton']['bd']
        self.backButton['highlightcolor'] =     tutorialSettings['backButton']['highlightcolor']
        self.backButton['relief'] =             tutorialSettings['backButton']['relief']
        self.backButton['command'] = self.backButtonClick
        self.backButton.pack()

    def backButtonClick(self):
        self.master.destroy()
