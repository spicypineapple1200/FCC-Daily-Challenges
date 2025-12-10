def parse_bold(markdown):
    checks, test = '**', markdown.replace('__', '**')
    answer, answer_list = '', []

    bits = test.split(checks)
    bits = [bit for bit in bits if bit != '']
    captured, bolds = [], []

    for item in bits:
        if item[0] != ' ' and item[-1] != ' ':captured.append(item)
    for item in captured:
        item = '**' + item + '**'
        bolds.append(item)
    final = False
    for item in bolds:
        if item in test:final = True
        else:
            final = False
            break

    if final == False:answer = markdown
    else:
        for item in bits:
            if item in captured:
                item = '<b>' + item + '</b>'
                answer_list.append(item)
            else:answer_list.append(item)
        for item in answer_list:answer+=item
    print(answer)
    return answer
