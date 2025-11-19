*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one required some creativity. The core of the solution is keeping track of the number of hashes at the beginning of the string and keeping that number to insert in an f string for the answer. Some conditions are included to make sure that the rules set in the challenge are obeyed. The middle part of the answer was where I wrote a bit of complicated code to accomplish in just one line. The variable "mid" nests python string functions to get the middle of the original string, strips away any excess at the beginning or end, and then that middle part is reinserted into the answer. Problem solved! Any conditions not being met result in the "Invalid format" being returned.***

****

## [Markdown Heading Converter](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-19)
Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

Start with zero or more spaces, followed by
1 to 6 hash characters (#) in a row, then
At least one space. And finally,
The heading text.
The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

    For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

****

    1. convert("# My level 1 heading") should return "<h1>My level 1 heading</h1>".
    2. convert("My heading") should return "Invalid format".
    3. convert("##### My level 5 heading") should return "<h5>My level 5 heading</h5>".
    4. convert("#My heading") should return "Invalid format".
    5. convert("  ###  My level 3 heading") should return "<h3>My level 3 heading</h3>".
    6. convert("####### My level 7 heading") should return "Invalid format".
    7. convert("## My #2 heading") should return "<h2>My #2 heading</h2>".
