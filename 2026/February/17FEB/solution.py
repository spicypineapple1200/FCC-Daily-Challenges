def check_eligibility(athlete_weights, sled_weight):
    team, team_weight = len(athlete_weights), sum(athlete_weights)+sled_weight
    if team == 4:
        if team_weight > 630 or sled_weight < 210:
            ans = "Not Eligible"
        else: ans = "Eligible"
    elif team == 2:
        if team_weight > 390 or sled_weight < 170:
            ans = "Not Eligible"
        else: ans = "Eligible"    
    elif team == 1:
        if team_weight > 247 or sled_weight < 162:
            ans = "Not Eligible"
        else: ans = "Eligible" 
    print(ans)
    return ans
