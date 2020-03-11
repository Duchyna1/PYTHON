from random import randint

p = [randint(20, 40) for x in range(52)]
d = 0
ad = 0
for x in range(1, len(p)):
    a = p[x]
    b = p[x-1]
    if a > b:
        d += 1
    else:
        if d > ad:
            ad = d
        d = 0

print(p)
print(min(p), ad)
