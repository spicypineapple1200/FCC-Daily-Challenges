def largest_number(s):
    checks, the_string = ",!?:;", ""
    for item in s:
        if item in checks: the_string+="/"
        else: the_string+=item
    ans = max([float(number) for number in the_string.split("/")])
    print(ans)
    return ans
