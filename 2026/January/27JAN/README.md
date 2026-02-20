*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Originally solved in datetime, had to rewrite because for some reason the solution just would not work in FCC IDE. Used regular time module and similar math to get and return solution.***

****
## [Odd or Even Day](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-27)

Given a timestamp (number of milliseconds since the Unix epoch), return:

"odd" if the day of the month for that timestamp is odd.
"even" if the day of the month for that timestamp is even.
For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd" because the day number (27) is an odd number.

Note: The timestamp is in milliseconds and you should use the date in the UTC timezone, not in your local time.

****
    1. odd_or_even_day(1769472000000) should return "odd".
    2. odd_or_even_day(1769444440000) should return "even".
    3. odd_or_even_day(6739456780000) should return "odd".
    4. odd_or_even_day(1) should return "odd".
    5. odd_or_even_day(86400000) should return "even".
