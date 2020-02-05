vaha = float(input("vaha v kg\n"))
vyska = float(input("vyska v metroch\n"))
BMI = vaha/(vyska**2)
if BMI < 18.5:
    print('podváha') 
elif 18.5<=BMI<25:    
    print('normálna hmotnosť')
elif 25<=BMI<30:
    print('nadváha')
elif BMI>30:
    print('obezita')