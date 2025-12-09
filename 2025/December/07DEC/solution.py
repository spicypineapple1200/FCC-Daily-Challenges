def compress_string(sentence):
    word_list = sentence.split(" ")
    answer = ''
    for word in word_list:
        num = word_list.count(word)
        if num > 1 and word not in answer:answer+=f"{word}({num}) "
        elif f"{word}(" in answer:pass
        else:answer+=f'{word} '
    answer = answer.strip()
    print(answer)
    return answer
