def count(text, parameter):
    length = len(parameter)
    answer = 0
    while parameter in text:
        observed = text[:length]
        if observed == parameter:
            answer+=1
        text = text[1:]
    print(answer)
    return answer
