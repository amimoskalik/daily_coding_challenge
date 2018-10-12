"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def test(k, arr):
    processed = set()

    for num in arr:
        if k-num in processed:
            return True
        processed.add(num)
    return False


assert test(17, [10, 15, 3, 7])
assert not test(10, [5, 15, 4, 7])
assert test(20, [10, 10, 3, 7])
assert test(0, [0, 15, 3, 7, 0])
