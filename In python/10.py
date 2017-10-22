# Find the sum of all the primes below two million.

def isprime(num):
    flag=0
    for i in range(2,int(num/2)):
        if (num%i==0):
            flag = flag+1

    if (flag==0):
        return True
    else:
        return False

def main():
    i = 0
    sum_ = 0
    while(i<200000):
        if(isprime(i) is True):
            sum_ += i
        i += 1
    print(sum_)

if __name__ =='__main__':
    main()



