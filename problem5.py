'''
Problem 5

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
'''
from __future__ import division
from eulerlib import primes

def smallest_multiple(n):
    x = 1
    for i in range(1, n+1):
        if x % i != 0:
            p = primes(i-1)
            y = i
            for j in p:
                if i % j == 0:
                    y = y/j
            x = x * y
    assert int(x) == 2*2*2*2*3*3*5*7*11*13*17*19
    return str(int(x))

if __name__ == '__main__':
    print(smallest_multiple(20))
