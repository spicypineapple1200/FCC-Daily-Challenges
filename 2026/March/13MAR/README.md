*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***First I used datetime to get an object that was the different between the two lists. The end of the object has our required time, the beginning has a number showing if the times overlapped a day or not. The time is used as our basis for getting the price, we add one if leftover time in the hour is present, but overall its multiplied by three to get the price. The price is upped by 10 as per problem instructions if we overlap a day. If the price is below 5 dollars we make sure to set the price to 5 as our minimum. We f string it with a dollar sign and return whatever the final answer is. Done!***

****
## [Parking Fee Calculator](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-13)

Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.

The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is 2pm for example.
The first string will be the time you parked your car, and the second will be the time you picked it up.
If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.
Fee rules:

Each hour parked costs $3.
Partial hours are rounded up to the next full hour.
If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
There is a minimum fee of $5 (only used if the total would be less than $5).
Return the total cost in the format "$cost", "$5" for example.

****
    1. calculate_parking_fee("09:00", "11:00") should return "$6".
    2. calculate_parking_fee("10:00", "10:30") should return "$5".
    3. calculate_parking_fee("08:10", "10:45") should return "$9".
    4. calculate_parking_fee("14:40", "23:10") should return "$27".
    5. calculate_parking_fee("18:15", "01:30") should return "$34".
    6. calculate_parking_fee("11:11", "11:10") should return "$82".
