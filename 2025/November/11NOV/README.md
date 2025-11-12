*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***For this one i made a list for vowels, one for the regular alphabet, then used if else statements to see what the letters in the word were. Kept count, then returned a list with the numbers.***

****

## [Vowels and Consonants](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-11)
Given a string, return an array with the number of vowels and number of consonants in the string.

Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].

****

    1. count("Hello World") should return [3, 7].
    2. count("JavaScript") should return [3, 7].
    3. count("Python") should return [1, 5].
    4. count("freeCodeCamp") should return [5, 7].
    5. count("Hello, World!") should return [3, 7].
    6. count("The quick brown fox jumps over the lazy dog.") should return [11, 24].
