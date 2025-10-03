*Below is the original challenge in freeCodeCamp. After that there is a divider and below that divider is the test cases for the accompanying python file for this challenge. *note, the python file can a return line and a print line at the end. The return line is the only one included in the original answer, the print line was used while building the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".

## P@ssw0rd Str3ngth!

Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

A password is evaluated according to the following rules:

It is at least 8 characters long.
It contains both uppercase and lowercase letters.
It contains at least one number.
It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules.

****

#### 1. check_strength("123456") should return "weak".
#### 2. check_strength("pass!!!") should return "weak".
#### 3. check_strength("Qwerty") should return "weak".
#### 4. check_strength("PASSWORD") should return "weak".
#### 5. check_strength("PASSWORD!") should return "medium".
#### 6. check_strength("PassWord%^!") should return "medium".
#### 7. check_strength("qwerty12345") should return "medium".
#### 8. check_strength("PASSWORD!") should return "medium".
#### 9. check_strength("PASSWORD!") should return "medium".
#### 10. check_strength("S3cur3P@ssw0rd") should return "strong".
#### 11. check_strength("C0d3&Fun!") should return "strong".
