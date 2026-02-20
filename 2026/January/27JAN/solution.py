import time

def odd_or_even_day(timestamp):
    seconds = timestamp / 1000
    day = time.gmtime(seconds).tm_mday
    ans = "even" if day%2 == 0 else "odd"
    print(ans)
    return ans
