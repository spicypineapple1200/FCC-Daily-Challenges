def is_match(fingerprint_a, fingerprint_b):
    a, b = fingerprint_a, fingerprint_b
    answer = False
    if len(a) == len(b):
        num = 0
        total = len(a)
        for count in range(len(a)):
            if a[count] == b[count]:
                num+=1
            else:pass
        if (num/total) < 0.90:
            answer = False
        else:
            answer = True
            pass
    else:pass
    print(answer)
    return answer
