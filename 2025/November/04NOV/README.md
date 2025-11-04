*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Solved this one with an if else statement that checks if the term is present in each image in the images list. Used pythons .lower() to make sure any differences in capitalization are mitigated while checking. Easy!***

****

## [Image Search](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-04)

On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

Given an array of image names and a search term, return an array of image names containing the search term.

Ignore the case when matching the search terms.
Return the images in the same order they appear in the input array.

****

    1. image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog") should return ["dog.png"].
    2. image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun") should return ["Sunset.jpg", "sunflower.jpeg"].
    3. image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG") should return ["Moon.png", "stars.png"].
    4. image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat") should return ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"].
