*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was relatively simple. I checked to ensure a character was not present in both lists, and if it was not then it became a part of the answer. Simple!***

****

## [Symmetric Difference](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-05)
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays.

****

    1. difference([1, 2, 3], [3, 4, 5]) should return [1, 2, 4, 5].
    2. difference(["a", "b"], ["c", "b"]) should return ["a", "c"].
    3. difference([1, "a", 2], [2, "b", "a"]) should return [1, "b"].
    4. difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) should return [2, 4, 6, 8].
