*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***This required a bit of googling. I found a method called the "Trial Division" and utilized that to find the prime number to return. A list of the primes is created up to the limit specified in n, but only the last item needed for the answer is used.***

****

## Nth Prime

A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.

****

    1. nth_prime(5) should return 11.
    2. nth_prime(10) should return 29.
    3. nth_prime(16) should return 53.
    4. nth_prime(99) should return 523.
    5. nth_prime(1000) should return 7919.
