__author__ = 'eVomeR'

# import only sqrt from math package
from math import sqrt

# prime test function
def isPrime(number):
    for index in range(2, int(sqrt(number)) + 1):
        if number % index == 0:
            return False
    return True

# read the input from console
isNumber = False

while isNumber <> True:
    try:
        number = int(raw_input("Number: "))
        isNumber = True
    except ValueError:
        print "Not a number"

# write the result
if isPrime(number) <> True:
    print "%d is not a prime number" % (number)
else:
    print "%d is a prime number" % (number)

# first N prime numbers
# read the input from console
isNumber = False

while isNumber <> True:
    try:
        n = int(raw_input("N = "))
        isNumber = True
    except ValueError:
        print "Not a number"

print "First %d prime numbers are: " % (n)

prime = 2

while n <> 0:
    if(isPrime(prime) == True):
        n -= 1
        print prime
    prime += 1

