n = int(input())

def stvorec(n):
    for i in range(n):
        print('*'*n)

def lavo_dole(n):
    for x in range(1, n+1):
        print('*'*x)

def lavo_hore(n):
    for x in range(n):
        print('*'*(n-x))

def dole(n):
    for x in range(n):
        print(' '*x + '*'*(n-x-1) + '*' + '*'*(n-x-1))

def prazdny(n):
    for x in range(n):
        if x == 0 or x == n-1:
            print('*'*n)
        else:
            print('*' + ' '*(n-2) + '*')

def pravo_hore(n):
    for x in range(n):
        print(' '*(x) + '*'*(n-x))

def pravo(n):
    lavo_dole(n)
    lavo_hore(n-1)

def pravo_prazdne(n):
    for x in range(1, n+1):
        print(' '*(x-1)+'*')
    for x in range(n-1):
        print(' '*(n-1-x-1)+'*')

stvorec(n)
print()
lavo_dole(n)
print()
lavo_hore(n)
print()
dole(n)
print()
prazdny(n)
print()
pravo_hore(n)
print()
pravo(n)
print()
pravo_prazdne(n)
print()