def convert_to_kgs(lbs):
    kilos = round(lbs*0.453592, 2)
    if kilos == 1.00:kf = "kilogram"
    else: kf = "kilograms"
    if lbs == 1.00:pd = "pound"
    else:pd = "pounds"
    answer = f"{lbs} {pd} equals {kilos:.2f} {kf}."
    print(answer)
    return answer
