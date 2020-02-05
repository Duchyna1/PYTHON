from math import sin, cos
import BetterTkinter as bt

pointX = 1
waveY = 50
waveX = 50
offX = 0
r = 1
bt.start()


def stepSIN(x):
    # bt.line(x, sin(x/waveX+offX)*waveY+250, x+pointX, sin((x+pointX)/waveX+offX)*waveY+250)
    bt.circle(x, sin(x/waveX+offX)*waveY+250, r, fill='white', width=0)
    if x < 700:
        stepSIN(x+pointX)


def stepCOS(x):
    bt.circle(x, cos(x/waveX+offX)*waveY+250, r, fill='white', width=0)
    if x < 700:
        stepCOS(x+pointX)


stepSIN(10)

bt.end()
