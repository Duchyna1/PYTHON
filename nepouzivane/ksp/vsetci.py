prvy = input()
prvy = prvy.split(' ')
ludia = int(prvy[0])
mimo = int(prvy[1])
vaha = input()
vaha = vaha.split(' ')
vaha = [int(vaha[i]) for i in range(mimo)]
while len(vaha) < ludia*2:
    vaha.append(0)
vaha.sort()
for x in range(ludia):
    print(vaha[x], vaha[ludia*2-x-1])