x=0
def setup():
    size(2400,1600)
def draw():
    global x
    background(random(0,255),random(0,255),random(0,255))
    fill(random(0,255),random(0,255),random(0,255))
    frameRate(100)
    ellipse(x, x, x,x)
    x = x + 0.1
