*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Initially I wrote my own code for calculating the LCM and was wasting time bug fixing when it occurred to me that pythons math module probably has tools for this. Indeed it did. I implemented that into the function using the two inputs when the function is called, stored that in a variable, and returned the answer. Easy.***

****

## [LCM](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-21)
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

Multiples of 4 are 4, 8, 12 and so on.
Multplies of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both.

****

    1. lcm(4, 6) should return 12.
    2. lcm(9, 6) should return 18.
    3. lcm(10, 100) should return 100.
    4. lcm(13, 17) should return 221.
    5. lcm(45, 70) should return 630.
