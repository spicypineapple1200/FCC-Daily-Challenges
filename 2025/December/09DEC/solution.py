def most_frequent(arr):
    subject = [1, 0]
    for item in arr:
        count = arr.count(item)
        if count > subject[1]:subject = [item, count]
        else:pass
    answer = subject[0]
    print(answer)
    return answer
