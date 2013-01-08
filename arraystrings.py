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

# 1.3
# Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer. NOTE: One or two additional variables are fine.
# An extra copy of the array is not.
def remdupes(s):
    '''Remove dupes

    >>> remdupes('')
    ''
    >>> remdupes('aaaa')
    'a'
    >>> remdupes('abc')
    'abc'
    >>> remdupes('abaa')
    'ab'
    '''
    l = list(s)
    for i in range(len(l)-1, -1, -1):
        for j in range(0, i):
            if l[i] == l[j]:
                del l[i]
                break
    return ''.join(l)

# 1.4
# Write a method to decide if two strings are anagrams or not.
# _ ________________________________________________________
def annagrammaa(s):
    '''Return True if s in an anagram, else False

    >>> annagrammaa('')
    True
    >>> annagrammaa('ab')
    False
    >>> annagrammaa('toot')
    True
    '''
    r = list(s)
    r.reverse()
    r = ''.join(r)
    return s == r

def annagrammaa2(s):
    '''Return True if s in an anagram, else False
    Loop through tediously, no rev this time

    >>> annagrammaa2('')
    True
    >>> annagrammaa2('ab')
    False
    >>> annagrammaa2('toot')
    True
    '''
    n = len(s) - 1
    for i in range(int(len(s)/2)):
        if s[i] != s[n-i]:
            return False

    return True

# 1.5
# Write a method to replace all spaces in a string with ‘%20’.
#    _ __________________________________________________
def replace(s,x,y):
    '''In s, replace all x with y

    >>> replace('moo and more', ' ', '%20')
    'moo%20and%20more'
    >>> replace('', ' ', '%20')
    ''
    '''
    l = list(s)
    for i, c in enumerate(l):
        if c == x:
            l[i] = y
    
    return ''.join(l)

# 1.6
# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate90(m):
    '''Rotate the matrix 90 deg anticlockwise.
    Direction is hardcoded for now, but can be changed quite easily

    >>> rotate90([[1,2,3],[4,5,6],[7,8,9]])
    [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    >>> rotate90([[1,2], [3,4]])
    [[2, 4], [1, 3]]
    >>> rotate90([])
    []
    '''
    n = len(m)
    r = [[None]*len(x) for x in m]

    # Flip rows to columns and reverse the order to achieve the 
    # rotation
    for i in range(n):
        for j in range(n):
            r[n-j-1][i] = m[i][j]
    return r
            
if __name__ == '__main__':
    doctest.testmod()
