def is_fizz_buzz(sequence):
    test = []
    for num in range(len(sequence)+1):
        if num == 0:
            pass
        elif num%3 == 0 and num%5 == 0:
            test.append("FizzBuzz")
        elif num%3 == 0:
            test.append("Fizz")
        elif num%5 == 0:
            test.append("Buzz")
        else:
            test.append(num)
    if test == sequence: answer=True
    else: answer=False
    print(answer)
    return answer
