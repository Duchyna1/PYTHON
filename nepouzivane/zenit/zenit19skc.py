n = [int(x) for x in input().split()]
n.sort()
Alicka = n.count(6)
Barborka = n.count(1)
if Alicka > Barborka:
    print('Alicka')
elif Barborka > Alicka:
    print('Barborka')
else:
    print('Remiza')