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
x=np.zeros([tsteps,N])              #coordinates
x[0]=np.random.uniform(0,L,N)
vx=np.zeros([tsteps,N])             #velocities
Nhalf=int(N/2)
vx[0,0:Nhalf]=np.random.uniform(0,-1,Nhalf)
vx[0,Nhalf:]=np.random.uniform(1,0,N-Nhalf)
