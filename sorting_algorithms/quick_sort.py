# The version that I know of quick sort: the merge is made in a different list which inceases the memory complexity
from typing import List


def quick_sort_michael_first_element(L: List) -> List:
    """
    This version of quick sort takes the first element as the pivot,
    which is not ideal in the worst case scenario
    Parameters
    ----------
    L (list): list to sort

    Returns
    -------
    Sorted list
    """
    if len(L) <= 1:
        return L
    else:
        # Definition of the pivot
        pivot = L[0]
        L_left, L_right = [], []

        # The split
        for x in L[1:]:
            if x < pivot:
                L_left.append(x)
            else:
                L_right.append(x)

        return quick_sort_michael_first_element(L_left) + [pivot] + quick_sort_michael_first_element(L_right)


def quick_sort_michael(L: List, randomized: bool = True) -> List:
    """
    This quick sort algorithm includes the possibility to choose a random pivot or
    to choose the first element of the list as the pivot
    Parameters
    ----------
    L (list): list to sort
    randomized (bool): if true the pivot is randomly chosen

    Returns
    -------
    Sorted list
    """
    if randomized:
        if len(L) <= 1:
            return L
        else:
            # Definition of the pivot
            rand_index = random.randint(0, len(L) - 1)
            pivot = L.pop(rand_index)
            L_left, L_right = [], []

            # The split
            for x in L:
                if x < pivot:
                    L_left.append(x)
                else:
                    L_right.append(x)

            return quick_sort_michael(L_left, randomized=randomized) \
                   + [pivot] \
                   + quick_sort_michael(L_right, randomized=randomized)
    else:
        return quick_sort_michael_first_element(L)


def partition_fist_element(L: List, left: int, right: int):
    """
    Sub function that partition the input list relatively to its first element
    Parameters
    ----------
    L (list): input list
    left (int): left index of the list to partition
    right (int): right index of the list to partition

    Returns
    -------
    Modifies the input list and returns the index of the position of the pivot
    """
    pivot = L[left]
    # i is the index of the split between elements smaller and bigger to the pivot
    # j is the element the crosses the list
    i = left + 1
    for j in range(left + 1, right + 1):
        if L[j] < pivot:
            L[i], L[j] = L[j], L[i]
            i += 1
    # Final swap to  put the pivot at its right place
    L[left], L[i - 1] = L[i - 1], L[left]
    return i - 1


def quick_sort_inplace_first_element(L: List) -> List:
    """
    This function sorts the input list with in-place implementation, i.e.
    it keeps memory complexity quite low as contrary to the quick_sort_michael function
    no additional L_left and L_right are created.

    Parameters
    ----------
    L (list): input list

    Returns
    -------
    Sorted list
    """

    def sub_function(L: List, right: int, left: int):
        if left < right:
            i_pivot = partition_fist_element(L, left=left, right=right)
            sub_function(L, left=left, right=i_pivot - 1)
            sub_function(L, left=i_pivot + 1, right=right)

    sub_function(L, left=0, right=len(L) - 1)
    return L


if __name__ == '__main__':
    L = InputList()
    print(L)
    print(quick_sort_inplace_first_element(L))
