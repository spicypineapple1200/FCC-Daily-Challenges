*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was very simple! The only things that change are the last four of the credit card number and the spacer used, which is either a dash or regular space. I captured both of those into variables and created an f string that plugs them in as needed. Done!***

****

## [Credit Card Masker](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-28)

Given a string of credit card numbers, return a masked version of it using the following constraints:

The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
Replace all numbers, except the last four, with an asterisk (*).
Leave the remaining characters unchanged.
For example, given "4012-8888-8888-1881" return "****-****-****-1881".

****

    1. mask("4012-8888-8888-1881") should return "****-****-****-1881".
    2. mask("5105 1051 0510 5100") should return "**** **** **** 5100".
    3. mask("6011 1111 1111 1117") should return "**** **** **** 1117".
    4. mask("2223-0000-4845-0010") should return "****-****-****-0010".
