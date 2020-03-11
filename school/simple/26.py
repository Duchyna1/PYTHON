def start(x):
    print(x)
    if x < 100:
        start(x+2)

start(2)