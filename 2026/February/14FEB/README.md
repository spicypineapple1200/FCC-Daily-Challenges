*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***For this challenge I wrote a while loop that continues to examine the first two letters of the track, and after each examination removes the first letter. It looks at the first two letters to determine what kind of turn/change was made and keeps a running count of the score for the track. Another if/else statement gives the final judgement on whether the track was easy, medium, or hard, based on the points accumulated. That is it!***

****
## [2026 Winter Games Day 9: Skeleton](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-14)

Given a string representing the curves on a skeleton track, determine the difficulty of the track.

The given string will only consist of the letters:

"L" for a left turn
"R" for a right turn
"S" for a straight segment
Each direction change adds 15 points (an "L" followed by an "R" or vice versa).

All other curves add 5 points each (all other "L" or "R" characters).

Straight segments add 0 points.

The difficulty of the track is based on the total score. Return:

"Easy" if the total is 0 - 100
"Medium" if the total is 101-200
"Hard" if the total is over 200

****
    1. get_difficulty("SLSLLSRRLSRLRL") should return "Easy".
    2. get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS") should return "Hard".
    3. get_difficulty("SRRRRLSLLRLRSSRLSRL") should return "Medium".
    4. get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL") should return "Hard".
    5. get_difficulty("SLLSSLRLSLSLRSLSSLRL") should return "Medium".
    6. get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR") should return "Easy".
