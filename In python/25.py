#  What is the first term in the Fibonacci sequence to contain 1000 digits?

i = 0
a = 0
b = 1
while(len(str(a))<1000 or len(str(b))<1000):
    a = a + b
    b = a + b
    i += 1
print(2*i) #because we are doing two values at once
