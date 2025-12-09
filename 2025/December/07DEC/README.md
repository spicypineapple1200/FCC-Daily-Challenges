*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***First I using the split function to divide everything using spaces as a delimiter. Then I iterated through every word in my newly made word list. I counted how many times the word appeared in the word_list. If more than once than we added the word in an f string along with the number of times it was counted. Another condition checks for this again to make sure the already counted word is not added again. Lastly if the word did not appear numerous times then I simply added the word all by itself.***

****

## [String Compression](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-07)

Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".

    1. compress_string("yes yes yes please") should return "yes(3) please".
    2. compress_string("I have have have apples") should return "I have(3) apples".
    3. compress_string("one one three and to the the the the") should return "one(2) three and to the(4)".
    4. compress_string("route route route route route route tee tee tee tee tee tee") should return "route(6) tee(6)".
