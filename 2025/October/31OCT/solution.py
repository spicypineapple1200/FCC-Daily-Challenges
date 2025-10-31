import string
import re

def spookify(boo):
    
    alpha = list(string.ascii_letters)
    
    boo = re.sub("_", "~", boo)
    boo = re.sub("-", "~", boo)
    
    answer = ''
    count = 0
    
    for item in boo:
        if count == 0:
            item = item.upper()
            answer+=item
            capitalize = False
        elif item in alpha and capitalize == False:
            item = item.lower()
            answer+=item
            capitalize = True
        elif item in alpha and capitalize == True:
            item = item.upper()
            answer+=item
            capitalize = False
        else:
            answer+=item
        count+=1
            
    print(answer)
    return answer
