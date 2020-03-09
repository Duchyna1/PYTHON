import tkinter
import random
import time

width, height = 350, 200
centerW, centerH = width//2, height//2

c = tkinter.Canvas(width = width, height = height, background = '#454545')
c.pack()

c.create_rectangle(centerW-148, centerH-50, centerW-50, centerH+50, fill = '#D3D3D3', width = 5)
c.create_rectangle(centerW-50, centerH-50, centerW+50, centerH+50, fill = '#D3D3D3', width = 5)
c.create_rectangle(centerW+50, centerH-50, centerW+148, centerH+50, fill = '#D3D3D3', width = 5)

# BAR 25% | 2BAR 25% | 3BAR 25% | @ 10% | # 10 % | $ 4% | 7 1%
symbols = ['BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 'BAR', 
           'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR', 'BAR\nBAR',
           'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR', 'BAR\nBAR\nBAR',
           '@', '@', '@', '@', '@', '@', '@', '@', '@', '@',
           '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
           '$', '$', '$', '$', 
           '7']

F = c.create_text(centerW-99, centerH, text = '7')
S = c.create_text(centerW, centerH, text = '7')
T = c.create_text(centerW+99, centerH, text = '7')
F_symbol = '7'
S_symbol = '7'
T_symbol = '7'

balance, bet = 1000, 10 ####################################################################################

c.create_text(centerW-115, centerH-65, text = 'BALANCE:')
balance_text = c.create_text(centerW-65, centerH-65, text = balance)
c.create_text(centerW+70, centerH-65, text = 'BET:')
bet_text = c.create_text(centerW+100, centerH-65, text = bet)

######################################################################################
######################################################################################
######################################################################################
    
def setF(symbol):
    global F, F_symbol
    c.itemconfig(F, text = symbol)
    F_symbol = symbol
    c.update()
def setS(symbol):
    global S, S_symbol
    c.itemconfig(S, text = symbol)
    S_symbol = symbol
    c.update()
def setT(symbol):
    global T, T_symbol
    c.itemconfig(T , text = symbol)
    T_symbol = symbol
    c.update()
def ran_sym_3slot():
    global symbols
    setF(symbols[random.randrange(100)])
    setS(symbols[random.randrange(100)])
    setT(symbols[random.randrange(100)])
def ran_sym_2slot():
    global symbols
    setS(symbols[random.randrange(100)])
    setT(symbols[random.randrange(100)])
def ran_sym_1slot():
    global symbols
    setT(symbols[random.randrange(100)])
def roll(event):
    global balance, bet, balance_text
    if balance > 0:
        balance = balance - bet
        c.itemconfig(balance_text, text = balance)
        c.update()
        for i in range(10):
            i = i+1
            ran_sym_3slot()
            time.sleep(.1)
        for i in range(10):
            i = i+1
            ran_sym_2slot()
            time.sleep(.1)
        for i in range(10):
            i = i+1
            ran_sym_1slot()
            time.sleep(.1)
        balance = balance+bet*win()
        c.itemconfig(balance_text, text = balance)
        c.update()
def fast_roll(event):
    global balance, bet, balance_text
    if balance > 0:
        balance = balance - bet
        c.itemconfig(balance_text, text = balance)
        c.update()
        ran_sym_3slot()
        balance = balance+bet*win()
        c.itemconfig(balance_text, text = balance)
        c.update()
def win():
    global F_symbol, S_symbol, T_symbol
    if F_symbol == 'BAR':
        if S_symbol == 'BAR':
            if T_symbol == 'BAR':
                return 10
    if F_symbol == 'BAR\nBAR':
        if S_symbol == 'BAR\nBAR':
            if T_symbol == 'BAR\nBAR':
                return 10
    if F_symbol == 'BAR\nBAR\nBAR':
        if S_symbol == 'BAR\nBAR\nBAR':
            if T_symbol == 'BAR\nBAR\nBAR':
                return 10
    if F_symbol == '@':
        if S_symbol == '@':
            if T_symbol == '@':
                return 100
    if F_symbol == '#':
        if S_symbol == '#':
            if T_symbol == '#':
                return 100
    if F_symbol == '$':
        if S_symbol == '$':
            if T_symbol == '$':
                return 1000
    if F_symbol == '7':
        if S_symbol == '7':
            if T_symbol == '7':
                return 10000
    return 0
def reset(event):
    global balance, balance_text
    balance = 1000
    c.itemconfig(balance_text, text = balance)
    c.update()
def test(event):
    global balance, bet, balance_text
    setF('7')
    setS('7')
    setT('7')
    balance = balance - bet
    c.itemconfig(balance_text, text = balance)
    c.update()
    balance = balance+bet*win()
    c.itemconfig(balance_text, text = balance)
    c.update()

######################################################################################
######################################################################################
######################################################################################

c.bind_all('f', fast_roll)
c.bind_all('<Return>', roll)
c.bind_all('r', reset)
c.bind_all('t', test)

tkinter.mainloop()