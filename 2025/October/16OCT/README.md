*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Check accompanying "solution.py" file for the logic here. I went step by step with the checks for this one to make sure the solution had decent readability.***

****

## Email Validator
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.

****

    1. validate("a@b.cd") should return True.
    2. validate("hell.-w.rld@example.com") should return True.
    3. validate(".b@sh.rc") should return False.
    4. validate("example@test.c0") should return False.
    5. validate("freecodecamp.org") should return False.
    6. validate("develop.ment_user@c0D!NG.R.CKS") should return True.
    7. validate("hello.@wo.rld") should return False.
    8. validate("hello@world..com") should return False.
    9. validate("git@commit@push.io") should return False.
