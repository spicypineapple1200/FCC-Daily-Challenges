import string

def check_strength(password):
    characters = 0
    char, upper, lower, num, special = False, False, False, False, False
    final = []
    answer = ['weak', 'medium', 'strong']
    
    uppers = string.ascii_uppercase
    lowers = string.ascii_lowercase
    nums = [f'{i}' for i in range(10)]
    specials = ['!', '@', '#', '$', '%', '^', '&', '*']

    for item in password:
        characters+=1
        if item in uppers: upper = True
        if item in lowers: lower = True
        if item in nums: num = True
        if item in specials: special = True
    
    if characters>=8: char = True
    final.extend([char, upper, lower, num, special])
    final = [item for item in final if item == True]
    passing_checks = len(final)
    if passing_checks < 3:answer = answer[0]
    elif passing_checks == 5:answer = answer[2]
    else:answer = answer[1]
    print(answer)
    return answer
