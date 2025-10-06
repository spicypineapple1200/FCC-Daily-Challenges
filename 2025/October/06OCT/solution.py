def send_message(route):
    final_trip = route[-1]
    route.pop(-1)
    delays = len(route)
    times = [i/300000 for i in route]
    answer = round(sum(times)+(delays/2)+(final_trip/300000), 4)
    print(answer)
    return answer
