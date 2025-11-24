*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was simple. I wrote code to split the string apart, pull the first letter from every word, lowercase it, and then combined the letters together into a variable called "letters". I made sure the validation string was lowercase as well. If they matched, I returned True, and if not, False. Easy!***

****

## [Message Validator](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-24)
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces.

****

    1. is_valid_message("hello world", "hw") should return True.
    2. is_valid_message("ALL CAPITAL LETTERS", "acl") should return True.
    3. is_valid_message("Coding challenge are boring.", "cca") should return False.
    4. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD") should return True.
    5. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT") should return False.
