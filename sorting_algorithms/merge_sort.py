from typing import List
from testing import test_sorting_algo


def merge_sort_explanation(L: List) -> List:
    """
    This will perform the merge sort algorithm
    Args:
        L(list): Input list
    Returns:
        Sorted list
    """
    if len(L) <= 1:
        return L
    else:
        mid = len(L) // 2
        L_left, L_right = L[:mid], L[mid:]
        L_left_sorted = merge_sort_explanation(L_left)
        L_right_sorted = merge_sort_explanation(L_right)
        # Merge step
        L_sorted = []
        # 'i' will iterate through L_left_sorted
        # 'j' will iterate through L_right_sorted
        i, j= 0, 0
        while i < len(L_left_sorted) and j < len(L_right_sorted):
            if L_left_sorted[i] < L_right_sorted[j]:
                L_sorted.append(L_left_sorted[i])
                i += 1
            else:
                L_sorted.append(L_right_sorted[j])
                j += 1
        # When one of the list has been scanned through, fill L_sorted with the left elements of the other list
        while i < len(L_left_sorted):
            L_sorted.append(L_left_sorted[i])
            i += 1
        while j < len(L_right_sorted):
            L_sorted.append(L_right_sorted[j])
            j += 1
        return L_sorted


def merge_sort(L: List) -> List:
    """
    This will perform the merge sort algorithm.
    This is a compact version of the previous algorithm.
    It will save some space memory
    Args:
        L(list): Input list
    Returns:
        Sorted list
    """
    if len(L) <= 1:
        return L
    else:
        mid = len(L) // 2
        L_left = merge_sort(L[:mid])
        L_right = merge_sort(L[mid:])
        i, j, k = 0, 0, 0
        while i < len(L_left) and j < len(L_right):
            if L_left[i] < L_right[j]:
                L[k] = L_left[i]
                i += 1
            else:
                L[k] = L_right[j]
                j += 1
            k += 1
        while i < len(L_left):
            L[k] = L_left[i]
            i += 1
            k += 1

        while j < len(L_right):
            L[k] = L_right[j]
            j += 1
            k += 1
        return L


if __name__ == '__main__':
    test_sorting_algo(algo_name=merge_sort, number_tests=1000)