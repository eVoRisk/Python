__author__ = 'eVomeR'

isNumber = False

# read the input from console
while isNumber <> True:
    try:
        a = int(raw_input("First Number: "))
        b = int(raw_input("Second Number: "))
        isNumber = True
    except ValueError:
        print "Not a number"

# save old values
_a = a; _b = b

# cmmdc
while a <> b:
    if a > b:
        a -= b
    else:
        b -= a

print "Cmmdc between %d and %d is %d" % (_a, _b, a)

