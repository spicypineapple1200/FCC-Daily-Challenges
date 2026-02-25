*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one just involved the creation of conditional statements to return the right string, not complicated.***

****
## [2026 Winter Games Day 14: Ski Mountaineering](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-19)

Given the snow depth and slope of a mountain, determine if there's an avalanche risk.

The snow depth values are "Shallow", "Moderate", or "Deep".
Slope values are "Gentle", "Steep", or "Very Steep".
Return "Safe" or "Risky" based on this table:

"Shallow"	"Moderate"	"Deep"
"Gentle"	"Safe"	"Safe"	"Safe"
"Steep"	"Safe"	"Risky"	"Risky"
"Very Steep"	"Safe"	"Risky"	"Risky" 

****
    1. avalanche_risk("Shallow", "Gentle") should return "Safe".
    2. avalanche_risk("Shallow", "Steep") should return "Safe".
    3. avalanche_risk("Shallow", "Very Steep") should return "Safe".
    4. avalanche_risk("Moderate", "Gentle") should return "Safe".
    5. avalanche_risk("Moderate", "Steep") should return "Risky".
    6. avalanche_risk("Moderate", "Very Steep") should return "Risky".
    7. avalanche_risk("Deep", "Gentle") should return "Safe".
    8. avalanche_risk("Deep", "Steep") should return "Risky".
    9. avalanche_risk("Deep", "Very Steep") should return "Risky".
