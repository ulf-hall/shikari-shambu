import doctest

# 1. 1 Implement an algorithm to determine if a string has all unique characters. What if you
# can not use additional data structures?
# ___________________________________
def alluniqcharsinstr(s):
    '''Returns True if the given string contains only unique char, False otherwise

    >>> print(alluniqcharsinstr(''))
    True
    >>> print(alluniqcharsinstr('abc'))
    True
    >>> print(alluniqcharsinstr('aab'))
    False
    '''
    return len(s) == len(list(set(s)))

def alluniqcharsinstr2(s):
    '''Returns True if the given string contains only unique char, False otherwise
    This version does not use the set

    >>> print(alluniqcharsinstr2(''))
    True
    >>> print(alluniqcharsinstr2('abc'))
    True
    >>> print(alluniqcharsinstr2('aab'))
    False
    '''
    d = {}
    for c in s:
        if d.get(c, 0) == 0:
            d[c] = 1
        else:
            return False

   # Found nothing so far
    return True

def alluniqcharsinstr3(s):
    '''Returns True if the given string contains only unique char, False otherwise
    No other data structures are use

    >>> print(alluniqcharsinstr2(''))
    True
    >>> print(alluniqcharsinstr2('abc'))
    True
    >>> print(alluniqcharsinstr2('aab'))
    False
    '''
    r = sorted(s)
    prev = ''
    for c in r:
        if c == prev:
            return False
        prev = c
    return True


if __name__ == '__main__':
    doctest.testmod()
