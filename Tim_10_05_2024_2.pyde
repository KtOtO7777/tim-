x = 300
e=200
c=300
w=200
r=300
t=200
y=300
u=200
def setup():
  size(600,400)
def draw():
  global x,e,c,w,r,t,y,u
  background(100)
  ellipse(x,e, 20,20)
  x = x + 1
  e=e+1
  ellipse(c, w, 20, 20)
  c=c-1
  w=w-1
  ellipse(r, t, 20, 20)
  r=r+1
  t=t-1
  ellipse(y, u, 20, 20)
  y=y-1
  u=u+1
