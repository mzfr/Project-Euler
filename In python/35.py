import math
num = 0
primelist = []

def isprime(test):
    if test == 2:
        primelist.append(2)
        return True

    elif test < 2:
        return False

    else:
        for i in primelist:
            if i > math.sqrt(test):
                break
            elif test%i == 0:
                return False
        primelist.append(test)
        return True

def rotation(n):
    answer = []
    rotation = n
    while not rotation in answer:
        answer.append(rotation)
        rotation = int(str(rotation)[1:] + str(rotation)[0])
        return answer

def main():
    num = 0
    for i in range (2,50):
        valid =True
        for j in rotation(i):
            if not isprime(j):
                valid = False
        if valid:
            num +=1
    print("This is num bro ",num)

if __name__ == '__main__':
    main()
