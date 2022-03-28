GlowScript 2.6 VPython

Length1=1
Length2=1
k1=200
k2=200

scene.background = color.white
scene.caption = "Code is here: https://github.com/natecundiff/MP3PhysicsProject"

stationary=sphere(pos=vec(0,Length1,0), radius=0.05, color=color.black)

node1=sphere(pos=stationary.pos-vec(0,Length1,0),radius=0.05,color=color.blue)
length1=helix(pos=stationary.pos,axis=node1.pos-stationary.pos,radius=0.015,color=color.black)
length1.coils = 30

node2=sphere(pos=node1.pos-vec(0,Length2,0),radius=0.05,color=color.blue)
length2=helix(pos=node1.pos, axis=node2.pos-node1.pos, radius=0.015,color=color.black)
length2.coils = 30

g=vec(0,-9.8,0)
theta1=75*pi/180
theta2=58*pi/180
theta1dot=0
theta2dot=0.8

node1.pos=stationary.pos+vec(Length1*sin(theta1),-Length1*cos(theta1),0)
node2.pos=node1.pos+vec(Length2*sin(theta2),-Length2*cos(theta2),0)
length1.axis=node1.pos-stationary.pos
length2.pos=node1.pos
length2.axis=node2.pos-node1.pos

mass1=20
mass2=20

node1.p=vec(0,0,0)
node2.p=vec(0,0,0)
node1.m=mass1
node2.m=mass2

t=0
dt=0.00001

attach_trail(node2, retain=100, color=color.blue)

#parallel

BLength1=1.001
BLength2=1.001
Bk1=200
Bk2=200

Bstationary=sphere(pos=vec(0,BLength1,0), radius=0.05, color=color.black)

Bnode1=sphere(pos=Bstationary.pos-vec(0,BLength1,0),radius=0.05,color=color.red)
Blength1=helix(pos=Bstationary.pos,axis=Bnode1.pos-Bstationary.pos,radius=0.015,color=color.black)
Blength1.coils = 15

Bnode2=sphere(pos=Bnode1.pos-vec(0,BLength2,0),radius=0.05,color=color.red)
Blength2=helix(pos=Bnode1.pos, axis=Bnode2.pos-Bnode1.pos, radius=0.015,color=color.black)
Blength2.coils = 15

Bg=vec(0,-9.8,0)
Btheta1=75*pi/180
Btheta2=58*pi/180
Btheta1dot=0
Btheta2dot=0.8

Bnode1.pos=Bstationary.pos+vec(BLength1*sin(Btheta1),-BLength1*cos(Btheta1),0)
Bnode2.pos=Bnode1.pos+vec(BLength2*sin(Btheta2),-BLength2*cos(Btheta2),0)
Blength1.axis=Bnode1.pos-Bstationary.pos
Blength2.pos=Bnode1.pos
Blength2.axis=Bnode2.pos-Bnode1.pos

Bmass1=20
Bmass2=20

Bnode1.p=vec(0,0,0)
Bnode2.p=vec(0,0,0)
Bnode1.m=Bmass1
Bnode2.m=Bmass2

Bt=0
Bdt=0.00001

attach_trail(Bnode2, retain=100, color=color.red)

while Bt<120000:
    rate(100000)
    Br1=Bnode1.pos-Bstationary.pos
    Br2=Bnode2.pos-Bnode1.pos
    BF2=Bnode2.m*Bg-Bk2*(mag(Br2)-BLength2)*norm(Br2)
    BF1=Bnode1.m*Bg-BF2-Bk1*(mag(Br1)-BLength1)*norm(Br1)
    Bnode1.p=Bnode1.p+BF1*Bdt
    Bnode2.p=Bnode2.p+BF2*Bdt
    Bnode1.pos=Bnode1.pos+Bnode1.p*Bdt/Bnode1.m
    Bnode2.pos=Bnode2.pos+Bnode2.p*Bdt/Bnode2.m
    Blength1.axis=Bnode1.pos-Bstationary.pos
    Blength2.pos=Bnode1.pos
    Blength2.axis=Bnode2.pos-Bnode1.pos
    Bt=Bt+Bdt
    BUg=Bnode1.m*mag(Bg)*Bnode1.pos.y+Bnode2.m*mag(Bg)*Bnode2.pos.y
    BT=.5*Bnode1.m*mag(Bnode1.p/Bnode1.m)**2+.5*Bnode2.m*mag(Bnode2.p/Bnode2.m)**2
    BUk=.5*Bk1*(mag(Br2)-BLength2)**2+.5*Bk2*(mag(Br1)-BLength1)**2
    BE=BT+BUg+BUk
    r1=node1.pos-stationary.pos
    r2=node2.pos-node1.pos
    F2=node2.m*g-k2*(mag(r2)-Length2)*norm(r2)
    F1=node1.m*g-F2-k1*(mag(r1)-Length1)*norm(r1)
    node1.p=node1.p+F1*dt
    node2.p=node2.p+F2*dt
    node1.pos=node1.pos+node1.p*dt/node1.m
    node2.pos=node2.pos+node2.p*dt/node2.m
    length1.axis=node1.pos-stationary.pos
    length2.pos=node1.pos
    length2.axis=node2.pos-node1.pos
    t=t+dt
    Ug=node1.m*mag(g)*node1.pos.y+node2.m*mag(g)*node2.pos.y
    T=.5*node1.m*mag(node1.p/node1.m)**2+.5*node2.m*mag(node2.p/node2.m)**2
    Uk=.5*k1*(mag(r2)-Length2)**2+.5*k2*(mag(r1)-Length1)**2
    E=T+Ug+Uk
