def calculate_penalty_distance(rounds):
    ans = 0
    for shots in rounds:
        ans+=((5-shots)*150)
    print(ans)
    return ans
