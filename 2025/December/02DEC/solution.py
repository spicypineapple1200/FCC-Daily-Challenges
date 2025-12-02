import string

def to_snake(camel):
    answer, lowers = '', string.ascii_lowercase
    for letter in camel:
        if letter in lowers:answer+=letter
        else:answer+=f"_{letter.lower()}"
    print(answer)
    return answer
