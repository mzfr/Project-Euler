def isprime(num):
    k = 0
    for i in range(1,int(num/2)+1):
        if(num%i==0):
            k += 1
    if (k == 0):
        return True
    else:
        return False

def pandigi(num):
    array = []
    k = 0
    for i in str(num):
        remain = int(num %10)
        if(remain in array):
            k += 1
            break
        else:
            array.append(remain)
            num = int(num/2)
    if(k==0):
        return True
    else:
        return False

def main ():
    num = 0
    i =11
    while(len(str(i))<8):
        if(pandigi(i) is True):
            if(isprime(i) is True):
                if(i>num):
                    num = i
        i += 1
    print(num)

if __name__ == '__main__':
    main()
