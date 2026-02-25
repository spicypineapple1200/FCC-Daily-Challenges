def flatten(arr):
    arr = str(arr).replace("[", "").replace("]", "").replace(",", "")
    if arr[0] == "'":
        arr = arr.replace("'", "")
        ans = [str(item) for item in arr.split(" ")]
    else:
        ans = [int(item) for item in arr.split(" ")]
    print(ans)
    return ans
