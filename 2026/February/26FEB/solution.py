import string

def count_letters_and_numbers(s):
    letters, alpha = 0, string.ascii_letters
    nums, numbers = 0, [str(num) for num in range(10)]
    print(alpha, numbers)
    for item in s:
        if item in numbers: nums+=1
        elif item in alpha: letters+=1
    if letters==1: l_extra = ""
    else: l_extra = "s"
    if nums==1: n_extra = ""
    else: n_extra = "s"
    ans = f"The string has {letters} letter{l_extra} and {nums} number{n_extra}."
    print(ans)
    return ans
