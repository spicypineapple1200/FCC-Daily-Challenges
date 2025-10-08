import math

def goldilocks_zone(mass):
    luminosity = math.pow(mass, 3.5)
    start_zone = round(math.sqrt(luminosity)*0.95, 2)
    end_zone = round(math.sqrt(luminosity)*1.37, 2)
    answer = [start_zone, end_zone]
    print(answer)
    return answer
