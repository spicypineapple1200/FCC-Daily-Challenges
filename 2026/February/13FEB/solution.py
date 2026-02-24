def get_fastest_speed(times):
    segments = [320, 280, 350, 300, 250]
    x, y = 0, 0
    count = 0
    for time in times:
        final = round(segments[count]/time, 2)
        count+=1
        if final > x:
            x = final
            y = count
    ans = f"The luger's fastest speed was {x} m/s on segment {y}."
    print(ans)
    return ans
