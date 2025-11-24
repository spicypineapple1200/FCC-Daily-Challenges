def is_valid_message(message, validation):
    letters = ''.join([word[0].lower() for word in message.split(" ")])
    validation = validation.lower()
    if letters == validation: answer = True
    else: answer = False
    print(answer)
    return answer
