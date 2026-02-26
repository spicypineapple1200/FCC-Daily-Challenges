*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***I started this one by creating two lists of the required words. Then I took the given word string, split it using the space as the delimiter, and then wrote a conditional statement checking to see if the words were in the lists or not. We save True or False into the answer variable depending on outcome and return it.***

****
## [2026 Winter Games Day 15: Freestyle Skiing](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-20)

Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.

A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid second words.

The two words will be separated by a single space.
Valid first words:

"Misty"
"Ghost"
"Thunder"
"Solar"
"Sky"
"Phantom"
"Frozen"
"Polar"
Valid second words:

"Twister"
"Icequake"
"Avalanche"
"Vortex"
"Snowstorm"
"Frostbite"
"Blizzard"
"Shadow"


****
    1. is_valid_trick("Polar Vortex") should return True.
    2. is_valid_trick("Solar Icequake") should return True.
    3. is_valid_trick("Thunder Blizzard") should return True.
    4. is_valid_trick("Phantom Frostbite") should return True.
    5. is_valid_trick("Ghost Avalanche") should return True.
    6. is_valid_trick("Snowstorm Shadow") should return False.
    7. is_valid_trick("Solar Sky") should return False.
