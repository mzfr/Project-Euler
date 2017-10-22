 # Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import math

def compute(num):
    add = 0
    flag = num
    for i in str(flag):
        remain = flag %10
        power = math.pow(remain,5)
        add = add + power
        flag = int(flag/10)

    if(add == num):
        return True
    else:
        return False

def main():
    sum_ = 0
    for i in range (2,1000000):
        if(compute(i) is True):
            sum_ += i

    print(sum_)

if __name__ == '__main__':
    main()
