*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This was an interesting one. My solution focuses on keeping track of the pages in a list, then changing another variable called "page_index" that essentially tracks where we are in our navigation. There is logic written in to make sure we do not go out of range as well. Easy!***

****

## [Navigator](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-28)

On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

You always start on the "Home" page, which will not be included in the commands array.
Valid commands are:
"Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
"Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
"Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
For example, given ["Visit About Us", "Back", "Forward"], return "About Us".

****

    1. navigate(["Visit About Us", "Back", "Forward"]) should return "About Us".
    2. navigate(["Forward"]) should return "Home".
    3. navigate(["Back"]) should return "Home".
    4. navigate(["Visit About Us", "Visit Gallery"]) should return "Gallery".
    5. navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]) should return "Home".
    6. navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]) should return "Contact".
    7. navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]) should return "Visit Us".
