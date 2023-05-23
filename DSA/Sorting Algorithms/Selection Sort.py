def selectionsort(L):
    for i in range(len(L)-1):
        minindex=i
        for j in range(i+1,len(L)):
            if L[j]<L[minindex]:
                minindex=j
        if minindex!=i:
            L[i],L[minindex]=L[minindex],L[i]
    return L
print(selectionsort([4,2,5,3,1,0]))
            
