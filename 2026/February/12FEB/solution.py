def largest_difference(skater1, skater2):
    ans, laptime = 0, 0
    for num in range(len(skater1)):
        diff = round(abs(skater1[num] - skater2[num]), 2)
        if diff > laptime: laptime, ans = diff, num+1
    print(ans)
    return ans
