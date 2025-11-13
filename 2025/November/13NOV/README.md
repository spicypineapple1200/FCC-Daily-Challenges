*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Solution for this one involved simply pulling the item from the back of the list to the front, or vice versa, for the count of n that is given to us in the function. For the reverse i multiplied n by -1 to make it positive for the purpose of using the range function properly. Easy!***

****

## [Array Shift](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-13)
Given an array and an integer representing how many positions to shift the array, return the shifted array.

A positive integer shifts the array to the left.
A negative integer shifts the array to the right.
The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].

****

    1. shift_array([1, 2, 3], 1) should return [2, 3, 1].
    2. shift_array([1, 2, 3], -1) should return [3, 1, 2].
    3. shift_array(["alpha", "bravo", "charlie"], 5) should return ["charlie", "alpha", "bravo"].
    4. shift_array(["alpha", "bravo", "charlie"], -11) should return ["bravo", "charlie", "alpha"].
    5. shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15) should return [5, 6, 7, 8, 9, 0, 1, 2, 3, 4].
