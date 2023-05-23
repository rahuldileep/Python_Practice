def permutation1(arr):
	return helper1("",[],arr)

def helper1(slate,result,arr):
	if not arr:
		result.append(slate)
	else:
		for i in range(len(arr)):
			helper1(slate + arr[i],result,arr[:i]+arr[i+1:])
	return result

print('without repetition',permutation1(["1","2"]))

def permutation2(arr):
	return helper2("",[],arr)

def helper2(slate,result,arr):
	if len(slate) == len(arr):
		result.append(slate)
		return
	else:
		for i in range(len(arr)):
			helper2(slate + arr[i],result,arr)
	return result

print('with repetition',permutation2(["1","2"]))

def permutation3(arr):
	result = []
	for i in range(len(arr)):
		helper3(arr[i],arr,result,len(arr))
	return result

def helper3(main,rem,result,n):
	if len(main) == n:
		result.append(main)
	for i in range(len(rem)):
		helper3(main+rem[i],rem[:i]+rem[i+1:],result,n)
	return result

print('with repetition',permutation3(["1","2"]))