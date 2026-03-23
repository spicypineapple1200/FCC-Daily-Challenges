*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***To solve this we simply iterate through every letter. First we fix the string by removing all spaces and lowercasing them all. Then we move on to the actual iteration and we create a temporary f string that doubles the chosen letter. We search the string to see if that double is present and if so, we break the iteration and return False, else we return True.***

****
## [No Consecutive Repeats](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-23)

Given a string, determine if it has no repeating characters.

A string has no repeats if it does not have the same character two or more times in a row.

****
    1. has_no_repeats("hi world") should return True.
    2. has_no_repeats("hello world") should return False.
    3. has_no_repeats("abcdefghijklmnopqrstuvwxyz") should return True.
    4. has_no_repeats("freeCodeCamp") should return False.
    5. has_no_repeats("The quick brown fox jumped over the lazy dog.") should return True.
    6. has_no_repeats("Mississippi") should return False.
