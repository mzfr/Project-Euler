# sum of all the numbers that cannot be written as sum of two abundant number

def divisor_sum(num):
    sum_ = 0
    flag = num
    for i in range(1,int(flag/2)+1):
        if (flag%i==0):
            sum_ += i
    if(sum_ > num):
        return False
    else:
        return True

def main():
    store = 0
    for i in range (1,28123):
        if (divisor_sum(i) is True):
            store = store + i
    print(store)

if __name__ == '__main__':
    main()

# logical error in this
# sum of the numbers are exceeding
# having problem in figuring out whether sum of 2 abundant number will be an abundant number or not
