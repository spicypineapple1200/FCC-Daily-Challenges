*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***For this challenge, I created a list of numbers with list comprehension, used an f string to piece together the beginning character we are looking for, and searched the markdown submitted to us to see if any number combination was present. If not, we return invalid, if so, then we return the answer. The answer is pieced together by extracting and stripping the words we need out of the original input using indexing, split, and strip. We then use an f string to slap on the tags and then return our answer.***

****

## [Markdown Ordered List Item Converter](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-03)
Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

1. Start with zero or more spaces, followed by
2. A number (1 or greater) and a period (.), followed by
3. At least one space, and then
4. The list item text.
5. If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.
****
    For example, given "1. My item", return "<li>My item</li>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

****

    1. convert_list_item("1. My item") should return "<li>My item</li>".
    2. convert_list_item(" 1.  Another item") should return "<li>Another item</li>".
    3. convert_list_item("1 . invalid item") should return "Invalid format".
    4. convert_list_item("2. list item text") should return "<li>list item text</li>".
    5. convert_list_item(". invalid again") should return "Invalid format".
    6. convert_list_item("A. last invalid") should return "Invalid format".
