import numpy as np
import random
M=20
a=np.zeros([M+1,M+1])
x=np.zeros([M+1])
b=random.uniform(0,1)
for i in range(0,M+1):
	a[i,i]=-2
	a[i,i+1]=1
	a[i+1,i]=1
a[0,M]=1
a[M,0]=1
x=np.linalg.solve(a,b)
print(x)

