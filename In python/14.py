def check(num):
    if (num % 2 == 0):
        return True
    else:
        return False

def chain(flag):
    array = []
    array.append(flag)

    while(flag != 1):

        if(check(flag) is True):
            flag = flag/2
            array.append(flag)

        else:
            flag = 3*flag + 1
            array.append(flag)
    return array

def main():
    ctrl = 0
    for i in range (1,14):
        if (len(chain(i)) > ctrl):
            ctrl = int(chain(i))
    print(ctrl)

if __name__ == '__main__':
    main()


# Having trouble with int and list thing

