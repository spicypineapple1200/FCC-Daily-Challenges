def get_extension(filename):
    answer = ''
    if '.' in filename:
        answer = filename.split('.')[-1]
        if answer == '':answer = 'none'
    else:answer = 'none'
    print(answer)
    return answer
