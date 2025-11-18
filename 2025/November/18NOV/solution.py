def one_hundred(chars):
    while len(chars) < 100:chars+=chars
    answer = chars[:100]
    print(answer)
    return answer
