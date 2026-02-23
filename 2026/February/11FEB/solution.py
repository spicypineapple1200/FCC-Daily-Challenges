def compute_score(judge_scores, *penalties):
    judge_scores.sort()
    ans = sum(judge_scores[1:-1])
    for num in penalties:
        ans-=num
    print(ans)
    return ans
