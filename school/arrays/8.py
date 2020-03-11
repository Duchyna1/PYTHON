from random import randint

z = [randint(1, 8) for x in range(100)]
print(z)
p = [0 for x in range(8)]
for x in range(len(z)):
    p[z[x]-1] += 1

print(p)
bp = []
n = len(z)*10
np = -1
for x in range(len(p)):
    if p[x] == 0:
        print('predavac', x+1, 'nebol v praci')
    else:
        if p[x] < n:
            n = p[x]
            np = x+1
print('predavac', np, 'bol najlenivejsi')
