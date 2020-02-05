numbers = [x for x in input()]

image = []

for x in range(25*6):
    image.append('2')

for x in range(0, len(numbers), 25*6):
    for y in range(25*6):
        if image[y] == '2':
            image[y] = numbers[x+y]

for x in range(0, 25*6, 25):
    for y in range(25):
        if image[x+y] == '0':
            print(' ', end='')
        elif image[x+y] == '1':
            print('#', end='')
    print()
