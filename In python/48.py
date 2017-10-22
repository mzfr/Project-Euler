# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


sum_ = 0
for i in range(1,1001):

    sum_ += pow(i,i)

ans = sum_ % (pow(10,10))
print("the last ten digit of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000 is ", ans)
