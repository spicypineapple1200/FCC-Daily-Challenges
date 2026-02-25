import operator

def get_semifinal_matchups(teams):
    teamscores = {}
    for item in teams:
        name = item.split(":")[0]
        setup = item.split(": ")[1].replace("-", "")
        mult, score = "3210", 0
        for num in range(4):
            score+=int(setup[num])*int(mult[num])
        teamscores[name] = score
    teamscores = dict(sorted(teamscores.items(), key=operator.itemgetter(1), reverse=True))
    final = [item for item in teamscores][:4]
    ans = f"The semi-final games will be {final[0]} vs {final[3]} and {final[1]} vs {final[2]}."
    print(ans)
    return ans
