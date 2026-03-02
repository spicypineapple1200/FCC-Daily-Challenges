def is_flat(arr):
    for item in arr:
        if isinstance(item, list):
            ans = False
            break
        else: ans = True
    print(ans)
    return ans
