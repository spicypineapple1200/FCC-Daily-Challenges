*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***For this one I used list comprehension combined with pythons split and some data manipulation to build a list of just the lengths of each word. Then I used pythons .join to go through and create a string with the list of numbers, separated by spaces, in the form required by the problem to be returned.***

****
## [Word Length Converter](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-11)

Given a string of words, return a new string where each word is replaced by its length.

Words in the given string will be separated by a single space
Keep the spaces in the returned string.
For example, given "hello world", return "5 5".

****
    1. convert_words("hello world") should return "5 5".
    2. convert_words("Thanks and happy coding") should return "6 3 5 6".
    3. convert_words("The quick brown fox jumps over the lazy dog") should return "3 5 5 3 5 4 3 4 3".
    4. convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl") should return "5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4".
