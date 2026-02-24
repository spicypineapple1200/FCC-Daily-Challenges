def get_difficulty(track):
    road, count = track, 0
    while len(road) > 1:
        segment = road[:2]
        if segment == "LR" or segment == "RL":
            count+=15
        elif len(segment) == 2 and segment[1] != "S":
            count+=5
        elif len(segment) == 2 and segment[1] == "S":
            count+=0
        road = road[1:]
    if count <= 100: ans = "Easy"
    elif count < 200: ans = "Medium"
    elif count >= 200: ans = "Hard"
    print(ans)
    return ans
