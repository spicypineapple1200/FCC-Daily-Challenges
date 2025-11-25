*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was very simple. First I created a list. Second, I iterated through a range of the given number, adding one so we can hit the desired number(range 4, for example goes from 0 to 3, we need that 4 so we add one). From here on out I simply wrote if else conditions, skipping zero of course, checking to see if the number was evenly divisible by 3, 5, or 3 and 5, and added code to append the appropriate word to the list. If none of the conditions are met it simply appends the regular number. Done!***

****

## [FizzBuzz](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-25)
Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

3 with "Fizz".
5 with "Buzz".
3 and 5 with "FizzBuzz".

****

    1. fizz_buzz(2) should return [1, 2].
    2. fizz_buzz(4) should return [1, 2, "Fizz", 4].
    3. fizz_buzz(8) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8].
    4. fizz_buzz(20) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"].
    5. fizz_buzz(50) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"].
