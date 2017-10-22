# Find the sum of the digits in the number 100!

import math

factorial = math.factorial(100)
print(factorial)
sumofnum = 0

# finding the sum of all the digits of number 100!
for i in str(factorial):
    remain  = factorial % 10
    sumofnum = sumofnum + remain
    factorial = factorial / 10
print ('The sum of the digit in the number 100! is ' , sumofnum)

"""problem in sum """
