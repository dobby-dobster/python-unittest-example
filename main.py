#!/usr/bin/env python

def add(x, y):
    """
    add two integers together and return the total
    """
    sum = x + y
    print('{0} + {1} equals {2}').format(x, y, sum)
    return sum

def multiple(x, y):
    """
    multiple two integers together and return the total
    """
    sum = x * y
    print('{0} * {1} equals {2}').format(x, y, sum)
    return sum

def istrue(var):
    var = True
    print(var)
    return var

if __name__ == '__main__':
    add(1, 2)
    multiple(2, 2)
    istrue(var=False)