def shift_array(arr, n):
    for count in range(n):
        add = arr[0]
        arr.remove(add)
        arr.append(add)
    if n < 0:
        for count in range((n*-1)):
            add = arr[-1]
            arr.insert(0, add)
            arr.pop()
    answer = arr
    print(answer)
    return answer
