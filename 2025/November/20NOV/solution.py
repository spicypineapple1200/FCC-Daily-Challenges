def longest_word(sentence):
    extras = ',.!\'?'
    sentence = (''.join([bit for bit in sentence if bit not in extras])).split(' ')
    check = [len(word) for word in sentence]
    answer = sentence[check.index(max(check))]
    print(answer)
    return answer
