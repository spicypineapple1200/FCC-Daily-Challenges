*Below is the original challenge in freeCodeCamp. After that there is a divider and below that divider is the test cases for the accompanying python file for this challenge.
*note, the python file can a return line and a print line at the end. The return line is the only one included in the original answer, the print line was used while building the solution in
 the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".

#### String Mirror

Given two strings, determine if the second string is a mirror of the first.

A string is considered a mirror if it contains the same letters in reverse order.
Treat uppercase and lowercase letters as distinct.
Ignore all non-alphabetical characters.

****

###### 1. is_mirror("helloworld", "helloworld") should return False.
is_mirror("helloworld", "helloworld")

###### 2. is_mirror("Hello World", "dlroW olleH") should return True.
is_mirror("Hello World", "dlroW olleH")

###### 3. is_mirror("RaceCar", "raCecaR") should return True.
is_mirror("RaceCar", "raCecaR")

###### 4. is_mirror("RaceCar", "RaceCar") should return False.
is_mirror("RaceCar", "RaceCar")

###### 5. is_mirror("Mirror", "rorrim") should return False.
is_mirror("Mirror", "rorrim")

###### 6. is_mirror("Hello World", "dlroW-olleH") should return True.
is_mirror("Hello World", "dlroW-olleH")

###### 7. is_mirror("Hello World", "!dlroW !olleH") should return True.
is_mirror("Hello World", "!dlroW !olleH")
