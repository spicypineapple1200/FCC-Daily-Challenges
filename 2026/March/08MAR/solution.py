def is_valid_hsl(hsl):
    ans = False
    mapping = str.maketrans({" ": "", "h": "", "s": "", "l": "", "(": "", ")": "", ";": ""})
    values = hsl.translate(mapping)
    values = values.split(",")
    h, s, l = int(values[0]), values[1], values[2]
    nums100 = [num for num in range(101)]
    nums360 = [num for num in range(361)]
    if "hsl(" in hsl and h in nums360 and s[-1] == "%" and l[-1] == "%" and int(s[:-1]) in nums100 and int(l[:-1]) in nums100:
        ans = True
    print(ans)
    return ans
