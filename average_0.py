def average(lst):
	return sum(lst)/len(lst)
list_i = []
for i in range(10):
	list_i.append(i)
average = average(list_i)
list_i = [i - average for i in list_i]
average = sum(list_i)/len(list_i)
print(list_i, average)
