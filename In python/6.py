sumofnum = 0
sumofsquare  = 0
for i in range (1,101):

    #finding the sum of the square of first 100 natural number
    square  = i*i
    sumofsquare  = sumofsquare + square

   # finding the square of sum of the first 100 natural numbers
    sumofnum  = i + sumofnum
    squareofsum = sumofnum * sumofnum

difference  = sumofsquare - squareofsum
print (difference)
