def mergesort(A):
    n=len(A)
    if n<2:
        return
    else:
        m=n//2
        L=A[:m]
        R=A[m:]
        mergesort(L)
        mergesort(R)
        merge(L,R,A)
    return A
def merge(L,R,A):
    ll=len(L)
    lr=len(R)
    i=j=k=0
    while i<ll and j<lr:
        if L[i]<R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    while i<ll:
        A[k]=L[i]
        i+=1
        k+=1
    while j<lr:
        A[k]=R[j]
        j+=1
        k+=1
print(mergesort([5,2,4,6,1,0,3,7]))

class Solution:
    def sortArray(self, nums):
        if len(nums)<2:
            return 
        else:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            self.sortArray(left)
            self.sortArray(right)
            i,j,k = 0,0,0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
        return nums

obj = Solution()
nums = [5,2,3,1]
print(nums)
obj.sortArray(nums)
print(nums)
