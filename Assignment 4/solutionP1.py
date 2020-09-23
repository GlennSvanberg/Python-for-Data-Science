"""
Consider a list of characters which are sorted in an increasing order. Each character is duplicated except one which corresponds to the non-duplicate character in the list.

Example 1:

Input list: ['a','a','b','b','c','d','d','e','e','r','r']

Non-duplicate: c

Example 2:

Input list: ['a','c','c','d','d','f','f','z','z']

Non-duplicate: a

Write a program that finds non-duplicate character based on the divide and conquer approach.
Please use solutionP1.py
Preview the document as a starting point by implementing the body of the function findNonDuplicate
which takes a sorted list of character as an input and returns the non-duplicate character.

Please do not change the filename.

divide and conquer
first approach is the normal recursion

halfway
recursion for both sides - stored as variables
and then compare them
more efficient by splitting it in the middle



"""
import math
# Scaffold for solution to DIT347 , Assignment 3


def findNonDuplicate(A):
    # Given an input list A of character, which is sorted in an increasing order,
    # and each character is duplicated except one which corresponds to the non-duplicate character in the list.
    # you need to find the non duplicate character
    # Your code below

    # only allow alpha
    # How to do this without increasing complexity?

    # empty list
    if len(A) == 0:
        return None

    # no duplicate value
    if len(A) == 2 and A[0] == A[1]:
        return None

    # Recursive case
    if len(A) > 2:
        # mid = math.ceil((len(A) / 2))
        mid = len(A) // 2
        if mid % 2 != 0:
            mid += 1

        right = A[mid:]
        left = A[:mid]

        if left[-1] == left[-2]:
            return findNonDuplicate(right)
        else:
            return findNonDuplicate(left)

    # Base case
    return A[0]


if __name__ == "__main__":
    assert findNonDuplicate(['c', 'c', 'd', 'd', 'f', 'f', 'z']) == 'z'
    assert findNonDuplicate(
        ['a', 'a', 'b', 'b', 'c', 'd', 'd', 'e', 'e', 'r', 'r']) == 'c'
    assert findNonDuplicate(
        ['a', 'a', 'b', 'b', 'd', 'd', 'e', 'e', 'r', 'r']) == None
