def how_many_BSTs(n):
    def helper(n,count):
        if n==0:
            count += 1
            return count
        return helper(n-1,count) + helper(n-1,count)
    c1 = helper(n,0)
    c2 = helper(n,0)
    print(c1,c2)

how_many_BSTs(3)
