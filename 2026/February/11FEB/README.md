*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Sorted the list, used indexing to capture the list without the first and last items, and used a for loop to subtract pentalties from final number.***

****
## [2026 Winter Games Day 6: Figure Skating](phttps://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-11)

Given an array of judge scores and optional penalties, calculate the final score for a figure skating routine.

The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove the highest and lowest judge scores and sum the remaining 8 scores to get the base score.

Any additional arguments passed to the function are penalties. Subtract all penalties from the base score to get the final score.

****
    1. compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1) should return 64.
    2. compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) should return 80.
    3. compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1) should return 67.
    4. compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0) should return 67.5.
    5. compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5) should return 59.
