from math import gcd

asteroids = []
for a in range(21):
    asteroids.append([x for x in input()])

numbers = []
counter = 0
bol = False

for y in range(21):
    for x in range(21):
        if asteroids[x][y] == '#':
            for yy in range(21):
                for xx in range(21):
                    if asteroids[xx][yy] == '#' and xx != x and yy != y:
                            offx, offy = xx-x, yy-y
                            nsd = gcd(offx, offy)
                            if nsd == 1:
                                counter += 1
                            else:
                                bol = False
                                for step in range(1, nsd+1):
                                    smallx, smally = offx//nsd, offy//nsd
                                    if asteroids[x+smallx*step][y+smally*step] == '#':
                                        bol = True
                                        break
                                if not bol:
                                    counter += 1
            numbers.append(counter)
            counter = 0

print(max(numbers))
