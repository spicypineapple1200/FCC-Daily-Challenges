*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one simply required some logic to select the right prefix and assign it to a variable. The rest was just putting it all together into an f string to return the answer.***

****

## [Email Signature Generator](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-12)
Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
A-I: Use >> as the prefix.
J-R: Use -- as the prefix.
S-Z: Use :: as the prefix.
A comma and space (, ) should follow the name.
The title and company should follow the comma and space, separated by " at " (with spaces around it).
For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".

****

Passed:1. generate_signature("Quinn Waverly", "Founder and CEO", "TechCo") should return "--Quinn Waverly, Founder and CEO at TechCo".
Passed:2. generate_signature("Alice Reed", "Engineer", "TechCo") should return ">>Alice Reed, Engineer at TechCo".
Passed:3. generate_signature("Tina Vaughn", "Developer", "example.com") should return "::Tina Vaughn, Developer at example.com".
Passed:4. generate_signature("B. B.", "Product Tester", "AcmeCorp") should return ">>B. B., Product Tester at AcmeCorp".
Passed:5. generate_signature("windstorm", "Cloud Architect", "Atmospheronics") should return "::windstorm, Cloud Architect at Atmospheronics".
