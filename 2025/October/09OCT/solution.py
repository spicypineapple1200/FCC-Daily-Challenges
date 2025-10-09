from datetime import date

def moon_phase(date_string):
    beginning = date(2000, 1, 6)
    parts = [int(i) for i in date_string.split("-")]
    formatted_date = (date(parts[0], parts[1], parts[2]))
    calculated_date = str(formatted_date - beginning)
    days = int(calculated_date.split(" ")[0])%28

    if days < 7: answer = "New"
    elif days <= 14: answer = "Waxing"
    elif days <= 21: answer = "Full"
    else: answer = "Waning"
    
    print(answer)
    return answer
