od, do = 359282, 820401

count = 0

print('od, do ', od, do)
dve = False

for cislo in range(od, do):
    cisla = []
    for cifra in str(cislo):
        cisla.append(int(cifra))
    if int(cisla[0]) <= int(cisla[1]) <= int(cisla[2]) <= int(cisla[3]) <= int(cisla[4]) <= int(cisla[5]):
        for do10 in range(10):
            aktu = cisla.count(do10)
            if aktu == 2:
                dve = True
        if dve:
            print(cislo)
            count += 1
            dve = False

print('count', count)
