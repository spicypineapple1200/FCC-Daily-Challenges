import math

def calculate_start_delays(jump_scores):
    best, ans = max(jump_scores), []
    for score in jump_scores:
        ans.append(math.ceil((best-score)*1.5))
    print(ans)
    return ans
