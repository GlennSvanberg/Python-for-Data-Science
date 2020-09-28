
def merge(a, b):
    # array to be returned
    res = []
    # index to iterate over for each array
    a_i = 0
    b_i = 0

    # iterate over both array a and b
    while a_i < len(a) and b_i < len(b):
        # append the largest value to array c and append the index the value is taken from
        if a[a_i] < b[b_i]:
            res.append(a[a_i])
            a_i += 1
        else:
            res.append(b[b_i])
            b_i += 1

    # add last value to the list
    if a_i == len(a):
        res.extend(b[b_i:])
    else:
        res.extend(a[a_i:])
    return res


def multiMerge(ListOfArrays):

    size = len(ListOfArrays)
    # return sublist if only one list and return list if
    if size == 1 and type(ListOfArrays[0]) == list:

        return ListOfArrays[0]
    # return input back if it is empty
    if size == 0:
        return ListOfArrays

    # split list of arrays in middle
    mid = size // 2
    left = multiMerge(ListOfArrays[:mid])
    right = multiMerge(ListOfArrays[mid:])

    # convert list of list to list
    if type(left[0]) == list:
        left = left[0]
    if type(right[0]) == list:
        right = right[0]
    return merge(left, right)


# Assertions
if __name__ == "__main__":
    assert multiMerge([[1, 3, 5], [2, 7, 9], [0, 6, 8]]) == [
        0, 1, 2, 3, 5, 6, 7, 8, 9]
    assert multiMerge([[1, 3, 5]]) == [1, 3, 5]
