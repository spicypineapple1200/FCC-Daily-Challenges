import string

def validate(email):
    
    # Establishing Viable Characters/Alphabet & Answer Variable
    chars = list(string.ascii_letters + '.' + '_' + '-')
    for i in range(10): chars.append(str(i))
    alpha = list(string.ascii_letters)
    answer = True
    
    # Checking if @ sign is present
    if email.count('@') != 1:
        answer = False
    
    # If @ sign is present, we continue with checks
    elif email.count('@') == 1:
        
        # Using the '@' sign, we split email into a part 1 and part 2
        full = email.split('@')
        p1, p2 = full[0], full[1]
        
        # Check part 1, make sure all items in part 1 are present in our character list
        for item in p1: 
            if item not in chars: 
                answer = False
                
        # Make sure part 1 does not start or end with a '.'
        if p1[0] == '.' or p1[-1] == '.': answer = False
        
        # Make sure there is at least one '.' in part 2
        if p2.count('.') < 1: answer = False
        
        # Pull everything behind the last period of the email
        p2dots = p2.split('.')[-1]
        
        # Make sure there are at least 2 alphabet characters present
        if len(p2dots) < 2: answer = False
        for i in p2dots: 
            if i not in alpha: answer = False
        
        # Make sure no double dots are present in part 1 or part 2
        if '..' in p1 or '..' in p2: answer = False

    print(answer)
    return answer
