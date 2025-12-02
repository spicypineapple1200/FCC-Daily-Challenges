def compare(word, guess):
    answer = ['-' for item in word]
    
    # Part 1
    for count in range(len(word)):
        if guess[count] == word[count]:answer[count] = '2'
    new_word, new_guess = '', ''
    for count in range(len(answer)):
        if answer[count] == '2':
            new_word+='-'
            new_guess+='-'
        else:
            new_word+=word[count]
            new_guess+=guess[count]
    
    # Part 2
    for count in range(len(new_guess)):
        letter = new_guess[count]
        if letter == '-':pass
        elif letter in new_word:
            word_count = new_word.count(letter)
            guess_count = new_guess[:count].count(letter)
            if guess_count >= word_count:answer[count] = '0'
            else:answer[count] = '1'
        else:answer[count] = '0'
    answer = ''.join(answer)
    print(answer)
    return answer
