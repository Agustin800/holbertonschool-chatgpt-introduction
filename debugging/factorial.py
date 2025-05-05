#!/usr/bin/python
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: ./factorial.py <number>"
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError("Number must be non-negative.")
    except ValueError as e:
        print ("Error: {}".format(e))
        sys.exit(1)

f = factorial(num)
print (f)
