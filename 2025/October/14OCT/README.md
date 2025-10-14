*Below is the original challenge in freeCodeCamp. After that there is a divider and below that divider is the test cases for the accompanying "solution.py" python file for this challenge. *note, the python file has a return line and a print line at the end. The return line is the only one included in the original answer, the print line was used while building the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".

"Originally used text.replace method, which worked for all tests except the last one! Decided that it would be text to check the length of the parameter, then check that number of characters at the beginning of the string to see if they match, then pull the first character away from the string until the parameter is not detected within the string anymore. Worked like a charm!"

## String Count

Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.

****

#### 1. count('abcdefg', 'def') should return 1.
#### 2. count('hello', 'world') should return 0.
#### 3. count('mississippi', 'iss') should return 2.
#### 4. count('she sells seashells by the seashore', 'sh') should return 3.
#### 5. count('101010101010101010101', '101') should return 10.
