import math
from collections import Counter

def count_permutations(s):
    length = len(s)
    counts = Counter(s)
    numerator = math.factorial(length)
    denominator = 1
    
    for count in counts.values():
        denominator *= math.factorial(count) 
    
    answer = numerator // denominator
    print(answer)
    return answer
