SUM = int(input())
ps = SUM//500
SUM %= 500 
ds = SUM//200
SUM %= 200
s = SUM//100
SUM %= 100
p = SUM//50
SUM %= 50
d = SUM//20
SUM %= 20
de = SUM//10
SUM %= 10
pe = SUM//5
SUM %= 5
j = SUM//1
print(ps, ds, s, p, d, de, pe, j, ps+ds+s+p+d+de+ps+j)