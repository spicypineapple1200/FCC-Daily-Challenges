*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was simple. All the math was provided in the problem so I coded it up, then added conditional statements to return vertain color strings based on the adjusted steepness. The most unique part of the code is probably the dictionary portion where I pulled certain numerical values based on their keys which are given at the beginning of the function.***

****
## [2026 Winter Games Day 10: Alpine Skiing](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-15)

Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.

To determine the rating:

Calculate the steepness of the hill by taking the drop divided by the distance.
Then, calculate the adjusted steepness based on the hill type:
"Downhill" multiply steepness by 1.2
"Slalom": multiply steepness by 0.9
"Giant Slalom": multiply steepness by 1.0
Return:

"Green" if the adjusted steepness is less than or equal to 0.1
"Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
"Black" if the adjusted steepness is greater than 0.25

****
    1. get_hill_rating(95, 900, "Slalom") should return "Green".
    2. get_hill_rating(620, 2800, "Downhill") should return "Black".
    3. get_hill_rating(420, 1680, "Giant Slalom") should return "Blue".
    4. get_hill_rating(250, 3000, "Downhill") should return "Green".
    5. get_hill_rating(110, 900, "Slalom") should return "Blue".
    6. get_hill_rating(380, 1500, "Giant Slalom") should return "Black".
