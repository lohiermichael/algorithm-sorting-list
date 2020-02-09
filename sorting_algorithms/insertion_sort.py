from inputs import InputList
from typing import List


def insertion(L: List) -> List:
    """
    This will perform the insertion sort algorithm
    Args:
        L(list): Input list
    Returns:
        Sorted list
    """

    for i in range(1, len(L)):
        while L[i - 1] > L[i] and i >= 1:
            L[i], L[i - 1] = L[i - 1], L[i]
            i -= 1
        # i will come back to the next value of the for ar the end of the while
    return L


if __name__ == '__main__':
    count_err = 0
    for i in range(100):
        L = InputList(l_length=10, min_value=0, max_value=100)
        if insertion(L) != sorted(L):
            count_err += 1
    print(f'There are {count_err} errors')
