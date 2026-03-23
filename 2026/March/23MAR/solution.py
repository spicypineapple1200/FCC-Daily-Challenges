def has_no_repeats(s):
    s = s.replace(" ", "").lower()
    for letter in s:
        if f"{letter}{letter}" in s: 
            ans = False
            break
        else: ans = True
    print(ans)
    return ans
