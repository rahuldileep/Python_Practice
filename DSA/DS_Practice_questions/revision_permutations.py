
def permutation(slate,array):
	if len(array) == 0:
		print(slate)
		return
	for i in range(len(array)):
		permutation(slate+str(array[i]),array[:i]+array[i+1:])

permutation("",[1,2,3])


def permutation_2(A):
	result = []
	helper(A,0,[],result)
	return result

def helper(array,i,slate,result):
	if i == len(array):
		result.append(slate[:])
		return
	for p in range(i,len(array)):
		array[p],array[i] = array[i],array[p]
		slate.append(array[i])
		helper(array,i+1,slate,result)
		slate.pop()
		array[p],array[i] = array[i],array[p]

print(permutation_2([1,2,3]))