*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***According to the problem I crafted a few if/else statements to ensure that the returned boolean was true or False based on if the recipient blood type matched the conditional requirements stemming from the type of the donor. It is initially True, and made false if any of the conditions are not met.***

****
## [Each blood type consists of:](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-23)


A letter: "A", "B", "AB", or "O"
And an Rh factor: "+" or "-"
Blood types will be one of the valid letters followed by an Rh factor. For example, "AB+" and "O-" are valid blood types.

Letter Rules:

"O" can donate to other letter type.
"A" can donate to "A" and "AB".
"B" can donate to "B" and "AB".
"AB" can donate only to "AB".
Rh Rules:

Negative ("-") can donate to both "-" and "+".
Positive ("+") can donate only to "+".
Both letter and Rh rule must pass for a donor to be able to donate to the recipient.

****
    1. can_donate("B+", "B+") should return True.
    2. can_donate("O-", "AB-") should return True.
    3. can_donate("O+", "A-") should return False.
    4. can_donate("A+", "AB+") should return True.
    5. can_donate("A-", "B-") should return False.
    6. can_donate("B-", "AB+") should return True.
    7. can_donate("B-", "A+") should return False.
    8. can_donate("O-", "O+") should return True.
    9. can_donate("O+", "O-") should return False.
    10. can_donate("AB+", "AB-") should return False.
