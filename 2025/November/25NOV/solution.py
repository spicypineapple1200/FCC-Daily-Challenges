def fizz_buzz(n):
    answer = []
    for num in range(n+1):
        if num == 0:
            pass
        elif num%3 == 0 and num%5 == 0:
            answer.append("FizzBuzz")
        elif num%3 == 0:
            answer.append("Fizz")
        elif num%5 == 0:
            answer.append("Buzz")
        else:
            answer.append(num)
    print(answer)
    return answer
