import string

def get_longest_word(sentence):
    alpha = string.ascii_uppercase + string.ascii_lowercase
    my_words = sentence.split(' ')
    max_length = 0
    answer = ''
    for word in my_words:
        if len(word) > max_length:max_length = len(word)
    for word in reversed(my_words):
        if len(word) == max_length:answer = word
    answer = ''.join([i for i in answer if i in alpha])
    print(answer)
    return answer
