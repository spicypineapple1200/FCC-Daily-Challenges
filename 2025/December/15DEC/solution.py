def speed_check(speed_mph, speed_limit_kph):
    my_speed = round(int(speed_mph * 1.60934), 0)
    limit = speed_limit_kph
    answer = ''
    if my_speed < limit:
        answer = "Not Speeding"
    elif my_speed <= (limit+5):
        answer = "Warning"
    else:
        answer = "Ticket"
    print(answer)
    return answer
