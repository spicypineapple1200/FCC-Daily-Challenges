*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***First I created a list with the months of the year. Next I split the list using the space as a delimiter. Then I used list indexing logic to get the year, month, and day. I used conditional statement to add a 0 to the month and day if needed. Finally I used an f string to pull it all together and return the answer. Done!***

****

## [Date Formatter](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-06)

Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

The given month will be the full English month name. For example: "January", "February", etc.
In the return value, pad the month and day with leading zeros if necessary to ensure two digits.
For example, given "December 6, 2025", return "2025-12-06".

****

    1. format_date("December 6, 2025") should return "2025-12-06".
    2. format_date("January 1, 2000") should return "2000-01-01".
    3. format_date("November 11, 1111") should return "1111-11-11".
    4. format_date("September 7, 512") should return "512-09-07".
    5. format_date("May 4, 1950") should return "1950-05-04".
    6. format_date("February 29, 1992") should return "1992-02-29".
