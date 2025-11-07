import math

def combinations(cards):
    answer = math.comb(52, cards)
    print(answer)
    return answer
