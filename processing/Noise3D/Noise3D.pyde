increment = 0.01

zoff = 0.0

zincrement = 0.02


def setup():
    size(200, 200)
    frameRate(30)


def draw():
    global zoff

    loadPixels()
    xoff = 0.0  


    for x in xrange(width):
        xoff += increment    
        yoff = 0.0     
        for y in xrange(height):
            yoff += increment  

            bright = noise(xoff, yoff, zoff) * 255
    
            times = 5
            for a in range(1, times+1):
                if 255/times*(a-1)<bright<255/times*a:
                    pixels[x + y * width] = color(random(255/times*(a-1), 255/times*a), random(255/times*(a-1), 255/times*a), random(255/times*(a-1), 255/times*a))
    updatePixels()
    zoff += zincrement  
