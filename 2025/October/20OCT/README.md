*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***For this one I used a number of different python tools. Manipulation of data types, string splitting and extraction, f strings, for loops, etc. The math was simple, I just needed the numbers to bounce between strings and floats as needed to do the calculations as well as piece the strings together for the final answer.***

****

## [Tip Calculator](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-20)

Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

Prices will be given in the format: "$N.NN".
Custom tip percents will be given in this format: "25%".
Return amounts in the same "$N.NN" format, rounded to two decimal places.
For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].

****

    1. calculate_tips("$10.00", "25%") should return ["$1.50", "$2.00", "$2.50"].
    2. calculate_tips("$89.67", "26%") should return ["$13.45", "$17.93", "$23.31"].
    3. calculate_tips("$19.85", "9%") should return ["$2.98", "$3.97", "$1.79"].
