import math
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
from matplotlib import animation
from itertools import combinations
n=9
r=0.05
dt=0.01
T=20
m1=0.1
m2=0.1
N=int(T/dt)
x=np.zeros((N+1,n))
y=np.zeros((N+1,n))
vx=np.zeros((N+1,n))
vy=np.zeros((N+1,n))
vx[0]=np.random.uniform(-1,1,n)
vy[0]=np.random.uniform(-1,1,n)
left=-0.5
right=0.5
up=0.5
bottom=-0.5
n1=int(math.sqrt(n))
#mesh
xm=(right-left)/math.sqrt(n)
ym=(up-bottom)/math.sqrt(n)
ni=0
for yi in range(0,n1):
    for xi in range(0,n1):
        x[0,ni]=np.array([xm/2+xi*xm+left])
        y[0,ni]=np.array([ym/2+yi*ym+bottom])
        ni=ni+1
for t in range (0,N):
    for j in range(0,n):
        x[t+1,j]=x[t,j]+dt*vx[t,j]
        y[t+1,j]=y[t,j]+dt*vy[t,j]
    pairs=combinations(range(n),2)
    for j,k in pairs:
        R=math.sqrt((x[t+1,k]-x[t+1,j])**2+(y[t+1,k]-y[t+1,j])**2)
        if R<2*r:
            x[t+1,j]=x[t,j]
            x[t+1,k]=x[t,k]
            y[t+1,j]=y[t,j]
            y[t+1,k]=y[t,k]
            #in a system where the first particle is at rest
            Vx=vx[t,k]-vx[t,j]
            Vy=vy[t,k]-vy[t,j]
            V=math.sqrt(Vx**2+Vy**2)
            #rotation angle of coordinates (x,y) to (t,n)
            dx=x[t+1,k]-x[t+1,j]
            dy=y[t+1,k]-y[t+1,j]
            alpha=np.arctan(dx/dy)
            #Vn alongside R
            Vn=-Vx*np.sin(alpha)+Vy*np.cos(alpha)
            #Vt perpendicular to R
            Vt=Vx*np.cos(alpha)+Vy*np.sin(alpha)
            #apply momentum conservation
            Vjn=Vn*2*m2/(m1+m2)
            Vkn=Vn*(m2-m1)/(m1+m2)
            #transform V to x y coordinates
            Vkx=Vt*np.cos(alpha)-Vkn*np.sin(alpha)
            Vjx=-Vjn*np.sin(alpha)
            Vky=Vt*np.sin(alpha)+Vkn*np.cos(alpha)
            Vjy=Vjn*np.cos(alpha)
            #transform velocities back
            vx[t+1,k]=Vkx+vx[t,j]
            vx[t+1,j]=Vjx+vx[t,j]
            vy[t+1,k]=Vky+vy[t,j]
            vy[t+1,j]=Vjy+vy[t,j]
        else:
            vx[t+1,j]=vx[t,j]
            vy[t+1,j]=vy[t,j]
            vx[t+1,k]=vx[t,k]
            vy[t+1,k]=vy[t,k]
    for j in range(0,n):
        #bounce
        if x[t+1,j]<left+r:
            x[t+1,j]=left+r
            vx[t+1,j]=-vx[t+1,j]
        if y[t+1,j]<bottom+r:
            y[t+1,j]=bottom+r
            vy[t+1,j]=-vy[t+1,j]
        if x[t+1,j]>right-r:
            x[t+1,j]=right-r
            vx[t+1,j]=-vx[t+1,j]
        if y[t+1,j]>up-r:
            y[t+1,j]=up-r
            vy[t+1,j]=-vy[t+1,j]
fig=plt.figure(figsize=[5, 5])
ax=plt.axes([0.1,0.1,0.8,0.8],xlim=(left,right),ylim=(bottom,up))
points_whole_ax=5*0.8*72
points_radius=2*r/1.0*points_whole_ax
scat=ax.scatter(x[0],y[0],marker='o',s=points_radius**2)
def animate(i):
    data = np.hstack((x[i,:,np.newaxis], y[i,:,np.newaxis]))
    scat.set_offsets(data)
    return scat,
anim=animation.FuncAnimation(fig,animate,frames=N)
plt.grid()
plt.show()
