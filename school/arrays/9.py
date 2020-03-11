from random import randint

nv = [randint(500, 1500) for x in range(60)]
s = [randint(500, 2000) for x in range(60)]

cs = 0
for x in range(len(s)):
    cs += s[x]
print(cs, 'metrov')
print(cs//1000, 'km/h')
print(max(nv), 'max nadmorska vyska')
for x in range(60):
    if nv[x] == max(nv):
        print('v', x+1, 'minute')
        break