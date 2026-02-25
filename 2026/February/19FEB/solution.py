def avalanche_risk(snow_depth, slope):
    depth = snow_depth
    if depth == "Shallow": ans = "Safe"
    else:
        if slope == "Gentle": ans = "Safe"
        else: ans = "Risky"
    print(ans)
    return ans
