x = 0
q = 20
w = -20 
e = 40
r =-40
t = 60
y=10

u=600
i=580
o=620
p=560
a=640
s=540
d=590
v=-300
img=0
z=0
def setup():
  
    size(600,400)
    global img

    img=loadImage("LOL.png")

def draw():
    global x,q,w,e,r,t,y,u,i,o,p,a,s,d,v,img,z
    background(0,255,236)
    image(img,x,z+10,30,30) 
    image(img,10+60+100,z,30,30) 
    image(img,30+60+100,z,30,30) 
    image(img,60+60,z,30,30) 
    image(img,90+60,z,30,30) 
    image(img,120+60,z,30,30) 
    image(img,150+60,z,30,30) 
    image(img,180+60,z,30,30) 
    image(img,110+60,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    image(img,x,z,30,30) 
    
    
    
    
    
    noStroke()
   
    # fill(255)
   
   
    
    
    if(v!=60):
        v=v+1
    fill(233,255,0)
    ellipse(300, v, 70,70)
    fill(255)
    ellipse(x, 40, 40,40)
    ellipse(q, 40, 40,40)                #верх
    ellipse(w, 40, 40,40)
    ellipse(e, 40, 40,40)
    
    ellipse(x, 80, 40,40)
    ellipse(q, 80, 40,40)                #низ
    ellipse(w, 80, 40,40)
    ellipse(e, 80, 40,40)
    
    ellipse(y, 20, 40,40)
    
    ellipse(y, 100, 40,40)        
                
   
    
     
    ellipse(u, 60, 40,40)
    ellipse(i, 60, 40,40)
    ellipse(o, 60, 40,40)              #центр 2
    ellipse(p, 60, 40,40)
    ellipse(a, 60, 40,40)
    ellipse(s,60,40,40)
   
    ellipse(u, 40, 40,40)
    ellipse(i, 40, 40,40)                #верх 2
    ellipse(o, 40, 40,40)
    ellipse(p, 40, 40,40)
    
    ellipse(u, 80, 40,40)
    ellipse(i, 80, 40,40)                #низ 2
    ellipse(o, 80, 40,40)
    ellipse(p, 80, 40,40)
    
    ellipse(d, 20, 40,40)
    
    ellipse(d, 100, 40,40)        
                
   
    
     
    ellipse(x, 60, 40,40)
    ellipse(q, 60, 40,40)
    ellipse(w, 60, 40,40)              #центр
    ellipse(e, 60, 40,40)
    ellipse(r, 60, 40,40)
    ellipse(t,60,40,40)
 
    x = x + 1
    q=q+1
    w=w+1
    e=e+1
    r=r+1
    t=t+1
    y=y+1
   
    u=u-1
    i=i-1
    o=o-1
    p=p-1
    a=a-1
    s=s-1
    d=d-1
    z=z+1 
