*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Solution here was simple. First I checked to make sure the length of the two fingerprints were the same, if they were I then checked to see what percentage of the fingerprints letters were the same. If either of those failed, the answer returns as False. If they both pass, the answer is True. Simple!***

****

## [Fingerprint Test](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-17)
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.

****

    1. is_match("helloworld", "helloworld") should return True.
    2. is_match("helloworld", "helloworlds") should return False.
    3. is_match("helloworld", "jelloworld") should return True.
    4. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog") should return True.
    5. is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog") should return True.
    6. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") should return False.
