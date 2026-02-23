*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Easy math solved this one. I just subtract the number of made shots from the total of 5, and multiply the remainder by 150 since each missed shot is 150. We keep a running total that we add this to and return it at the end.***

****
## [2026 Winter Games Day 3: Biathlon](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-08)

Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.

Each round consists of 5 targets.
Each missed target results in a 150 meter penalty loop.

****
    1. calculate_penalty_distance([4, 4]) should return 300.
    2. calculate_penalty_distance([5, 5]) should return 0.
    3. calculate_penalty_distance([4, 5, 3, 5]) should return 450.
    4. calculate_penalty_distance([5, 4, 5, 5]) should return 150.
    5. calculate_penalty_distance([4, 3, 0, 3]) should return 1500.
