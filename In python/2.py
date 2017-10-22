"""
By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""

a = 1
b = 2
add = 0

# Loop to find the fibonacci sequence
for i in range (1,4000000):
    a = a + b
    b = a + b

    if a % 2 == 0 :
        add = add + a
    if b % 2 == 0:
        add = add + b

# Printing the value
print ('The sum of the even-valued term is : ', add)
