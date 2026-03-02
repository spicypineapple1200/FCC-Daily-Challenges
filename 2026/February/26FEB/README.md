*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Created lists for letters and numbers, iterated through to count how many of each we had, and added a for loop to determine whether the words should have an s or not based on our count. Short and simple explanation!***

****
## [Letter and Number Count](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-26)

Given a string, return a message with the count of how many letters and numbers it contains.

Letters are A-Z and a-z.
Numbers are 0-9.
Ignore all other characters.
Return "The string has X letters and Y numbers.", where "X" is the count of letters and "Y" is the count of numbers. If either count is 1, use the singular form for that item. E.g: "1 letter" instead of "1 letters" and "1 number" instead of "1 numbers".

****
    1. count_letters_and_numbers("helloworld123") should return "The string has 10 letters and 3 numbers.".
    2. count_letters_and_numbers("Catch 22") should return "The string has 5 letters and 2 numbers.".
    3. count_letters_and_numbers("A1!") should return "The string has 1 letter and 1 number.".
    4. count_letters_and_numbers("12345") should return "The string has 0 letters and 5 numbers.".
    5. count_letters_and_numbers("password") should return "The string has 8 letters and 0 numbers.".
