*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Since the formula is provided in the challenge description, I simply utilized that and compared the converted temp with the original temp. I then took the differences and plugged them into an if/else statement to get the appropriate answers.***

****

## [Thermostat Adjuster 2](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-21)
Given the current temperature of a room in Fahrenheit and a target temperature in Celsius, return a string indicating how to adjust the room temperature based on these constraints:

Return "Heat: X degrees Fahrenheit" if the current temperature is below the target. With X being the number of degrees in Fahrenheit to heat the room to reach the target, rounded to 1 decimal place.
Return "Cool: X degrees Fahrenheit" if the current temperature is above the target. With X being the number of degrees in Fahrenheit to cool the room to reach the target, rounded to 1 decimal place.
Return "Hold" if the current temperature is equal to the target.
To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32 to the result (F = (C * 1.8) + 32).

****

    1. adjust_thermostat(32, 0) should return "Hold".
    2. adjust_thermostat(70, 25) should return "Heat: 7.0 degrees Fahrenheit".
    3. adjust_thermostat(72, 18) should return "Cool: 7.6 degrees Fahrenheit".
    4. adjust_thermostat(212, 100) should return "Hold".
    5. adjust_thermostat(59, 22) should return "Heat: 12.6 degrees Fahrenheit".
