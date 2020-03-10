from opensimplex import OpenSimplex

gen = OpenSimplex()

def noise(nx, ny):
    return gen.noise2d(nx, ny) / 2.0 + 0.5

value = []

width = 5
height = 5

for y in range(height):
    value.append([0] * width)
    for x in range(width):
        nx = x/width - 0.5
        ny = y/height - 0.5
        val = int(noise(nx, ny)*1000)
        if val > 500:
            value[y][x] = 1
        else:
            value[y][x] = 0
    print(value[y])
