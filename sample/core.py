# -*- coding: utf-8 -*-

def add(a, b):
    """Add two numbers"""

    if((type(a) is bool) and (type(b) is bool)):
        return a or b
    if((type(a) is bool) and not(type(b) is bool)):
        raise TypeError
    if ((type(b) is str) or (type(a) is str)):
        a = str(a)
        b = str(b)
    return a + b

if __name__ == "__main__":
    add(1,2)