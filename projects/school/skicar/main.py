import tkinter
from tkinter.colorchooser import askcolor

import color
import button
import penStamp

########################################################################################################################
#########################################################################################################################
########################################################################################################################

class Modes:
    DRAWING = 0
    STAMP = 1

class Pen:
    LINE = 0
    CIRCLE = 1
    SQUARE = 2

class Stamp:
    HOUSE = 0
    FLOWER = 1

########################################################################################################################
#########################################################################################################################
########################################################################################################################

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light gray', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'Slategray1', 'Slategray2', 'Slategray3',
          'Slategray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlategray1', 'DarkSlategray2', 'DarkSlategray3', 'DarkSlategray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'grey1', 'grey2', 'grey3', 'grey4', 'grey5', 'grey6', 'grey7', 'grey8', 'grey9', 'grey10',
          'grey11', 'grey12', 'grey13', 'grey14', 'grey15', 'grey16', 'grey17', 'grey18', 'grey19',
          'grey20', 'grey21', 'grey22', 'grey23', 'grey24', 'grey25', 'grey26', 'grey27', 'grey28',
          'grey29', 'grey30', 'grey31', 'grey32', 'grey33', 'grey34', 'grey35', 'grey36', 'grey37',
          'grey38', 'grey39', 'grey40', 'grey42', 'grey43', 'grey44', 'grey45', 'grey46', 'grey47',
          'grey48', 'grey49', 'grey50', 'grey51', 'grey52', 'grey53', 'grey54', 'grey55', 'grey56',
          'grey57', 'grey58', 'grey59', 'grey60', 'grey61', 'grey62', 'grey63', 'grey64', 'grey65',
          'grey66', 'grey67', 'grey68', 'grey69', 'grey70', 'grey71', 'grey72', 'grey73', 'grey74',
          'grey75', 'grey76', 'grey77', 'grey78', 'grey79', 'grey80', 'grey81', 'grey82', 'grey83',
          'grey84', 'grey85', 'grey86', 'grey87', 'grey88', 'grey89', 'grey90', 'grey91', 'grey92',
          'grey93', 'grey94', 'grey95', 'grey97', 'grey98', 'grey99']

canvasHeight, canvasWidth = 600, 700
canvasBG = "white"

canvas = tkinter.Canvas(width=canvasWidth, height=canvasHeight, background=canvasBG)
canvas.pack()

colors = []
colors2 = []
drawings = []

moreColor = button.create(6*40, 20, 40, 40, 0, "gray", "MORE", canvas)
currentColor = button.create(0, 0, canvasWidth, 20, 0, "black", "CURRENT", canvas)
lastColor = button.create(canvasWidth-40, 20, 40, 40, 0, "white", "LAST", canvas)
RGB = button.create(7*40, 20, 40, 40, 0, "light gray", "RGB", canvas)

modeLine = penStamp.create(8*40, 20, 40, 40, 0, canvas, "LINE")
modeCircle = penStamp.create(9*40, 20, 40, 40, 0, canvas, "CIRCLE")
modeSquare = penStamp.create(10*40, 20, 40, 40, 0, canvas, "SQUARE")
modeHouse = penStamp.create(11*40, 20, 40, 40, 0, canvas, "HOUSE")
modeFlower = penStamp.create(12*40, 20, 40, 40, 0, canvas, "FLOWER")
currentMode = penStamp.create(canvasWidth - 80, 20, 40, 40, 0, canvas, "LINE")

mode = Modes.DRAWING
pen = Pen.LINE
stamp = Stamp.HOUSE

labelPen = tkinter.Label(text = "Pen width")
labelPen.pack()
entryPen = tkinter.Entry()
entryPen.pack()
labelStamp = tkinter.Label(text = "Stamp size")
labelStamp.pack()
entryStamp = tkinter.Entry()
entryStamp.pack()

penWidth = 5
stampWidth = 20
px, py = 0, 0

mc = False

moreColorBG = "white"
drawingColor = "black"

########################################################################################################################
#########################################################################################################################
########################################################################################################################

def drawMoreColors():
    global colors2, moreColorsBG
    stepX, stepY = 35, 25
    moreColorsBG = canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill="white", width=0)
    for y in range(0, canvasHeight, stepY):
        for x in range(0, canvasWidth, stepX):
            try:
                colors2.append(color.create(x, y, stepX, stepY, COLORS[(y // stepY) * (canvasWidth // stepX) + (x // stepX)], 1, canvas))
            except:
                break

def deleteMoreColors():
    global colors2, moreColorsBG
    for color in colors2:
        canvas.delete(color.button)
    canvas.delete(moreColorsBG)
    colors2.clear()

def delete(event):
    global drawings
    if not mc:
        for drawing in drawings:
            canvas.delete(drawing)
        drawings.clear()

def motion(event):
    global px, py
    px = event.x
    py = event.y

def dragL(event):
    global drawings, penWidth, px, py
    x, y = event.x, event.y
    if y > 60 and py > 60:
        if not mc:
            if mode == Modes.DRAWING:
                if pen == Pen.LINE:
                    try:
                        penWidth = int(entryPen.get())
                    except:
                        penWidth = 5
                    drawings.append(canvas.create_line(x, y, px, py, width=penWidth, fill=drawingColor))
                    drawings.append(canvas.create_oval(x - penWidth // 2, y - penWidth // 2, x + penWidth // 2, y + penWidth // 2, width=0, fill=drawingColor))
                if pen == Pen.CIRCLE:
                    try:
                        penWidth = int(entryPen.get())
                    except:
                        penWidth = 5
                    drawings.append(canvas.create_oval(x - penWidth // 2, y - penWidth // 2, x + penWidth // 2, y + penWidth // 2, width=0, fill=drawingColor))
                if pen == Pen.SQUARE:
                    try:
                        penWidth = int(entryPen.get())
                    except:
                        penWidth = 5
                    drawings.append(canvas.create_rectangle(x - penWidth // 2, y - penWidth // 2, x + penWidth // 2, y + penWidth // 2, width=0, fill=drawingColor))
    px, py = x, y

def dragR(event):
    global drawings, penWidth, px, py
    x, y = event.x, event.y
    if y > 60 and py > 60:
        if not mc:
            if pen == Pen.LINE:
                try:
                    penWidth = int(entryPen.get())
                except:
                    penWidth = 5
                drawings.append(canvas.create_line(x, y, px, py, width=penWidth, fill=canvasBG))
                drawings.append(
                    canvas.create_oval(x - penWidth // 2, y - penWidth // 2, x + penWidth // 2, y + penWidth // 2,
                                       width=0, fill=canvasBG))
            if pen == Pen.CIRCLE:
                try:
                    penWidth = int(entryPen.get())
                except:
                    penWidth = 5
                drawings.append(
                    canvas.create_oval(x - penWidth // 2, y - penWidth // 2, x + penWidth // 2, y + penWidth // 2,
                                       width=0, fill=canvasBG))
            if pen == Pen.SQUARE:
                try:
                    penWidth = int(entryPen.get())
                except:
                    penWidth = 5
                drawings.append(
                    canvas.create_rectangle(x - penWidth // 2, y - penWidth // 2, x + penWidth // 2, y + penWidth // 2,
                                            width=0, fill=canvasBG))
    px, py = x, y

def leftClick(event):
    global stampWidth, mc, drawingColor, lastColor, currentColor, pen, mode, stamp, currentMode
    x, y = event.x, event.y
    if not mc:
        for color in colors:
            if (color.x < x < color.x+color.width) and (color.y < y < color.y+color.height):
                lastColor.color = drawingColor
                canvas.itemconfig(lastColor.button, fill=lastColor.color)
                drawingColor = color.color
                currentColor.color = drawingColor
                canvas.itemconfig(currentColor.button, fill=currentColor.color)
        if (moreColor.x < x < moreColor.x+moreColor.width) and (moreColor.y < y < moreColor.y+moreColor.height):
            mc = True
            drawMoreColors()
        elif (lastColor.x < x < lastColor.x+lastColor.width) and (lastColor.y < y < lastColor.y+lastColor.height):
            drawingColor = lastColor.color
            lastColor.color = currentColor.color
            canvas.itemconfig(lastColor.button, fill=lastColor.color)
            currentColor.color = drawingColor
            canvas.itemconfig(currentColor.button, fill=currentColor.color)
        elif (RGB.x < x < RGB.x+RGB.width) and (RGB.y < y < RGB.y+RGB.height):
            c = askcolor()
            if c[-1] != None:
                drawingColor = c[-1]
                lastColor.color = drawingColor
                canvas.itemconfig(lastColor.button, fill=lastColor.color)
                currentColor.color = drawingColor
                canvas.itemconfig(currentColor.button, fill=currentColor.color)
        elif (modeLine.x < x < modeLine.x+modeLine.width) and (modeLine.y < y < modeLine.y+modeLine.height):
            mode = Modes.DRAWING
            pen = Pen.LINE
            currentMode = penStamp.create(canvasWidth - 80, 20, 40, 40, 0, canvas, "LINE")
        elif (modeCircle.x < x < modeCircle.x+modeCircle.width) and (modeCircle.y < y < modeCircle.y+modeCircle.height):
            mode = Modes.DRAWING
            pen = Pen.CIRCLE
            currentMode = penStamp.create(canvasWidth - 80, 20, 40, 40, 0, canvas, "CIRCLE")
        elif (modeSquare.x < x < modeSquare.x+modeSquare.width) and (modeSquare.y < y < modeSquare.y+modeSquare.height):
            mode = Modes.DRAWING
            pen = Pen.SQUARE
            currentMode = penStamp.create(canvasWidth - 80, 20, 40, 40, 0, canvas, "SQUARE")
        elif (modeHouse.x < x < modeHouse.x+modeHouse.width) and (modeHouse.y < y < modeHouse.y+modeHouse.height):
            mode = Modes.STAMP
            stamp = Stamp.HOUSE
            currentMode = penStamp.create(canvasWidth - 80, 20, 40, 40, 0, canvas, "HOUSE")
        elif (modeFlower.x < x < modeFlower.x+modeFlower.width) and (modeFlower.y < y < modeFlower.y+modeFlower.height):
            mode = Modes.STAMP
            stamp = Stamp.FLOWER
            currentMode = penStamp.create(canvasWidth - 80, 20, 40, 40, 0, canvas, "FLOWER")
        elif mode == Modes.STAMP:
            if y > 60:
                if stamp == Stamp.FLOWER:
                    try:
                        stampWidth = int(entryStamp.get())
                    except:
                        stampWidth = 20
                    drawings.append(canvas.create_oval(x+stampWidth, y+stampWidth, x, y, fill = "red", widt = 0))
                    drawings.append(canvas.create_oval(x-stampWidth, y+stampWidth, x, y, fill = "red", widt = 0))
                    drawings.append(canvas.create_oval(x+stampWidth, y-stampWidth, x, y, fill = "red", widt = 0))
                    drawings.append(canvas.create_oval(x-stampWidth, y-stampWidth, x, y, fill = "red", widt = 0))
                    drawings.append(canvas.create_oval(x-stampWidth/2, y-stampWidth/2, x+stampWidth/2, y+stampWidth/2, fill = "yellow", width = 0))
                if stamp == Stamp.HOUSE:
                    try:
                        stampWidth = int(entryStamp.get())
                    except:
                        stampWidth = 20
                    drawings.append(canvas.create_rectangle(x+stampWidth, y+stampWidth, x-stampWidth, y-stampWidth, fill = "red", width = 0))
                    drawings.append(canvas.create_polygon(x-stampWidth, y-stampWidth, x+stampWidth, y-stampWidth, x, y-stampWidth*2, fill = "brown", width = 0))
    elif mc:
        for color in colors2:
            if (color.x < x < color.x+color.width) and (color.y < y < color.y+color.height):
                lastColor.color = drawingColor
                canvas.itemconfig(lastColor.button, fill = lastColor.color)
                drawingColor = color.color
                currentColor.color = drawingColor
                canvas.itemconfig(currentColor.button, fill = currentColor.color)
                mc = False
                deleteMoreColors()
                break

########################################################################################################################
#########################################################################################################################
########################################################################################################################

colors.append(color.create(0, 20, 40, 40, 'black', 0, canvas))
colors.append(color.create(40, 20, 40, 40, 'red', 0, canvas))
colors.append(color.create(80, 20, 40, 40, 'green', 0, canvas))
colors.append(color.create(120, 20, 40, 40, 'blue', 0, canvas))
colors.append(color.create(160, 20, 40, 40, 'yellow', 0, canvas))
colors.append(color.create(200, 20, 40, 40, 'brown', 0, canvas))

########################################################################################################################
#########################################################################################################################
########################################################################################################################

canvas.bind_all("<Delete>", delete)
canvas.bind_all("<Motion>", motion)
canvas.bind_all("<B1-Motion>", dragL)
canvas.bind_all("<B3-Motion>", dragR)
canvas.bind_all("<Button-1>", leftClick)

canvas.mainloop()
