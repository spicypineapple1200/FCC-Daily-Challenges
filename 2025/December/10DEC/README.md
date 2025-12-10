*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was kind of convoluted. In a nutshell, I basically found every term surrounded by the symbols that are supposed to make it bold in markdown. If there were spaces, I ignored it and if so then I continued with the program. Every bit that was surrounded by the symbols is put into a list, checked against the original, and if everything looks good I put together the answer by adding the tags. One easy part of this is I replaced the __ with ** for most of the logic. I just made sure not to lose the original input for use in piecing together the answer.***

****
## [Markdown Bold Parser](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-10)

Given a string that may include some bold text in Markdown, return the equivalent HTML string.

Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
Convert all bold occurrences to HTML b tags and return the string.
For example, given "**This is bold**", return "<b>This is bold</b>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

****
    1. parse_bold("**This is bold**") should return "<b>This is bold</b>".
    2. parse_bold("__This is also bold__") should return "<b>This is also bold</b>".
    3. parse_bold("**This is not bold **") should return "**This is not bold **".
    4. parse_bold("__ This is also not bold__") should return "__ This is also not bold__".
    5. parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog.") should return "The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog.".
