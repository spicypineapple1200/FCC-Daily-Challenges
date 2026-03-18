*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***First I create a list with all the options plus the numbers associated with them. Next I iterate through all the items and I use code to get two numbers, the current num limit and the limit for the next item, if it is the last item then we use a high number. Finally we see if our number is between or including the two and if it is, we return that status.***

****
## [Anniversary Milestones](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-17)

Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:

Years Married	Milestone
1	"Paper"
5	"Wood"
10	"Tin"
25	"Silver"
40	"Ruby"
50	"Gold"
60	"Diamond"
70	"Platinum"
If they haven't reached the first milestone, return "Newlyweds".

****
    1. get_milestone(0) should return "Newlyweds".
    2. get_milestone(1) should return "Paper".
    3. get_milestone(8) should return "Wood".
    4. get_milestone(10) should return "Tin".
    5. get_milestone(26) should return "Silver".
    6. get_milestone(45) should return "Ruby".
    7. get_milestone(50) should return "Gold".
    8. get_milestone(64) should return "Diamond".
    9. get_milestone(71) should return "Platinum".
