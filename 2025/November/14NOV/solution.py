from datetime import date, datetime

def days_until_weekend(date_string):
    d = date_string.split("-")
    year, month, day = int(d[0]), int(d[1]), int(d[2])
    day = date(year, month, day)
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = days[day.weekday()]
    weekend_num = days.index("Saturday")
    day_num = days.index(weekday)
    diff = weekend_num-day_num
    print(diff, weekday)

    if diff == 1:
        answer = f"{diff} day until the weekend."
    elif diff <= 5 and diff > 0:
        answer = f"{diff} days until the weekend."
    elif diff <= 0:
        answer = "It's the weekend!"
    print(answer)
    return answer
