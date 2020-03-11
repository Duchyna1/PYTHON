znamienko = 0
n = int(input())

vysledok = 0
for x in range(1, n+1):
    if znamienko == 0:
        vysledok -= 1/x
        znamienko = 1
    elif znamienko == 1:
        vysledok += 1/x
        znamienko = 0
    
print(vysledok)