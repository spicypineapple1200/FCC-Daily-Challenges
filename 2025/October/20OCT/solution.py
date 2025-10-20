def calculate_tips(meal_price, custom_tip):
    raw_answers = []
    meal = float(meal_price[1:])
    prices = [0.15, 0.20, (float(custom_tip[:-1]))/100]
    tip1, tip2, tip3 = round(meal*prices[0], 2), round(meal*prices[1], 2), round(meal*prices[2], 2)
    raw_answers.append(tip1)
    raw_answers.append(tip2)
    raw_answers.append(tip3)
    answer = []
    for item in raw_answers:
        dotbit1, dotbit2 = str(item).split('.')[0], str(item).split('.')[1]
        if len(dotbit2) < 2:item = f'${dotbit1}.{dotbit2}0'
        else:item = f'${dotbit1}.{dotbit2}'
        answer.append(item)
    print(answer)
    return answer
