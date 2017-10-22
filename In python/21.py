# Amicable numbers under 10000

def divisor_sum(num):
    sum_ = 0
    for i in range(1,int(num/2+1)):
        if (num%i==0):
            sum_ = sum_ + i
    return sum_

def main():
    ami = 0
    array = []
    for i in range(1,10000):
        sum1 = divisor_sum(i)
        sum2 = divisor_sum(sum1)
        if (sum2 == i):
            array.append(sum2)
            ami = ami + sum1
    print(ami)
    print(array)
if __name__ == '__main__':
    main()

# sum is exceeding
# Everything is correct but still having trouble with answer
# [6,28,220,284,496,1184,1210,2620,2924,5020,5564,6232,6368,8128
