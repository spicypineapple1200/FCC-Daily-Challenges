import string

def wise_speak(sentence):
    catch_words = ["have", "must", "are", "will", "can"]
    punctuations = string.punctuation
    for i in sentence:
        if i in punctuations:the_punct = i
    sentence = sentence.replace(the_punct, "").strip()
    sent = sentence.split(' ')
    for word in sent:
        if word in catch_words:index = (sent.index(word))+1
    part1, part2 = sent[index:], sent[:index]
    answer = f'{part1[0].title()} '
    for i in part1[1:]:
        answer+=f'{i}'
        if i == part1[-1]:answer+=','
        else:answer+=' '
    answer+=' '
    for i in part2:
        answer+=i.lower()
        if i == part2[-1]:answer+=the_punct
        else:answer+=' '
    print(answer)
    return answer
