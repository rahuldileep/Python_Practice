def generate_all_expressions(s, target):
    if not s:
        return []
			
    num_len = len(s)
    res = []
    
    def dfs(idx, path):
        if idx == num_len - 1:
            # num_len - 1 to prevent situations like (1+2+) or (1*3*) etc..
            path = path + s[idx] 
            if eval(path) == target:
                res.append(path)
            return
        
        dfs(idx+1, path + s[idx] + "+") 
        dfs(idx+1, path + s[idx] + "*")
        if (path and path[-1] not in ['+','*'] and s[idx] == '0') or s[idx] != '0':
            
            # Prevent cases such as (2+05) which cannot be evaluated using the eval function
            # Cases such as 12+104 should be acceptable, but not 121+04
            
            dfs(idx+1, path + s[idx])
        
    dfs(0, "")
    return res

print(generate_all_expressions("050505",5))

# 0+5+0+5*0*5
# 0+5+0*5+0*5
# 0+5+0*5*0*5
# 0+5+0*5*05
# 0+5+0*50*5
# 0+5+0*505
# 0+5*0+5+0*5
# 0+5*0+5*0+5
# 0+5*0*5+0+5
# 0+5*0*5*0+5
# 0+5*0*5+05
# 0+5*0*50+5
# 0+5+05*0*5
# 0+5*05*0+5
# 0*5+0+5+0*5
# 0*5+0+5*0+5
# 0*5+0*5+0+5
# 0*5+0*5*0+5
# 0*5+0*5+05
# 0*5+0*50+5
# 0*5*0+5+0*5
# 0*5*0+5*0+5
# 0*5*0*5+0+5
# 0*5*0*5*0+5
# 0*5*0*5+05
# 0*5*0*50+5
# 0*5+05+0*5
# 0*5+05*0+5
# 0*5*05+0+5
# 0*5*05*0+5
# 0*5*05+05
# 0*5*050+5
# 0+50*5*0+5
# 0*50+5+0*5
# 0*50+5*0+5
# 0*50*5+0+5
# 0*50*5*0+5
# 0*50*5+05
# 0*50*50+5
# 0+505*0+5
# 0*505+0+5
# 0*505*0+5
# 0*505+05
# 0*5050+5
# 05+0+5*0*5
# 05+0*5+0*5
# 05+0*5*0*5
# 05+0*5*05
# 05+0*50*5
# 05+0*505
# 05*0+5+0*5
# 05*0+5*0+5
# 05*0*5+0+5
# 05*0*5*0+5
# 05*0*5+05
# 05*0*50+5
# 05+05*0*5
# 05*05*0+5
# 050*5*0+5
# 0505*0+5