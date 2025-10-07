def find_landing_spot(matrix):
    count = len(matrix)
    zero_list = []
    surrounding_sums = []
    for x in range(count):
        for y in range(count):
            item = matrix[x][y]
            surroundings = 0
            if item == 0:
                zero_list.append([x, y])
                try:surroundings+=matrix[x][y-1]
                except:pass
                try:surroundings+=matrix[x][y+1]
                except:pass
                try:surroundings+=matrix[x-1][y]
                except:pass
                try:surroundings+=matrix[x+1][y]
                except:pass
                surrounding_sums.append(surroundings)
    answer = zero_list[surrounding_sums.index(min(surrounding_sums))]
    print(answer)
    return answer
