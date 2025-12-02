*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was simple. First I created an empty string for the answer, then created the alphabet all in lowercase. I iterated through the given string and if any letters weren't lowercase, i simply added an underscore along with the lowercase version of the letter. At the end, the new string is returned. Easy!***

****

## [Camel to Snake](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-02)
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).

****

    1. to_snake("helloWorld") should return "hello_world".
    2. to_snake("myVariableName") should return "my_variable_name".
    3. to_snake("freecodecampDailyChallenges") should return "freecodecamp_daily_challenges".
