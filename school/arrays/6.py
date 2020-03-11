from random import randint
import  tkinter

t = [randint(0, 25) for x in range(30)]
max = max(t)
min = min(t)
s = 0
for x in range(len(t)):
    s += t[x]
p = s/len(t)

c = tkinter.Canvas(width=600, height=500)
c.pack()

c.create_line(0, 500-p*20, 600, 500-p*20, width=5, fill='yellow')
for x in range(len(t)):
    if t[x] == max or t[x] == min:
        if t[x] == 0:
            c.create_rectangle(x*20, 500, x*20+20, 500-5, width=0, fill='red')
        else:
            c.create_rectangle(x*20, 500, x*20+20, 500-t[x]*20, width=0, fill='red')
    else:
        if t[x] < p:
            c.create_rectangle(x*20, 500, x*20+20, 500-t[x]*20, width=0, fill='light blue')
            if t[x] == 0:
                c.create_rectangle(x*20, 500, x*20+20, 500-5, width=0, fill='light blue')
        else:
            c.create_rectangle(x*20, 500, x*20+20, 500-p*20, width=0, fill='light blue')
            c.create_rectangle(x*20, 500-p*20, x*20+20, 500-t[x]*20, width=0, fill='IndianRed1')
    c.create_text(x*20+10, 250, text=t[x])

c.mainloop()