
def dive(map, coordinates):
    discovery = map[coordinates[0]][coordinates[1]]
    if discovery =='-': answer = "Empty"
    elif discovery == 'X': answer = "Found"
    elif discovery == 'O': 
        full_map = ''
        for section in map:
            for item in section:full_map+=item
        num = 0
        num+=(coordinates[0]+1)
        print(coordinates[0]+1)
        num+=(coordinates[1]+1)+1
        print((coordinates[1]+1)+1)
        print(full_map, full_map[num:])
        if "O" in full_map:answer = "Found"
        else:answer = "Recovered"
    print(answer)

# dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1])
# should return "Recovered".

# dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0])
# should return "Empty".

# dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1])
# should return "Found".

dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0])
# should return "Recovered".
