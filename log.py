import numpy as np
def average(lst):
	return sum(lst)/len(lst)
#def amplitude(lst):
#	return max(lst)-min(lst)
list_i = []
for i in range(10):
	list_i.append(i)
average = average(list_i)
list_i = [i - average for i in list_i]
average = sum(list_i)/len(list_i)
amplitude = max(list_i)-min(list_i)
variance_1 = [x / amplitude for x in list_i]
print(variance_1)
#print(list_i, average, variance_1, max(variance_1)-min(variance_1))
variance_1 = [x+1 for x in variance_1]
print(variance_1)
variance_1 = np.log(variance_1)
print(variance_1)