*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***I got tired of trying to solve this by navigating the lists so since the order never changes, I simply turned the entire thing into a string and pulled out all of the annoying list parentheses. I added logic to detect if they were originally integers or strings, and put them back together into lists with their original data type. Easy.***

****
## [Flatten the Array](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-28)

Given an array that contains nested arrays, return a new array with all values flattened into a single, one-dimensional array. Retain the original order of the items in the arrays.

****
    1. flatten([1, [2, 3], 4]) should return [1, 2, 3, 4].
    2. flatten([5, [4, [3, 2]], 1]) should return [5, 4, 3, 2, 1].
    3. flatten(["A", [[[["B"]]]], "C"]) should return ["A", "B", "C"].
    4. flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]) should return ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"].
    5. flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]) should return ["red","blue","green","yellow","purple","orange","pink","brown"].
