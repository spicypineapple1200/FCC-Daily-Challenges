*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one simply required doing pythons split and index selection to get the answer. If the answer was empty, I returned none as required in the instructions.***

****

## [Extension Extractor](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-10)
Given a string representing a filename, return the extension of the file.

The extension is the part of the filename that comes after the last period (.).
If the filename does not contain a period or ends with a period, return "none".
The extension should be returned as-is, preserving case.

****

    1. get_extension("document.txt") should return "txt".
    2. get_extension("README") should return "none".
    3. get_extension("image.PNG") should return "PNG".
    4. get_extension(".gitignore") should return "gitignore".
    5. get_extension("archive.tar.gz") should return "gz".
    6. get_extension("final.draft.") should return "none".
