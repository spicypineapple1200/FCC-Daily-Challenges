*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was a bit complicated. I used mapping and split to get the relevant hsl values into a list. I declared the answer as False by default. Then I used if/else statements, built around the requirements in the problem, to check for various factors and if they all checked out, the answer is changed to True. Of all the techniques I used for this solution, the mapping/translate portion was completely new to me, but it wasn't hard to figure out and it worked great!***

****
## [HSL Validator](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-08)

Given a string, determine whether it is a valid CSS hsl() color value.

A valid HSL value must be in the format "hsl(h, s%, l%)", where:

h (hue) must be a number between 0 and 360 (inclusive).
s (saturation) must be a percentage between 0% and 100%.
l (lightness) must be a percentage between 0% and 100%.
Spaces are only allowed:

After the opening parenthesis
Before and/or after the commas
Before and/or after closing parenthesis
Optionally, the value can end with a semi-colon (";").

For example, "hsl(240, 50%, 50%)" is a valid HSL value.

****
    1. is_valid_hsl("hsl(240, 50%, 50%)") should return True.
    2. is_valid_hsl("hsl( 200 , 50% , 75% )") should return True.
    3. is_valid_hsl("hsl(99,60%,80%);") should return True.
    4. is_valid_hsl("hsl(0, 0%, 0%) ;") should return True.
    5. is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;") should return True.
    6. is_valid_hsl("hsl(361, 50%, 80%)") should return False.
    7. is_valid_hsl("hsl(300, 101%, 70%)") should return False.
    8. is_valid_hsl("hsl(200, 55%, 75)") should return False.
    9. is_valid_hsl("hsl (80, 20%, 10%)") should return False.
