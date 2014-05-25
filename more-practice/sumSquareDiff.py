# find the difference between the sum of the squares of the first 100 natural numbers and the square of them

sumOfSquares = 0
sumOfN = 0
for n in range(1,101):
	sumOfSquares = (n**2) + sumOfSquares
	sumOfN = n + sumOfN

print (sumOfN**2) - sumOfSquares
