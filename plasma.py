import numpy as np
from scipy.constants import epsilon_0
#import maths
N=10000                             #number particles
M=100                               #mesh points
L=50                                #truba size
n0=0                                #number density
tEnd=50                             #simulation time
dt=1                                #timestep
tsteps=int(tEnd/dt )                     #timesteps
Lapl=np.zeros([M+1,M+1])
phi=np.zeros([M+1])
x=np.zeros([tsteps,N])              #coordinates
x[0]=np.random.uniform(0,L,N)
vx=np.zeros([tsteps,N])             #velocities
Nhalf=int(N/2)
vx[0,0:Nhalf]=np.random.uniform(0,-1,Nhalf)
vx[0,Nhalf:]=np.random.uniform(1,0,N-Nhalf)
dx=int(L/M)			    			#delta x
for i in range(0,M+1):
	Lapl[i,i]=-2
    if i!=M:
		Lapl[i,i+1]=1
        Lapl[i+1,i]=1
Lapl[0,M]=1
Lapl[M,0]=1
for t in range(tsteps):
	n=np.zeros([M])		    		#charge density
	for i in range(N):
		nl=int(x[t,i]/dx)
		nr=nl+1
		if nr==(M+1):
			nr=0
		wnl=(x[t,i]-dx*nl)/dx
		n[nl]=n[nl]+wnl
		wnr=(dx*nr-x[t,i])/dx
		n[nr]=n[nr]+wnr
	phi=np.linalg.solve(Lapl,n)
