
def merge(a, b):
    # array to be returned
    c = []
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
    return c


"""
a = [1, 3, 5]
b = [2, 4, 6]
print(merge(a, b))
"""


def m_sort(a):

    # if length has zero or one values it is already sorted and can be returned directly

    if len(a) <= 1:
        return a
    # Split array in middle
    middle = len(a)//2
    left = m_sort(a[:middle])
    right = m_sort(a[middle:])

    # merge the now sorted sublists
    return merge(left, right)


a = [1, 6, 7, 9, 3, 5, 7,  2, 4, 7, 9, 6, 3]
print(m_sort(a))


def merge_sort(arr):
    size = len(arr)
    print(arr)

    # divide into subproblems by splitting in the middle
    if size > 1:
        mid = size // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        p = 0
        q = 0
        r = 0

        left_size = len(left)
        right_size = len(right)

        while p < left_size and q < right_size:
            if left[p] < right[q]:
                arr[r] = left[p]
                p += 1
            else:
                arr[r] = right[q]
                q += 1

            r += 1
        # iterate over left side
        while p < left_size:
            arr[r] = left[p]
            p += 1
            r += 1

        # iterate over right side
        while q < right_size:
            arr[r] = right[q]
            q += 1
            r += 1


"""
inp_arr = [11, 31, 7, 41, 101, 56, 77, 2]
print("Input Array:")
print(inp_arr)
merge_sort(inp_arr)
print("Sorted Array:")
print(inp_arr)
"""
