*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one required some research as my initial solution used the permutations function built into itertools. The last solution made it work too hard for that to work! Instead I found a way to calculate it using math.factorial and returned the answer. I am no math genius, but I found a way!***

****

## [Permutation Count](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-04)
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".

****

    1. count_permutations("abb") should return 3.
    2. count_permutations("abc") should return 6.
    3. count_permutations("racecar") should return 630.
    4. count_permutations("freecodecamp") should return 39916800.
