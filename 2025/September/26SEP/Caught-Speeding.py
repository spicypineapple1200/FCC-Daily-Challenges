def speeding(speeds, limit):
    speeders = 0
    average, answer = [], []
    if max(speeds) <= limit: answer = [0, 0]
    else:
        for speed in speeds:
            if speed > limit:
                speeders+=1
                average.append(speed)
        answer.append(speeders)
        average = [i-limit for i in average]
        answer.append(sum(average)/len(average))
        if str(answer[1])[1:] == '.0':
            x = answer[1]
            answer.pop()
            answer.append(int(x))
    print(answer)
    return answer
