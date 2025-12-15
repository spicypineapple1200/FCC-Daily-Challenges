*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was fun. For this one I used list comprehension to apply pythons title() function(uppercases first letter and lowercases the rest) to each item within the given string by splitting the string using a space as a delimiter. I then used pythons .join to pull them all back together and added the space between them all once again to make the sentence look normal again. Easy!***

****
## [Capitalize It](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-14)

Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space.

****
    1. title_case("hello world") should return "Hello World".
    2. title_case("the quick brown fox") should return "The Quick Brown Fox".
    3. title_case("JAVASCRIPT AND PYTHON") should return "Javascript And Python".
    4. title_case("AvOcAdO tOAst fOr brEAkfAst") should return "Avocado Toast For Breakfast".
