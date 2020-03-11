x = [int(input()),int(input()),int(input())]
x.sort()
nejaky = False
if x[-1] < x[0]+x[1]:
    if x[0] == x[1] == x[2]:
        print('rovnostranny')
        nejaky = True
    elif x[0] == x[1] or x[0] == x[2] or x[1] == x[2]:
        print('rovnoramenny')
        nejaky = True
    if x[0]**2+x[1]**2==x[2]**2:
        print('pravouhli')
        nejaky = True
    if not nejaky:
        print('iny')
    
     
else:
    print('Flase')