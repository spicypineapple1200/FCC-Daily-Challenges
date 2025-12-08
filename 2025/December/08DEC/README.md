*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was simple. The math needed for the conversion is provided already. I did the math part of the challenge and stored it in a variable. Then I added conditional statements to account for the words part of the challenge. Finally I created an f string for the answer and plugged everything in as needed. Done!***

****

## [Pounds to Kilograms](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-08)

Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

Replace "(lbs)" with the input number.
Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
1 pound equals 0.453592 kilograms.
If the input is 1, use "pound" instead of "pounds".
If the converted value is 1, use "kilogram" instead of "kilograms".

****

    1. convert_to_kgs(1) should return "1 pound equals 0.45 kilograms.".
    2. convert_to_kgs(0) should return "0 pounds equals 0.00 kilograms.".
    3. convert_to_kgs(100) should return "100 pounds equals 45.36 kilograms.".
    4. convert_to_kgs(2.5) should return "2.5 pounds equals 1.13 kilograms.".
    5. convert_to_kgs(2.20462) should return "2.20462 pounds equals 1.00 kilogram.".
