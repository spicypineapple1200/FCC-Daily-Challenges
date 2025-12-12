*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was simple. I created a dictionary and put everything from the inventory into it. Next I added everything from the shipment and if the shipment goods were not already in the dictionary to be added to a preexisting item, then i added them as a new item. Finally I created a list and appended everything from the dictionary into it, formatted just right so the answer could be properly returned. Simple!***

****
## [Inventory Update](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-12)

Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
Update items in the inventory by adding the quantity of any matching items from the shipment.
If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
Return inventory in the order it was given with new items at the end in the order they appear in the shipment.
For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]].

****
        1. update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]) should return [[3, "apples"], [8, "bananas"]].
        2. update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]) should return [[3, "apples"], [8, "bananas"], [4, "oranges"]].
        3. update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]) should return [[10, "apples"], [30, "bananas"], [20, "oranges"]].
        4. update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]) should return [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]].
