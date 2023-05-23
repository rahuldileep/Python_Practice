def quicksort(A,first,last):
    if first<last:
        p=partition(A,first,last)
        quicksort(A,first,p-1)
        quicksort(A,p+1,last)
    return A
def partition(A,first,last):
    pivot=A[last]
    pindex=first
    for i in range(first,last):
        if A[i]<pivot:
            swap(A,i,pindex)
            pindex+=1
    swap(A,pindex,last)
    return pindex 
def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
print(quicksort([5,3,4,2,1,0],0,5))
