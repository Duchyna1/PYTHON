ludia, vek, dvojicky, jedinacik = int(input()), sorted([int(i) for i in input().split()]), [], []
while True:
    if ludia == 1:
        print(1, vek[0])
        break
    elif vek[0] == vek[1]:
        dvojicky.append(vek[0])
        del vek[1]
        del vek[0]
    else:
        jedinacik.append(vek[0])
        del vek[0]
    if len(vek) == 1:
        jedinacik.append(vek[0])
        del vek[0]
    if len(vek) == 0:
        break
if ludia == 1:
    pass
elif len(jedinacik) > 0:
    print(len(dvojicky)+1, jedinacik[-1])
else:
    print(len(dvojicky), dvojicky[-1])
    