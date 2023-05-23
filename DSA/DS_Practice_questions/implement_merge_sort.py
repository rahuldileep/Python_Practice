def merge_sort(arr):
    # Write your code here
    n = len(arr)-1
    return merge_helper(0,n,arr)
    
def merge_helper(start,end,nums):
    if start>=end:
        return nums
    mid = start + (end-start)//2
    merge_helper(start,mid,nums)
    merge_helper(mid+1,end,nums)
    aux = []
    i,j = start,mid+1
    while i<=mid and j<=end:
        if nums[i] < nums[j]:
            aux.append(nums[i])
            i += 1
        else:
            aux.append(nums[j])
            j += 1
    while i<=mid:
        aux.append(nums[i])
        i += 1
    while j<=end:
        aux.append(nums[j])
        j += 1
    nums[start:end+1] = aux
    return nums
    



nums = [1,1]
merge_sort(nums)
print(nums)