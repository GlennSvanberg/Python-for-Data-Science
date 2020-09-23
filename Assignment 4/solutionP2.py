"""
MergeSort is based on the merge function which takes as an input two sorted list of n elements each and return as an output a sorted list of 2n elements.

An extended version of this function is multiMerge where the input is k sorted lists of size n each and returns as an output a list of kn sorted elements.

Example 1:

Input list: [[1,3,5],[2,7,9],[0,6,8]]

Non-duplicate: [0, 1, 2, 3, 5, 6, 7, 8, 9]

Solve this problem by using recursion. Please use solutionP2.py
Preview the document as a starting point by implementing the body of the function multiMerge(listOfLists) 
which takes k sorted lists of size n each as an input and returns a sorted list of kn elements. 
Please do not change the filename.
"""


def multiMerge(ListOfArrays):
    # Given an input  k sorted lists of size n each
    # you need to return a sorted list of kn elements by using recursion
    # Your code below

    return


if __name__ == "__main__":
    assert multiMerge([[1, 3, 5], [2, 7, 9], [0, 6, 8]]) == [
        0, 1, 2, 3, 5, 6, 7, 8, 9]
    assert multiMerge([[1, 3, 5]]) == [1, 3, 5]
