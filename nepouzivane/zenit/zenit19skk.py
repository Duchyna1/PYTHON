from random import randrange, random
from math import sqrt, degrees, atan, tan
pi = 3.14

pocet = int(input())
if pocet == 1:
    n = input().split()
    print(n[0], n[1])
else:
    body = []
    vzdialenosti = []

    def from_0(x, y):
        return sqrt(x**2+y**2)

    def from_avr(x, y, mid):
        return sqrt((x-mid)**2+y**2)

    for n in range(pocet):
        a = input().split()
        x, y = float(a[0]), float(a[1])
        if x < 0:
            vz0 = -1*from_0(x, y)
        else:
            vz0 = from_0(x, y)
        bod = [x, y, vz0]
        body.append(bod)

    body.sort(key=lambda l:l[2])

    midX, midY = (body[0][0]+body[-1][0])/2, (body[0][1]+body[-1][1])/2
    a = midX-body[0][0]
    b = midY-body[0][1]
    alfa = degrees(atan(a/b))
    beta = 90-alfa
    offX = tan(beta*pi/180)*midY
    avr = offX+midX

    for n in range(pocet):
        vzdialenost = from_avr(body[n][0], body[n][1], avr)
        vzdialenosti.append(vzdialenost)

    vzdialenosti.sort()
    print2 = vzdialenosti[-1]
    print(avr, print2)