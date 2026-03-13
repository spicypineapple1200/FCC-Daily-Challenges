from datetime import datetime

def calculate_parking_fee(park_time, pickup_time):
    fmt = "%H:%M"
    start = datetime.strptime(park_time, fmt)
    end = datetime.strptime(pickup_time, fmt)
    difference = str(end-start)
    time = difference.split(" ")[-1].split(":")[:2]
    price = int(time[0] if time[1] == "00" else int(time[0])+1)*3
    if difference[0] == "-": price+=10
    ans = f"${price}" if price>5 else f"${5}"
    print(ans)
    return ans
