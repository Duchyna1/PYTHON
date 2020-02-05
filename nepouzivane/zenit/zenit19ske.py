n = input().split()
r = int(n[0])
s = int(n[1])
if r == 13 and s == 13:
    print('Ujo je doma!', end='')
else:
    for y in range(15):
        for x in range(15):
            if x == 0:
                print('#', end='')
            elif x == 14:
                print('#')
            elif y == 0 or y == 14:
                print('#', end='')
            elif x == s and y == r:
                print('U', end='')
            elif x == 13 and y == 13:
                print('D', end='')
            elif x > s and r == y:
                print('x', end='')
            elif y > r and x == 13:
                print('x', end='')
            else:
                print('.', end='')
            