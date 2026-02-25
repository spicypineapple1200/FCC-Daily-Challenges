*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Used simple math to get the total team number as well as the total weight. Then I created multiple conditional statements in order to filter the resulting numbers according to the parameters given in the problem. Finally we return the final statement.***

****
## [2026 Winter Games Day 12: Bobsled](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-17)

Given an array representing the weights of the athletes on a bobsled team and a number representing the weight of the bobsled, determine whether the team is eligible to race.

The length of the array determines the team size: 1, 2 or 4 person teams.
All given weight values are in kilograms (kg).
The bobsled (sled by itself) must have a minimum weight of:

162 kg for a 1-person team
170 kg for a 2-person team
210 kg for a 4-person team
The total weight of the bobsled (athletes plus sled) must not exceed:

247 kg for a 1-person team
390 kg for a 2-person team
630 kg for a 4-person team
Return "Eligible" if the team meets all the requirements, or "Not Eligible" if the team fails to meet one or more of the requirements.

****
    1. check_eligibility([78], 165) should return "Eligible".
    2. check_eligibility([80], 160) should return "Not Eligible".
    3. check_eligibility([80], 170) should return "Not Eligible".
    4. check_eligibility([85, 90], 170) should return "Eligible".
    5. check_eligibility([85, 95], 168) should return "Not Eligible".
    6. check_eligibility([112, 97], 185) should return "Not Eligible".
    7. check_eligibility([110, 102, 90, 106], 222) should return "Eligible".
    8. check_eligibility([106, 99, 90, 88], 205) should return "Not Eligible".
    9. check_eligibility([106, 99, 103, 96], 227) should return "Not Eligible".
