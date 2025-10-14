def to_12(time):
    part1, part2, part3 = int(time[:2]), time[2:], 'AM'
    if part1 >= 13: 
        part1 = f'{part1-12}'
        part3 = 'PM'
    elif part1 == 0: part1 = '12'
    answer = f'{part1}:{part2} {part3}'
    print(answer)
    return answer
