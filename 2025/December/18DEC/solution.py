def create_board(dimensions):
    answer, char = [], 'X'
    for count in range(dimensions[0]):
        list = []
        for num in range(dimensions[1]):
            list.append(char)
            if char == 'X':
                char = 'O'
            else:
                char = 'X'
        if list[0] == 'X':
            char = 'O'
        else:
            char = 'X'
        answer.append(list)
    print(answer)
    return answer
