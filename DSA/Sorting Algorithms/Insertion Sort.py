def insertionsort(a):
    for i in range(1,len(a)):
        temp=a[i]
        j=i-1
        while j>=0:
            if a[j]>temp:
                a[j+1]=a[j]
                a[j]=temp
                j=j-1
            else:
                break
    return a
print(insertionsort([4,3,5,2,1,0]))
