*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was fun. I completed this challenge in four steps. First was the creation of the "extras" variable. All this is, is a string with characters we want to avoid that may be in the sentence. Second is restructuring the sentence. In this line of code we use list comprehension to go through every bit in the sentence and keep it only if the bit is not present in the extras. This turns every the sentence into a list where every individual letter is its own item in the list, and we do not want this so we join it all back together into a sentence again. Then we split the sentence apart using the split, and use a space as the separator. Now we have a clean list of all the words! Third is figuring out the length of the words. We use list comprehension again to create a list of the length of each word in sentence in order. We are checking the length so i called this list check. The first number in the check list is the length of the first word in the sentence list, and so on, so we will use them both in the next bit. Finally we use max to get the largest number in the check list, then we use index to get the index of the largest number within the check list. Since we know the positions of the items in the two lists are the same, this index number is the same as the actual word in the sentence list, so we take it all and get the word from the sentence list and store it in a variable called "answer". Challenge complete!***

****

## [Longest Word](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-20)
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.

****

    1. longest_word("The quick red fox") should return "quick".
    2. longest_word("Hello coding challenge.") should return "challenge".
    3. longest_word("Do Try This At Home.") should return "This".
    4. longest_word("This sentence... has commas, ellipses, and an exlamation point!") should return "exlamation".
    5. longest_word("A tie? No way!") should return "tie".
    6. longest_word("Wouldn't you like to know.") should return "Wouldnt".
