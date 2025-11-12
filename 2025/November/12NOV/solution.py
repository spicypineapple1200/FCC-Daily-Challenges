import string

def generate_signature(name, title, company):
    alpha = string.ascii_uppercase
    name_index = alpha.index(name[0].upper())
    if name_index <= 8: prefix = '>>'
    elif name_index <= 17: prefix = '--'
    elif name_index <= 26: prefix = '::'
    answer = f'{prefix}{name}, {title} at {company}'
    print(answer)
    return answer
