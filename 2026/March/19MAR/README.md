*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Since every question only comprises two different strings/variables in the lists, we capture those at the beginning. Then we move on to building our own lists. We iterate through the existing lists, then build our lists with the oppose or alternate value. "ans" holds all the lists we are going to make and append, the constantly changing "build" variable holds all of the smaller lists we make and append along the way.***

****
## [Inverted Matrix](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-19)

Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

    [
      ["a", "b"],
      ["a", "a"]
    ]
Return:

    [
      ["b", "a"],
      ["b", "b"]
    ]

****
    1. invert_matrix([["a", "b"], ["a", "a"]]) should return [["b", "a"], ["b", "b"]].
    2. invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]) should return [[0, 1, 0], [0, 0, 0], [1, 0, 1]].
    3. invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]]) should return [["banana", "apple", "apple", "banana"], ["apple", "banana", "banana", "apple"], ["apple", "apple", "apple", "banana"]].
    4. invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]]) should return [[7, 6, 6, 6, 7], [6, 7, 6, 7, 6], [6, 6, 7, 6, 6], [6, 7, 6, 7, 6], [7, 6, 6, 6, 7]].
    5. invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]) should return [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]].
