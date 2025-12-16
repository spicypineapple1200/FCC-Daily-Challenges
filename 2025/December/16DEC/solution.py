import string

def has_consonant_count(text, target):
    stri = string.ascii_letters
    cons, num = "aeiouAEIOU", 0
    for letter in text:
        if letter not in cons and letter in stri: num+=1
    if num == target: answer = True
    else: answer = False
    print(answer)
    return answer
