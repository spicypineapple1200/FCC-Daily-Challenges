*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Used a combination of datetime module, along with list indexing to get the answer. Some simple math to determine the day and its proximity to the "weekend" was all that was needed for this to work. Answers are chosen based on conditional statement depending on the "diff" variable I created.***

****

## [Is It the Weekend?](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-14)
Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

The weekend starts on Saturday.
If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Make sure the calculation ignores your local timezone.

****

    1. days_until_weekend("2025-11-14") should return "1 day until the weekend.".
    2. days_until_weekend("2025-01-01") should return "3 days until the weekend.".
    3. days_until_weekend("2025-12-06") should return "It's the weekend!".
    4. days_until_weekend("2026-01-27") should return "4 days until the weekend.".
    5. days_until_weekend("2026-09-07") should return "5 days until the weekend.".
    6. days_until_weekend("2026-11-29") should return "It's the weekend!".
