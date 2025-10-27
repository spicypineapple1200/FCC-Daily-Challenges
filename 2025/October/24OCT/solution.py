def dive(map, coordinates):
    discovery = map[coordinates[0]][coordinates[1]]
    if discovery =='-': answer = "Empty"
    elif discovery == 'X': answer = "Found"
    elif discovery == 'O': 
        leftovers = map[(coordinates[0]):]
        x = ''
        for item in leftovers:
            for i in item:
                x+=i
        leftovers = x[(coordinates[1]):]
        leftovers = leftovers[1:]
        if "O" in leftovers:answer = "Found"
        else:answer = "Recovered"
    print(answer)
    return answer
