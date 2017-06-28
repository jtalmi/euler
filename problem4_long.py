'''
Problem 4

A palindromic number reads the same both ways.
he largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

1. Identify higheset palindromes and check factors
2. Multiply 3 digit numbers together to maximize size and check if palindrome
'''
from __future__ import division
import math

def smallest_prime_factor(n):
    i = 2
    while i <= n:
        if n%i == 0:
            break
        i += 1
    return i

def factor(n):
     alist = []
     lcd = 2
     while lcd <= n:
         if n % lcd == 0:
            alist.append(lcd)
            n = int(n/lcd)
         lcd = smallest_prime_factor(n)
     return alist

def is_palindrome(x):
    if list(str(x)) == list(reversed(str(x))):
        return True
    else:
        return False

def number_of_digits(x):
    return len(list(str(x)))

def compute():
    for i in list(reversed(range(100, 1000))):
        palindrome = int(str(i) + "".join(list(reversed(str(i)))))
        if three_digit_factors(palindrome) == True:
            return str(palindrome)

def three_digit_factors(x):
    factors = factor(x)
    length = len(factors)
    if number_of_digits(factors[-1]) > 3:
        return False
    elif number_of_digits(factors[-1]) == 3 and number_of_digits(factors[-2]) == 3 and length > 2:
        return False
    elif number_of_digits(factors[-1]) == 3:
        a = factors[-1]
        b = 1
        for i in range(len(factors)):
            a = a * factors[i]
            if number_of_digits(a) > 3:
                a = a/factors[i]
                for j in factors[i:-1]:
                    b = b * j
                if number_of_digits(b) != 3:
                    break
                else:
                    return True
    else:
        return "Unknown"

if __name__ == '__main__':
    print(compute())
