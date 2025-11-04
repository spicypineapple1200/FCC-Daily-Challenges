*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was simple! I used a combination of list comprehension, pythons len function, and pythons split function, using a space as the delimiter, to count the number of words. The number pulled from len is returned as the answer. Easy!***

****

## [Word Counter](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-03)

Given a sentence string, return the number of words that are in the sentence.

Words are any sequence of non-space characters and are separated by a single space.

****

    1. count_words("Hello world") should return 2.
    2. count_words("The quick brown fox jumps over the lazy dog.") should return 9.
    3. count_words("I like coding challenges!") should return 4.
    4. count_words("Complete the challenge in JavaScript and Python.") should return 7.
    5. count_words("The missing semi-colon crashed the entire internet.") should return 7.
