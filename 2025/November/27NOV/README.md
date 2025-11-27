*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one took more effort, mainly to learn/navigate using datetime module. I used split/datatype conversion to subtract the dates for the answer. I then compared the dates to see if the persons birthday has passed or not and if it had not, subtracted a year to compensate. That's it!***

****

## [What's My Age Again?](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-27)
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025.

****

    1. calculate_age("2000-11-20") should return 25.
    2. calculate_age("2000-12-01") should return 24.
    3. calculate_age("2014-10-25") should return 11.
    4. calculate_age("1994-01-06") should return 31.
    5. calculate_age("1994-12-14") should return 30.
