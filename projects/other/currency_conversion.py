print('###########################')
print('### CURRENCY CONVERSION ###')
print('###########################')



def EURtoEUR(EUR):
    return EUR
def KZCtoEUR(KZC):
    EUR = KZC * 0.039
    return EUR
def EURtoKZC(EUR):
    KZC = EUR * 25.84
    return KZC
def PLNtoEUR(PLN):
    EUR = PLN * 0.23
    return EUR
def EURtoPLN(EUR):
    PLN = EUR * 4.32
    return PLN
def dolaretoEUR(dolare):
    EUR = dolare * 1
    return EUR
def EURtodolare(EUR):
    dolare = EUR * 1
    return dolare
def librytoEUR(libry):
    EUR = libry * 1
    return EUR
def EURtolibry(EUR):
    libry = EUR * 1
    return libry

    
while True:
    print()
    print('\'eur\' = EUR\t\'kzc\' = KZC')
    print('\'pln\' = PLN\t\'libry\' = libry')
    print('\'dolare\' = dolare')
    print('\'q\' to quit')
    print()
    print('amount currency to currency')

    a = input()
    if a == 'q':
        break
    a = a.split(' ')
    fromSuma = int(a[0])
    fromMena = a[1]
    toMena = a[3]
    medziEUR = 0
    prevod = 0

    if fromMena == 'eur':
        medziEUR = EURtoEUR(fromSuma)
    if fromMena == 'kzc':
        medziEUR = KZCtoEUR(fromSuma)
    if fromMena == 'pln':
        medziEUR = PLNtoEUR(fromSuma)
    if fromMena == 'dolare':
        medziEUR = dolaretoEUR(fromSuma)
    if fromMena == 'libry':
        medziEUR = librytoEUR(fromSuma)



    if toMena == 'eur':
        prevod = EURtoEUR(medziEUR)
    if toMena == 'kzc':
        prevod = EURtoKZC(medziEUR)
    if toMena == 'pln':
        prevod = EURtoPLN(medziEUR)
    if toMena == 'dolare':
        prevod = EURtodolare(medziEUR)
    if toMena == 'libry':
        prevod = EURtolibry(medziEUR)

    print()
    print('#' * len(str(fromSuma) + ' ' + fromMena + ' = ' + str(prevod) + ' ' + toMena))
    #print('#' * len(str(fromSuma) + ' ' + fromMena + ' = ' + str(prevod) + ' ' + toMena))
    print(str(fromSuma) + ' ' + fromMena + ' = ' + str(prevod) + ' ' + toMena)
    print('#' * len(str(fromSuma) + ' ' + fromMena + ' = ' + str(prevod) + ' ' + toMena))
    #print('#' * len(str(fromSuma) + ' ' + fromMena + ' = ' + str(prevod) + ' ' + toMena))
    dorax = input('\'q\' to quit\nenter to continue\n')
    if dorax == 'q':
        break