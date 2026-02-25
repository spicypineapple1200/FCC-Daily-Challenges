def get_hill_rating(drop, distance, hill_type):
    hilltype = {
        "Downhill": 1.2,
        "Slalom": 0.9,
        "Giant Slalom": 1.0
    }
    
    steepness = drop/distance
    adjusted = steepness*(hilltype[hill_type])
    
    if adjusted <= 0.1: ans = "Green"
    elif adjusted >=0.1 and adjusted <= 0.25:
        ans = "Blue"
    else: ans = "Black"
    print(ans)
    return ans
