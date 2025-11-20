def longest_word(sentence):
    no = ',.!\'?'
    sentence = list((''.join([i for i in sentence if i not in no])).split(' '))
    check = [len(word) for word in sentence]
    answer = sentence[check.index(max(check))]
    print(answer)
    return answer
