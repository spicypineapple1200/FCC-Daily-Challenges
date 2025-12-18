*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***I used two for loops to solve this. The smaller one builds the smaller lists and the larger one makes the larger list to return as an answer. The lists are built using logic that alternates between Xs and Os within the smaller for loop. To make sure the "checkerboard" is built properly, the larger for loop checks to see what the first item in the list was to make sure the next list begins with the opposite character. If the previous began with X, the next will begin with O, and so on.***

****
## [Checkerboard](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-18)

Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

The characters should alternate like a checkerboard.
The top-left cell must always be "X".
For example, given [3, 3], return:

    [
      ["X", "O", "X"],
      ["O", "X", "O"],
      ["X", "O", "X"]
    ]

****
    1. create_board([3, 3]) should return [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]].
    2. create_board([6, 1]) should return [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]].
    3. create_board([2, 10]) should return [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]].
    4. create_board([5, 4]) should return [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]].
