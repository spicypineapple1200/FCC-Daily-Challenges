import math

def count_perfect_cubes(a, b):
    ans = 0
    nums = [abs(item) for item in range(a if a<b else b, a+1 if a>b else b+1)]
    for n in nums:
        check = (round(n ** (1/3)))**3
        if check == n: ans+=1
    print(ans)
    return ans
