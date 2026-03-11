def can_donate(donor, recipient):
    ans = True
    if donor[-1:] == "+" and recipient[-1:] != "+":
        ans = False
    if "A" in donor and "A" not in recipient:
        ans = False
    if "B" in donor and "B" not in recipient:
        ans = False
    if "AB" in donor and "AB" not in recipient:
        ans = False
    print(ans)
    return ans
