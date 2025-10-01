def second_largest(arr):
    num = max(arr)
    while num in arr:
        arr.remove(num)
    answer = max(arr)
    print(answer)
    return answer
