import string

def count(s):
    s = s.lower()
    vowels_chars = ['a', 'e', 'i', 'o', 'u']
    alpha = string.ascii_lowercase
    vows, cons = 0, 0

    for letter in s:
        if letter in vowels_chars:
            vows+=1
        elif letter in alpha:
            cons+=1
    answer = [vows, cons]
    print(answer)
    return answer
