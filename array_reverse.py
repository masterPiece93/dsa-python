"""
Array Reverse
=============

SOLUTION_VERSION = '1.0'
    two pointer approach
    - complexity : O(N/2) ~ O(N)

---

Run
    python3 factorial.py
Tests
    python3 -m doctest -v factorial.py
"""
from typing import Any

SOLUTION_VERSION = '1.0'


def reverse(array: list[Any], start: int = 0, end: int = ...):
    """
    >>> reverse([1, 9, 2, 8, 3, 7])
    [7, 3, 8, 2, 9, 1]

    >>> reverse([1, 9, 2, 8, 3, 7, 4, 6], start=3, end=6)
    [1, 9, 2, 4, 7, 3, 8, 6]

    >>> reverse([], start=3, end=6)
    Traceback (most recent call last):
    ...
    Exception: invalid range specified

    >>> reverse([1, 9, 2, 8, 3, 7, 4, 6], start=-1, end=99)
    [6, 4, 7, 3, 8, 2, 9, 1]
    """

    if SOLUTION_VERSION == '1.0':
        # raw
        # ===
        idx_start = start if 0 <= start < len(array) else 0
        if end is ...:
            idx_end = len(array) - 1
        else:
            idx_end = end if 0 <= end < len(array) else len(array) - 1
        if idx_start >= idx_end:
            raise Exception('invalid range specified')
        
        while idx_start < idx_end:
            array[idx_start], array[idx_end] = array[idx_end], array[idx_start]
            idx_start += 1
            idx_end -= 1

        return array
    
    raise NotImplementedError(f"not implemented")

if __name__ == '__main__':
    SOLUTION_VERSION == '1.0'
    assert reverse([1, 9, 2, 8, 3, 7])==[7, 3, 8, 2, 9, 1]
