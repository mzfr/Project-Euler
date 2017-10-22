# Find the largest palindrome made from the product of two 3-digit numbers.

def reverse(num):
    add = 0
    flag = num
    for i in range(len(str(num))):

        add = int(str(add) + str(flag % 10))
        flag = int(flag / 10)

    if (add == num):
        return True
    else:
        return False

def main():
    number = 0
    for i in range (100,1000):
        for j in range (100,1000):
            product = i * j
            if (reverse(product) is True):
                if(product > number):
                    number = product

    print(number)

if __name__ == '__main__':
    main()
