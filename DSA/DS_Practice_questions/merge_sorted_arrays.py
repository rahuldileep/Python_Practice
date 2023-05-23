def merger_first_into_second(arr1, arr2):
    #
    # Write your code here.
    #
    n = len(arr1)-1
    i,j = n,n
    write_ptr = len(arr2)-1
    while i >=0 and j >=0:
        if arr1[i] > arr2[j]:
            arr2[write_ptr] = arr1[i]
            i -= 1
        else:
            arr2[write_ptr] = arr2[j]
            j -= 1
        write_ptr -= 1
    while i>=0:
        arr2[write_ptr] = arr1[i]
        i -= 1
        write_ptr -= 1

a1 = [1,3,5]
a2 = [2,4,6,0,0,0]
merger_first_into_second(a1,a2)
print(a2)