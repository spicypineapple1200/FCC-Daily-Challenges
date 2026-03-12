*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***My method for solving this is to first establish an initial variable called check that pulls the second number of the first item in the domino list, along with ans as a True Boolean. We iterate through the rest of the domino list, ignoring the first one of course, and check to see if the check does not match the first item of the item. If it does not we change the answer to a False and break the iteration. If it is fine then we continue on and reset check to the second number of the current item for the next iteration. We return the boolean and then we are done.***

****
## [Domino Chain Validator](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-12)

Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.

Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
For the chain to be valid, the second number of each domino must match the first number of the next domino.
The first number of the first domino and the last number of the last domino don't need to match anything.

****
    1. is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]) should return True.
    2. is_valid_domino_chain([[6, 2], [3, 4], [4, 1]]) should return False.
    3. is_valid_domino_chain([[2, 5], [5, 6], [5, 1]]) should return False.
    4. is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]) should return True.
    5. is_valid_domino_chain([[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]]) should return False.
