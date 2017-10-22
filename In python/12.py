
def divisor(n):
    div = []
    for i in range (1,n+1):
        if (n%i==0):
            div.append(i)
    # print(div)
    if (len(div) == 10):
        return True
    else:
        return False

def main():
    flag = 0
    for i in range (1,100):
        flag = flag + i
        print(flag)
        if (divisor(flag) is True):
            print(flag)
            break
        # else:
            # print("bad")

if __name__ == '__main__':
    main()

# Every thing is working correctly.
# The values are different
