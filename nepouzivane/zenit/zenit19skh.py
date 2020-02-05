n = input()
ano = False
new = ''
if '6' in n:
    ano = True
if '9' in n:
    ano = True
if '1' in n:
    ano = False
elif '3' in n:
    ano = False
elif '4' in n:
    ano = False
elif '7' in n:
    ano = False
else:
    for x in reversed(n):
        if x == '6':
            new = new+'9'
        elif x == '9':
            new = new+'6'
        else:
            new = new+str(x)
    if new == n:
        ano = False    
if ano:
    print('ano')
else:
    print('nie')