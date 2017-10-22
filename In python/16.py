# What is the sum of the digits of the number 2^1000?

import math
power = math.pow(2,1000)

sumofremain = 0

# adding all the digit of the variable power
for i in range(len(str(power))):
    remain  = power % 10
    sumofremain  = remain + sumofremain
    power  = power / 10
print ('sum of the digits of the number 2^1000 is : ' , sumofremain)
