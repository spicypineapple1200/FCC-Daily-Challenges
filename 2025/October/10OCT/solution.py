def launch_fuel(payload):
    fuel1 = payload/5
    payload+=fuel1
    fuel_diff = 9999
    while fuel_diff > 1:
        fuel2 = payload/5
        fuel_diff = fuel2 - fuel1
        payload+=fuel_diff
        fuel1 = fuel2
    answer = round(fuel2, 1)
    print(answer)
    return answer
