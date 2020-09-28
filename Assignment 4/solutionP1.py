

def findNonDuplicate(A):

    # empty list
    if len(A) == 0:
        return None

    # no duplicate value
    if len(A) == 2 and A[0] == A[1]:
        return None

    # Recursive case
    if len(A) > 2:
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


def findNonDuplicateVerifiedInput(A):
    for a in A:
        if not a.isalnum():
            return f"{a} is not a valid input value"

    return findNonDuplicate(A)


if __name__ == "__main__":
    assert findNonDuplicate(['c', 'c', 'd', 'd', 'f', 'f', 'z']) == 'z'
    assert findNonDuplicate(
        ['a', 'a', 'b', 'b', 'c', 'd', 'd', 'e', 'e', 'r', 'r']) == 'c'
    assert findNonDuplicate(
        ['a', 'a', 'b', 'b', 'd', 'd', 'e', 'e', 'r', 'r']) == None
    assert findNonDuplicateVerifiedInput(
        ['c', 'c', 'd', 'd', 'f', '&', 'z']) == '& is not a valid input value'
