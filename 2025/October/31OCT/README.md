*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was simple. Definitely made a silly mistake in specifying the first character as the start of the alternating pattern, just to come across that character later in the string and accidentally "restarting" the pattern. Keeping track of a separate "count" variable fixed that.***

****

## SpOoKy~CaSe

Given a string representing a variable name, convert it to "spooky case" using the following constraints:

Replace all underscores (_), and hyphens (-) with a tilde (~).
Capitalize the first letter of the string, and every other letter after that, ignore the tilde character when counting.
For example, given hello_world, return HeLlO~wOrLd.

****

    1. spookify("hello_world") should return "HeLlO~wOrLd".
    2. spookify("Spooky_Case") should return "SpOoKy~CaSe".
    3. spookify("TRICK-or-TREAT") should return "TrIcK~oR~tReAt".
    4. spookify("c_a-n_d-y_-b-o_w_l") should return "C~a~N~d~Y~~b~O~w~L".
    5. spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts") should return "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS".
