import tkinter
from math import sin, cos, radians

bt = tkinter.Canvas(width = 300, height = 300, bg = 'black')
bt.pack()

def find_x_y_from_angel(angel):
    global bt

    x = cos(radians(angel))*100
    y = sin(radians(angel))*100

    # print(x/100, y/100)

    # bt.create_oval(150+100, 150+100, 150-100, 150-100, outline = 'white')
    # bt.create_line(150, 0, 150, 300, fill = 'white')
    # bt.create_line(0, 150, 300, 150, fill = 'white')

    bt.create_line(150, 150, 150+x, 150-y, fill = 'white')
    bt.update()

# angel = int(input('angel: '))
# find_x_y_from_angel(angel)

for x in range(90, -99999999, -6):
    find_x_y_from_angel(x)
    find_x_y_from_angel(x//60+90)
    find_x_y_from_angel(x//3600+90)
    bt.after(1)
    bt.delete('all')

bt.mainloop()