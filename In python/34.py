# Find the sum of all numbers which are equal to the sum of the factorial of their digits.


import math

def factorial_sum(num):
    sum_ = 0
    flag= num
    for i in str(num):
        remain = int(flag % 10)
        sum_ += math.factorial(remain)
        flag = int(flag / 10)

    if (sum_ == num):
        return True

def main():
    add = 0
    for i in range(3,10000000):
        if(factorial_sum(i) is True):
            add += i
    print(add)

if __name__ == '__main__':
    main()
