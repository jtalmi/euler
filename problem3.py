'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''
from __future__ import division

def smallest_prime_factor(n):
    i = 2
    while i <= n:
        if n%i == 0:
            break
        i += 1
    return i

def largest_prime(top):
    while True:
        top = int(top/smallest_prime_factor(top))
        if top == smallest_prime_factor(top):
            return str(top)

if __name__ == '__main__':
    print largest_prime(600851475143)
