from random import randint

metre = 0
ano = 1
while 0<=metre<=100:
    fet = randint(0, 1) 
    print(fet, end=' ')
    if fet == 1:
        ano *= -1
        print(ano, end=' ')
        metre += ano*10
    else:
        metre += ano*10
    print(metre)
print(metre)