*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Created two lists using python string import for upper and lowercase alphabet. Created answer variable equal to zero for us to add to. Created for loop that looks in each string for the letter and if it is present, adds that index plus one. Finally we return the answer integer. Done!***

****
## [Sum the Letters](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-02)

Given a string, return the sum of its letters.

Letters are A-Z in uppercase or lowercase
Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
Uppercase and lowercase letters have the same value.
Ignore all non-letter characters.

****
    1. sum_letters("Hello") should return 52.
    2. sum_letters("freeCodeCamp") should return 94.
    3. sum_letters("The quick brown fox jumps over the lazy dog.") should return 473.
    4. sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.") should return 1681.
    5. sum_letters("</404>") should return 0.
