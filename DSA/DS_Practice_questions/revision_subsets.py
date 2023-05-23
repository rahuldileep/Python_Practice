def subsets(A):
	result = []
	helper(A,"",result)
	return result
def helper(array,slate,result):
	if len(array) == 0:
		result.append(slate)
		return
	helper(array[1:],slate,result)
	helper(array[1:],slate+str(array[0]),result)
	
print(subsets([1,2,3]))


def subsets_2(A):
	result = []
	helper_2(A,0,[],result)
	return result

def helper_2(array,i,slate,result):
	if i == len(array):
		result.append(slate[:])
		return
	helper_2(array,i+1,slate,result)
	slate.append(array[i])
	helper_2(array,i+1,slate,result)
	slate.pop()
	
print(subsets_2([1,2,3]))