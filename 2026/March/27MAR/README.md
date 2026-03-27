*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***First I created a list of weekdays. I then used variound conditional statements to see if the chosen time was on the weekend or not. I checked to see if the time is before 5pm or not. All these statements adjust the price. The last thing we do is see if its a tuesday showing and if so, we reset the price entirely. Finally we adjust for the number of tickets and multiply by that number. Done!***

****
## [Movie Night](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-26)

Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.

The given day will be one of:

"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
"Sunday"
The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".

Return the total cost in the format "$D.CC" using these rules:

Weekend (Friday - Sunday): $12.00 per ticket.
Weekday (Monday - Thursday): $10.00 per ticket.
Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
Tuesdays: all tickets are $5.00 each.

****
    1. get_movie_night_cost("Saturday", "10:00pm", 1) should return "$12.00".
    2. get_movie_night_cost("Sunday", "10:00am", 1) should return "$10.00".
    3. get_movie_night_cost("Tuesday", "7:20pm", 2) should return "$10.00".
    4. get_movie_night_cost("Wednesday", "5:40pm", 3) should return "$30.00".
    5. get_movie_night_cost("Monday", "11:50am", 4) should return "$32.00".
    6. get_movie_night_cost("Friday", "4:30pm", 5) should return "$50.00".
    7. get_movie_night_cost("Tuesday", "11:30am", 1) should return "$5.00".
