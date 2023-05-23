def bubblesort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    return L
print(bubblesort([4,5,2,3,1,0]))
