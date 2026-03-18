*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***For this one I declared two variables, one for a new string and one for the characters we are supposed to use as separaters. First I recreated the given string and replaced all those character with a forward slash. Then I used python split, using the forward slash as a delimiter, as well as list comprehension to turn all number string into floats. This gives me a list of numbers with the desired float data type. Finally I wrap it in pythons max function to get the largest number and we return it. Done.***

****
## [Largest Number](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-18)

Given a string of numbers separated by various punctuation, return the largest number.

The given string will only contain numbers and separators.
Separators can be commas (","), exclamation points ("!"), question marks ("?"), colons (":"), or semi-colons (";").

****
    1. largest_number("1,2") should return 2.
    2. largest_number("4;15:60,26?52!0") should return 60.
    3. largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011") should return -402.
    4. largest_number("12;-50,99.9,49.1!-10.1?88?16") should return 99.9.
