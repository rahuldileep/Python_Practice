#In how many ways you can select k students out of n 

def C(n,k):
	print(n,k)
	if k==0 or k==n:
		return 1
	else:
		return C(n-1,k) + C(n-1,k-1)
print(C(3,2))

#Enumerate all possible strings of length n
def binary_string(n):
	helper("",n)
def helper(slate,n):
	if n==0:
		print(slate)
	else:
		helper(slate+"0",n-1)
		helper(slate+"1",n-1)
binary_string(3)