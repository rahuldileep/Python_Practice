def generate_palindromic_decompositions(s):
    if not s:
        return []
    def helper(curr_pal, i):
        if i == len(s):
            res.append("|".join(curr_pal))
            return
        for j in range(i+1,len(s)+1):
            sub = s[i:j]
            if sub ==sub[::-1]:
                curr_pal.append(sub)
                helper(curr_pal, j)
                curr_pal.pop()
    helper([],0)
res = []
generate_palindromic_decompositions("abracadabra")
print(res)