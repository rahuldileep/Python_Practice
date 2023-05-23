def check_if_sum_possible(arr, k):
    if not arr:
        return False
    def helper(so_far,i,atleast_one):
        if i == len(arr):
            return so_far == k and atleast_one==True
        return helper(so_far+arr[i],i+1, True) or helper(so_far,i+1, atleast_one)
    return helper(0,0,False)

print(check_if_sum_possible([1,2,3,4,5],0))