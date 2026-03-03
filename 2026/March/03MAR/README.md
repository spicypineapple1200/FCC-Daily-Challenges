*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***First I created a variable to keep track of our count later. Then I used list comprehension to create a flexible list based on the value of the integers we get passed. We iterate through that list, along with some math I found online to work through finding perfect cubes, and we keep count of the perfect cubes. Finally we return that number!***

****
## [Perfect Cube Count](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-03)

Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

The lower number is not garanteed to be the first argument.
A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27.


****
    1. count_perfect_cubes(3, 30) should return 2.
    2. count_perfect_cubes(1, 30) should return 3.
    3. count_perfect_cubes(30, 0) should return 4.
    4. count_perfect_cubes(-64, 64) should return 9.
    5. count_perfect_cubes(9214, -8127) should return 41.
