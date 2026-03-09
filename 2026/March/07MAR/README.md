*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one I did in just two parts. I used pythons split to pull the numbers from all the given variables, then used some simple math and data type manipulation to calculate the new pixels based on the given viewport width and height numbers. F string to get the result formatted properly and done!***

****
## [Element Size](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-07)

Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.

The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.

"vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.

"vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window.

****
    1. get_element_size("1200 x 800", "50vw", "50vh") should return "600 x 400".
    2. get_element_size("320 x 480", "25vw", "50vh") should return "80 x 240".
    3. get_element_size("1000 x 500", "7vw", "3vh") should return "70 x 15".
    4. get_element_size("1920 x 1080", "95vw", "100vh") should return "1824 x 1080".
    5. get_element_size("1200 x 800", "0vw", "0vh") should return "0 x 0".
    6. get_element_size("1440 x 900", "100vw", "114vh") should return "1440 x 1026".
