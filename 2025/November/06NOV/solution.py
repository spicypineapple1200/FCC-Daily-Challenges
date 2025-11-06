from datetime import datetime

def get_weekday(date_string):
    date_parts = date_string.split('-')
    my_date = datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    answer = weekdays[my_date.weekday()]
    print(answer)
    return answer
