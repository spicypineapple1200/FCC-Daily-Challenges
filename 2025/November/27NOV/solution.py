from datetime import date

def calculate_age(birthday):
    age_date = date(2025, 11, 27)
    d = birthday.split("-")
    birthday = date(int(d[0]), int(d[1]), int(d[2]))
    answer = age_date.year - birthday.year
    if (age_date.month, age_date.day) < (birthday.month, birthday.day):
        answer -= 1
    print(answer)
    return answer
