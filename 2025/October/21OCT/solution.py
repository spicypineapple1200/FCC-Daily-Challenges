def adjust_thermostat(current_f, target_c):
    converted_f = (target_c*1.8) + 32
    if current_f == converted_f:answer = 'Hold'
    elif current_f < converted_f:answer = f'Heat: {round(converted_f-current_f, 1)} degrees Fahrenheit'
    else:answer = f'Cool: {round(current_f-converted_f, 1)} degrees Fahrenheit'
    print(answer)
    return answer
