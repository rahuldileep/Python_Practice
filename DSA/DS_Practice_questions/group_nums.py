def solve(arr):
    k = len(arr)
    i = 0
    while i<k:
    	if arr[i]%2==0:
    		i +=1
    	else:
    		break
    j = i + 1
    while i<k and j<k:
        if arr[j]%2 == 0:
            arr[i],arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    return arr

print(solve([3,4,7,8]))
print(solve([8,4,9,5,2,9,5,7,10]))