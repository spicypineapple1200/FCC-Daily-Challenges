def get_movie_night_cost(day, showtime, number_of_tickets):
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
        ]
    ans = 0
    if day in weekdays[4:]: ans+=12
    else: ans+=10
    newtime = int(showtime.split(":")[0])
    if "am" in showtime: pass
    elif "pm" in showtime: newtime+=12
    if newtime<17: ans-=2
    if day == "Tuesday": ans = 5
    ans*=number_of_tickets
    ans = f"${ans}.00"
    print(ans)
    return ans
