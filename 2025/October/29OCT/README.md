*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This one was especially challenging for me, but got it working! I had to learn some new tricks for using pythons "sorting" function, as well as get creative with tracking the domains and user names. Long story short I sorted the domains, sorted the names by the domain name, then went in order adding the emails to the final answer and had to make sure none were repeatedly added in the wrong order.***

****

## Email Sorter

On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are billions of email addresses.

In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the @), and username second (the part before the @).

Sorting should be case-insensitive.
If more than one email has the same domain, sort them by their username.
Return an array of the sorted addresses.
Returned addresses should retain their original case.
For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com", "john@example.com", "jill@mail.com"].

****

    1. sort(["jill@mail.com", "john@example.com", "jane@example.com"]) should return ["jane@example.com", "john@example.com", "jill@mail.com"].
    2. sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"]) should return ["bob@mail.com", "carol@mail.com", "alice@zoo.com"].
    3. sort(["user@z.com", "user@y.com", "user@x.com"]) should return ["user@x.com", "user@y.com", "user@z.com"].
    4. sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]) should return ["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"].
    5. sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]) should return ["SAM@ALPHA.com", "sammy@alpha.com", "sara@alpha.com", "Sarah@Alpha.com", "simon@beta.com", "Simone@Beta.com"].
