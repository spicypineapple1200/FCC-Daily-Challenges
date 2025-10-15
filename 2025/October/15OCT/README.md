*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***I initially tried using some logic with pythons split element. Deciding iterating through the entire thing was easier and offered more control. I simply set a parameter named "check" to detect when tags begin and end and kept everything that was not within the tags!***

****

## HTML Tag Stripper

Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' should return "Click here".

****

    1. strip_tags('<a href="#">Click here</a>') should return "Click here".
    2. strip_tags('<p class="center">Hello <b>World</b>!</p>') should return "Hello World!".
    3. strip_tags('<img src="cat.jpg" alt="Cat">') should return an empty string ("").
    4. strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') should return sectionsection.
