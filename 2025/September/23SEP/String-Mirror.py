import string

def is_mirror(str1, str2):
    judgement = ''
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    str1 = ''.join((list(reversed([letter for letter in str1 if letter in alphabet]))))
    str2 = ''.join((list([letter for letter in str2 if letter in alphabet])))
    if str1 == str2:judgement = True
    else: judgement = False
    print(judgement)
    # return judgement
