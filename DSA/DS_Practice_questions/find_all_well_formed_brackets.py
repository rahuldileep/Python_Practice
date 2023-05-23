def find_all_well_formed_brackets(n):
    res = []
    def helper(slate,left,right):
        if left>right:
            return
        if left ==0 and right==0:
            res.append(slate)
        elif left ==0:
            helper(slate+')',left,right-1)
        else:
            helper(slate+'(',left-1,right)
            helper(slate+')',left,right-1)
    helper("",n,n)
    return res
print(find_all_well_formed_brackets(0))