import tkinter as tk

class Button:
    def __init__(self, canvas, x, y, width, height, border, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        self.canvas = canvas
        self.color = color
        self.text = text
        self.button = self.canvas.create_rectangle(x, y, x+width, y+height, fill=self.color, width=border)
        self.text = self.canvas.create_text(x+width//2, y+height//2, text=self.text)

    def remove(self):
        self.canvas.delete(self.button)
        self.canvas.delete(self.text)
