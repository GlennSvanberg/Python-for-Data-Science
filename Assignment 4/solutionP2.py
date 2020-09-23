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


def merge(a, b):
    # array to be returned
    c = []
    print("a", a)
    print("b", b)
    # index to iterate over for each array
    a_index, b_index = 0, 0

    # iterate over both array a and b
    while a_index < len(a) and b_index < len(b):
        # append the largest value to array c and append the index the value is taken from
        if a[a_index] < b[b_index]:
            c.append(a[a_index])
            a_index += 1
        else:
            c.append(b[b_index])
            b_index += 1

    # add last value to the list
    if a_index == len(a):
        c.extend(b[b_index:])
    else:
        c.extend(a[a_index:])
        print("c", c)
    return c


def multiMerge(ListOfArrays):

    size = len(ListOfArrays)

    if size <= 1:
        # add code to return it as a list and not a nested list
        return ListOfArrays

    print("Arrays:", ListOfArrays)
    # split list of arrays in middle
    mid = size // 2
    left = multiMerge(ListOfArrays[:mid])
    right = multiMerge(ListOfArrays[mid:])

    # convert list of list to list
    if type(left[0]) == list:
        left = left[0]
    if type(right[0]) == list:
        right = right[0]

    print("left", left)
    print("right", right)
    return merge(left, right)


print(multiMerge([[1, 3, 5, 111, 123], [2, 6, 9], [5, 8, 33, 87]]))


"""
Assertions

if __name__ == "__main__":
    assert multiMerge([[1, 3, 5], [2, 7, 9], [0, 6, 8]]) == [
        0, 1, 2, 3, 5, 6, 7, 8, 9]
    assert multiMerge([[1, 3, 5]]) == [1, 3, 5]

"""
