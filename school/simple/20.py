a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('3 rovnake')
elif a == b or a == c or b == c:
    print('2 rovnake')
else:
    print('1 rovnake')