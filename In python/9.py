
for i in range (1,999):
    for j in range (1,998):
        two_side = i*i + j*j
        long_side = (1000-i-j)*(1000-i-j)
        if (two_side==long_side):
            print(i,j,(1000-i-j))
            print(i*j*(1000-i-j))
