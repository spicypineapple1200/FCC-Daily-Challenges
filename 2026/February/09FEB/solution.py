def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    other = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]
    other.sort(reverse=True)
    mine = distance_points + style_points + wind_comp + k_point_bonus
    place, placement = 0, ["Gold", "Silver", "Bronze", "No Medal"]
    for item in other:
        if item > mine:
            place+=1
            if place > 3: place=3
        else: ans = placement[place]
    print(ans)
    return ans
