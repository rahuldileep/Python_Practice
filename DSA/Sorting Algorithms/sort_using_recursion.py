def insert(array,temp):
	if not array or array[-1] <= temp:
		array.append(temp)
		return
	else:
		val = array.pop()
		insert(array,temp)
		array.append(val)
		return
def sort(array):
	if not array:
		return
	temp = array.pop()
	sort(array)
	insert(array,temp)

array = [2,3,7,6,4,5]
sort(array)
print(array)