*Below is the original challenge in freeCodeCamp. After that there is a divider and below that divider is the test cases for the accompanying python file for this challenge. *note, the python file can a return line and a print line at the end. The return line is the only one included in the original answer, the print line was used while building the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".

## Caught Speeding
Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

If there were no vehicles speeding, return [0, 0].
****

#### 1. speeding([50, 60, 55], 60) should return [0, 0].
#### 2. speeding([58, 50, 60, 55], 55) should return [2, 4].
#### 3. speeding([61, 81, 74, 88, 65, 71, 68], 70) should return [4, 8.5].
#### 4. speeding([100, 105, 95, 102], 100) should return [2, 3.5].
#### 5. speeding([40, 45, 44, 50, 112, 39], 55) should return [1, 57].
