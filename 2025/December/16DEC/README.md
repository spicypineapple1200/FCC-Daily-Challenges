*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***My solution for this one was to create variable for the consonants, upper and lower, as well as the entire alphabet upper and lower. I created a variable to hold the number 0 and simply iterated through the given word. If the letter is not a consonant and is in the alphabet, then we count it. This ignores spaces and all other items as required in the challenge. We then check our number against the target and return true if they match and false if not. Done!***

****
## [Consonant Count](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-16)

Given a string and a target number, determine whether the string contains exactly the target number of consonants.

Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
Ignore digits, punctuation, spaces, and other non-letter characters when counting.

****
    1. has_consonant_count("helloworld", 7) should return True.
    2. has_consonant_count("eieio", 5) should return False.
    3. has_consonant_count("freeCodeCamp Rocks!", 11) should return True.
    4. has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24) should return False.
    5. has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23) should return True.
