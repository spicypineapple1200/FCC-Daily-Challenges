*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one took some time as I made a crucial mistake in my logic and had to rewrite it, but I got it done. First I created a string of dashes to match the length of the words. Then in part one I go through and see if the letters match, if they do then those respective dashes are changed into 2's. Then I make a new word and guess to remove the ones that matched! Then in part two we go through the rest of the letters, adding ones and twos as per the rules in the challenge. To add 1s properly, I added logic to keep count of how often letters were used. If that usage in the guess word went over or equal to the number of times that letter appears in the secret word, then we add a 0, else we add a 1. Done!***

****

## [Word Guesser](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-28)
Given two strings of the same length, a secret word and a guess, compare the guess to the secret word using the following rules:

The secret word and guess will only consist of uppercase letters ("A" to "Z");
For each letter in the guess, replace it with a number according to how it matches the secret word:
"2" if the letter is in the secret word and in the correct position.
"1" if the letter is in the secret word but in the wrong position.
"0" if the letter is not in the secret word.
Each letter in the secret word can be used at most once.
Exact matches ("2") are assigned first, then partial matches ("1") are assigned from left to right for remaining letters.
If a letter occurs multiple times in the guess, it can only match as many times as it appears in the secret word.
For example, given a secret word of "APPLE" and a guess of "POPPA", return "10201":

The first "P" is not in the correct location ("1"), the "O" isn't in the secret word ("0"), the second "P" is in the correct location ("2"), the third "P" is a zero ("0") because the two "P"'s in the secret word have been used, and the "A" is not in the correct location ("1").

****

    1. compare("APPLE", "POPPA") should return "10201".
    2. compare("REACT", "TRACE") should return "11221".
    3. compare("DEBUGS", "PYTHON") should return "000000".
    4. compare("JAVASCRIPT", "TYPESCRIPT") should return "0000222222".
    5. compare("ORANGE", "ROUNDS") should return "110200".
    6. compare("WIRELESS", "ETHERNET") should return "10021000".
