def strip_tags(html):
    answer = ''
    check = False
    for item in html:
        if item == '<':check = False
        elif item == '>':
            check = True
            item = ''
        if check == True:answer+=item
        else:pass
    print(answer)
    return answer
