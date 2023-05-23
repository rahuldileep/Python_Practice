def insertion_sort(A):
	for j in range(1,len(A)):
		i = j-1
		nth = A[j]
		while i>=0 and A[i]>nth:
			A[i+1] = A[i]
			i -=1
		A[i+1] = nth
	def recursion(n):
		if n<=1:
			return
		recursion(n-1)
		nth = A[n-1]
		j = n-1
		i = j-1
		while i>=0 and A[i]>nth:
			A[j] = A[j-1]
			i -= 1
			j -= 1
		A[j] = nth
	recursion(len(A))

def merge_sort(A):
	def helper(start,end):
		if start >= end:
			return
		mid = (start+end)//2
		helper(start,mid)
		helper(mid+1,end)
		temp = []
		i,j = start, mid+1
		while i<=mid and j<=end:
			if A[i] <= A[j]:
				temp.append(A[i])
				i += 1
			else:
				temp.append(A[j])
				j += 1
		while i<=mid:
			temp.append(A[i])
			i += 1
		while j <= end:
			temp.append(A[j])
			j += 1
		A[start:end+1] = temp

	helper(0,len(A)-1)

A = [4,2,5,3,1]
insertion_sort(A)
print(A)

A = [4,2,5,3,1]
merge_sort(A)
print(A)