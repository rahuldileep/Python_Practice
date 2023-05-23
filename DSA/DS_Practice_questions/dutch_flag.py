def dutch_flag_sort(balls):
    k = len(balls)-1
    i = 0
    j = 0
    while i<=k and j<=k:
        print(i,j,balls)
        if balls[j] == "R":
            balls[i],balls[j] = balls[j], balls[i]
            i += 1
        elif balls[j] == "B":
            balls[j],balls[k] = balls[k], balls[j]
            k -= 1
            j -= 1
        j += 1
        print(i,j,balls)

balls = ['B','R','G']
print(balls)
dutch_flag_sort(balls)
print(balls)