def difference(arr1, arr2):
    test_set = arr1+arr2
    answer = []
    for item in test_set:
        if item in arr1 and item in arr2:pass
        else:answer.append(item)
    print(answer)
    return answer
