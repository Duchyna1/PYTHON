from time import sleep
from random import randrange

def progress(percent=0, width=100):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

def run_progress():
    for i in range(101):
        s  = randrange(10)/(10**randrange(2,5))
        sleep(s)
        progress(i)

print('1+1=?')
print('Wait...')
sleep(randrange(50)/10)
run_progress()
print()
print('Sorting...')
sleep(randrange(50)/10)
run_progress()
print()
print('Chilling...')
sleep(randrange(50)/10)
run_progress()
print()
print('Feting...')
sleep(randrange(50)/10)
run_progress()
print()
print('Calculating...')
sleep(randrange(50)/10)
run_progress()
print()
sleep(randrange(50)/10)
print('1+1=2', end='')
input()