import string

def sum_letters(s):
    upper, lower = string.ascii_uppercase, string.ascii_lowercase
    ans = 0
    for letter in s:
        if letter in upper: ans+=((upper.index(letter))+1)
        elif letter in lower: ans+=((lower.index(letter))+1)
    print(ans)
    return ans
