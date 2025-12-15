*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***For this one, most of the work just involved building the conditional statements as the math is already provided in the challenge. I made used the math to create the "my_speed" variable and renamed the other to "limit" for ease of use. The first condition check if the person is speeding and assigns "Not Speeding" if true. The second adds 5 to the limit variable and checks to see if the person deserves a warning, assigning "Warning" if true. The last assigns "ticket" if they are speeding. Easy!***

****
## [Speed Check](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-15)

Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

1 mile equals 1.60934 kilometers.
If you are travelling less than or equal to the speed limit, return "Not Speeding".
If you are travelling 5 KPH or less over the speed limit, return "Warning".
If you are travelling more than 5 KPH over the speed limit, return "Ticket".

****
    1. speed_check(30, 70) should return "Not Speeding".
    2. speed_check(40, 60) should return "Warning".
    3. speed_check(40, 65) should return "Not Speeding".
    4. speed_check(60, 90) should return "Ticket".
    5. speed_check(65, 100) should return "Warning".
    6. speed_check(88, 40) should return "Ticket".
