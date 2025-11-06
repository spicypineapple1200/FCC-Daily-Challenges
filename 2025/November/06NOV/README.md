*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Went and did some research for datetime usage. Implementing that, pythons string split and data type manipulation, some list indexing for choosing the weekday, and this one was an easy solve.***

****

## [Weekday Finder](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-06)
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.

****

    1. get_weekday("2025-11-06") should return Thursday.
    2. get_weekday("1999-12-31") should return Friday.
    3. get_weekday("1111-11-11") should return Saturday.
    4. get_weekday("2112-12-21") should return Wednesday.
    5. get_weekday("2345-10-01") should return Monday.
