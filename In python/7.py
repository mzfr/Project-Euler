# What is the 10,001st prime number?

def isprime(num):
    flag=0
    for i in range(2,int(num/2)):
        if (num%i==0):
            flag = flag+1

    if (flag==0):
        return True
    else:
        return False

def main ():
    array = []
    i=0
    while(len(array)<10001):
        if (isprime(i) is True):
            array.append(i)
        i += 1
    print(array[10000])

if __name__ == '__main__':
    main()
