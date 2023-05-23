def mcm(i,j):
	if i>=j:
		return 0
	mn = float("inf")
	for k in range(i,j):
		print('divide:',(i,k),(k+1,j))
		print(matrix[i-1],matrix[k],matrix[j])
		temp =  mcm(i,k)+mcm(k+1,j)+ matrix[i-1]*matrix[k]*matrix[j]
		print(i,k,j,'temp',temp)
		mn = min(mn,temp)
		print('mn',temp)
	print('returning mn',mn)
	return mn

matrix = [10,30,5,60]
i,j = 1,len(matrix)-1

print(mcm(i,j))