from typing import List
from testing import test_sorting_algo


def insertion_sort(L: List) -> List:
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
    test_sorting_algo(algo_name=insertion_sort, number_tests=10)