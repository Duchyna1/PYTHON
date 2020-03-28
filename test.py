#1
meno = input('Meno: ')
meno = meno.upper()
print(meno)

#2
nahrdelnik = input('Nahrdelnik: ')
podobny = nahrdelnik.replace('a', '***')
print(podobny)

#3
zaznam = input('Zaznam: ')
slabika = input('Slabika: ')
print(zaznam.count(slabika))

#4
veta = input('Veta: ')
novaVeta = ''
for znak in veta:
    if znak == 'z':
        novaVeta = novaVeta + 'y'
    elif znak == 'Z':
        novaVeta = novaVeta + 'Y'
    elif znak == 'y':
        novaVeta = novaVeta + 'z'
    elif znak == 'Y':
        novaVeta = novaVeta + 'Z'
    else:
        novaVeta = novaVeta + znak
print(novaVeta)