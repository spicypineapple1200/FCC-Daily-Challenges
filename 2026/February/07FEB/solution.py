from itertools import cycle

def get_landing_stance(start_stance, rotation):
    calc = abs(0 + rotation) // 180
    options = ["Regular", "Goofy"]
    current_index = options.index(start_stance)
    for _ in range(calc):
        current_index = (current_index + 1) % len(options)
    ans = options[current_index]
    print(ans)
    return ans
