x = [int(input()),int(input()),int(input())]
x.sort()
if x[-1] < x[0]+x[1]:
    print('True')
else:
    print('Flase')