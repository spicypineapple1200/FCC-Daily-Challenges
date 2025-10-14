*Below is the original challenge in freeCodeCamp. After that there is a divider and below that divider is the test cases for the accompanying python file for this challenge. *note, the python file has a return line and a print line at the end. The return line is the only one included in the original answer, the print line was used while building the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".

## 24 to 12

Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".

****

#### 1. to_12("1124") should return "11:24 AM".
#### 2. to_12("0900") should return "9:00 AM".
#### 3. to_12("1455") should return "2:55 PM".
#### 4. to_12("2346") should return "11:46 PM".
#### 5. to_12("0030") should return "12:30 AM".
