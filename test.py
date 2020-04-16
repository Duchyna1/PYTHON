# # 1
# from random import randrange
# s = input()
# sifra = ''
# for i in range(len(s)):
#     sifra = sifra + str(randrange(0, 10))
# print(sifra)
#
# # 2
# s1 = input()
# s2 = input()
# noves2 = s2
# for znak in s1:
#     pocet = s2.count(znak)
#     print(znak, pocet)
#     noves2.replace(znak, '*')
# print(noves2)
#
# # 3
# s = input()
# noves = ''
# staryZnak = ' '
# for znak in s:
#     if znak == 'i' or znak == 'y':
#         if znak == 'i':
#             noves = noves + 'y'
#         if znak == 'y':
#             noves = noves + 'i'
#     else:
#         if staryZnak == ' ':
#             noves = noves + znak.upper()
#         else:
#             noves = noves + znak
#     staryZnak = znak
# print(noves)
#
# # 4
# s = input()
# pocetCislic = 0
# for znak in s:
#     if 48 <= ord(znak) <= 57:
#         print(znak, ord(znak))
#         pocetCislic = pocetCislic + s.count(znak)
#         s = s.replace(znak, '*')
# print(pocetCislic)
# print(s)
#
# # 5
# s = input()
# kolkatyZnak = 1
# odsifrovany = ''
# for znak in s:
#     if kolkatyZnak % 2 == 1:
#         odsifrovany = odsifrovany + znak
#     kolkatyZnak = kolkatyZnak+1
# odsifrovany = odsifrovany.replace(' ', '\n')
# print(odsifrovany)
#
#
# 1C
s = 'Vianoce' # input()
s = s + ' '
for i in range(len(s)):
    print(i*' ' + s[:-i])
#
# # 2C
# s = input()
# predoslyZnak = ''
# vysledok = ''
# for znak in s:
#     if znak != predoslyZnak:
#         vysledok = vysledok + znak
#         predoslyZnak = znak
# print(vysledok)
#
# # 3C
# s = input()
# s = ' ' + s + ' '
# vysledok = ''
# for i in range(1, len(s)):
#     if s[i-1] == ' ' and s[i+1] == ' ':
#         vysledok = vysledok + s[i].upper()
#     else:
#         vysledok = vysledok + s[i]
# print(vysledok)