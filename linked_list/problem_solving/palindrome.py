"""
Palindrome Number

Run
    python3 palindrome.py
Tests
    python3 -m doctest -v palindrome.py
"""
from linked_list import LinkedList, Operations
from functools import singledispatch

def digits_reversed(number):
    """
    Fetching Digits in reversed order
    Complexity : O(N)

    >>> print([d for d in digits_reversed(123456789)])
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    while number:
        yield number%10
        number//=10

def digits(number):
    """
    Fetching Digits in original order
    Complexity : O(N+M) => O(N)

    >>> print([d for d in digits(123456789)])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    all_digits: LinkedList = Operations.ll_from(digits_reversed(number))
    for digit in reversed(all_digits):
        yield digit.data

def two_pointer_loop(container, logic):
    """
    A Two pointer converging inwards loop
    Complexity : O(N/2) => O(N)

    >>> two_pointer_loop([1, 2, 3, 4, 5], lambda _, i, j: print(i,j))
    0 4
    1 3
    2 2

    >>> two_pointer_loop([1, 2, 3, 4], lambda _, i, j: print(i,j))
    0 3
    1 2
    """
    i = 0
    j = len(container)-1

    while i<=j:
        logic(container, i, j)
        i+=1
        j-=1

@singledispatch
def palindrome(value):
    """Default implementation for palindrome.
    
    >>> palindrome(123421)
    False
    >>> palindrome(12321)
    True
    >>> palindrome(123321)
    True

    >>> palindrome('abcdba')
    False
    >>> palindrome('abcba')
    True
    >>> palindrome('abccba')
    True
    """
    raise NotImplementedError(f"No Implementation for Processing generic data of type {type(value)}.")

@palindrome.register(int)
def _(value: int):
    """
    Checks If Number is palindrome
    Complexity O(N)
        - digits_reversed => O(N) --- C1
        - Operations.ll_from => O(N) --- C2
        - two_pointer_loop => O(N) --- C3
        - logic_layer => O(1) --- C4

        C1 + C2 * C3 => C1 + Ck ==> O(N)
    """
    all_digits: LinkedList = Operations.ll_from(digits_reversed(value))
    def logic_layer(container, i, j):
        if container[i].data != container[j].data:
            raise Exception('break')
    
    try:
        two_pointer_loop(all_digits, logic_layer)
    except Exception as e:
        if str(e) == 'break':
            return False
        raise e
    else:
        return True

@palindrome.register(str)
def _(value: str):
    """
    Checks If String is palindrome
    Complexity O(N)
        - Operations.ll_from => O(N)--- C1
        - two_pointer_loop => O(N) --- C2
        - logic_layer => O(1) --- C3

        C1 + C2 * C3 => C1 + Ck ==> O(N)
    """
    all_digits: LinkedList = Operations.ll_from(value)
    def logic_layer(container, i, j):
        if ord(container[i].data) != ord(container[j].data):
            raise Exception('break')
    
    try:
        two_pointer_loop(all_digits, logic_layer)
    except Exception as e:
        if str(e) == 'break':
            return False
        raise e
    else:
        return True

if __name__ == '__main__':
    value = 12421
    is_palindrome = palindrome(value)
    print(f"{value=} {is_palindrome=}")