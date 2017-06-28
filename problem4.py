'''
Problem 4

A palindromic number reads the same both ways.
he largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

1. Identify higheset palindromes and check factors
2. Multiply 3 digit numbers together to maximize size and check if palindrome
'''

def compute():
    ans = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            k = i * j
            if list(str(k)) == list(reversed(str(k))) and k > ans:
                ans = k
    return ans

if __name__ == '__main__':
    print(compute())
