#  Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

def isprime(num):
    k = 0
    if num == 2:
        return True

    elif num < 2:
        return False

    else:
        for i in range(3,int(num/2)+1):
            if num%i == 0:
                k +=1
        if k==0:
            return True
        else:
            return False

def left(num):
    flag = num
    k = 0

    for i in str(num):

        if (len(str(flag)) == 1):
            if not isprime(flag):
                k += 1

        else:

            flag = int(str(flag)[1:])
            if not isprime(flag):
                k += 1

    if(k==0):
        return True
    else:
        return False

def Right(num):
    flag = num
    k = 0

    for i in str(num):
        flag = int(flag/10)
        if not isprime(flag):
            k += 1

    if(k==0):
        return True
    else:
        return False

def main():
    array = []
    i = 10
    sum_ = 0
    while(len(array) < 12):
        if (isprime(i) is True):
            if(left(i) is True ):
                if( Right(i) is True):
                    sum_ += i
                    array.append(i)
        i += 1

    print(sum_)

if __name__ == '__main__':
    main()

# not Tested
# taking too much time
