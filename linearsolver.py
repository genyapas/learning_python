import numpy as np
M=10
eps=1e-12
sumax=np.zeros([M+1])
a=np.zeros([M+1,M+1])
x=np.zeros([M+1])
#b=np.zeros([M+1])
b=np.random.uniform(-1,1,M+1)
for i in range(0,M+1):
	a[i,i]=-2
	if i!=M:
		a[i,i+1]=1
		a[i+1,i]=1
#a[0,M]=1
#a[M,0]=1
x=np.linalg.solve(a,b)
#print(x)
for i in range(M+1):
	for j in range(M+1):
		sumax[i]=sumax[i]+a[i,j]*x[j]	
	print(sumax[i],b[i])
	if abs(sumax[i]-b[i])>eps:
		print('wrong solution')
		quit()
