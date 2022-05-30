import numpy as np
from scipy.constants import epsilon_0
import matplotlib.pyplot as plt
#import maths
N=40000                             #number particles
M=500                               #mesh points
L=50                                #truba size
n0=1                                #number density
tEnd=50                             #simulation time
dt=1                                #timestep
m=1                                 #mass
a=0.1							#perturbation
addve=3								#additional velocity
tsteps=int(tEnd/dt )                #timesteps
Lapl=np.zeros([M+1,M+1])
phi=np.zeros([M+1])
x=np.zeros([tsteps+1,N])              #coordinates
x[0]=np.random.uniform(0,L,N)
vx=np.zeros([tsteps+1,N])             #velocities
Nhalf=int(N/2)
E=np.zeros([M+1])
phi=np.zeros([M])
vx[0,0:Nhalf]=(-addve)+np.random.uniform(-1,0,Nhalf)
vx[0,Nhalf:]=addve+np.random.uniform(0,1,N-Nhalf)
for i in range(N):
	vx[0,i]=vx[0,i]*(1+a*np.sin(2*np.pi*x[0,i]/L))
#plt.scatter(x[0,0:Nhalf], vx[0,0:Nhalf], c="red", s=0.4, alpha=0.5)
#plt.scatter(x[0,Nhalf:], vx[0,Nhalf:], c="blue", s=0.4, alpha=0.5)
#plt.show()
#quit()
dx=L/M      		    			#deltax
for i in range(0,M+1):
    Lapl[i,i]=-2/dx**2
    if i!=M:
        Lapl[i,i+1]=1/dx**2
        Lapl[i+1,i]=1/dx**2
Lapl[0,M]=1/dx**2
Lapl[M,0]=1/dx**2
for t in range(tsteps):
    n=np.zeros([M+1])		    		#charge density
    for i in range(N):
        nl=int(x[t,i]/dx)
        nr=nl+1
        if nr==(M+1):
            nr=0
        wnl=(x[t,i]-dx*nl)/dx       #weight
        n[nl]=n[nl]+wnl
        wnr=(dx*nr-x[t,i])/dx
        n[nr]=n[nr]+wnr
    for m in range(M):
        n[m]=M-n0/N*n0*n[m]
    phi=np.linalg.solve(Lapl,n)
    for i in range(M):
        E[i]=-(phi[i+1]-phi[i-1])/2*dx
    for p in range(N):
        i=int(x[t,p]/dx)
        wEl=(x[t,p]-dx*i)/dx
        F=E[i]*wEl
        wEr=(dx*i-x[t,p])/dx
        F=F+wEr*E[i+1]
        a=-F/m
        vx[t+1,p]=a*dt+vx[t,p]
        x[t+1,p]=vx[t+1,p]*dt+x[t,p]
        if x[t+1,p]>L:
            x[t+1,p]=x[t+1,p]-L
        if x[t+1,p]<0:
            x[t+1,p]=x[t+1,p]+L
plt.scatter(x[tsteps,0:Nhalf], vx[tsteps,0:Nhalf], c="red", s=0.4, alpha=0.5)
plt.scatter(x[tsteps,Nhalf:], vx[tsteps,Nhalf:], c="blue", s=0.4, alpha=0.5)
plt.show()


