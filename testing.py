from inputs import InputList
from typing import Callable


def test_sorting_algo(algo_name: Callable, reference_algo_name: Callable = sorted, number_tests: int =100) -> None:
    """
    Compare the result of an sorting algorithm with a referenced one for a certain number of test
    Parameters
    ----------
    algo_name(func): The name of the sorting algorithm that we want to check
    reference_algo_name(func): The referenced algorithm that we know works
    number_tests(int): The number of tests that we want to perform

    Returns
    -------
    None
    """
    count_err = 0
    for i in range(100):
        L = InputList(l_length=10, min_value=0, max_value=100)
        if algo_name(L) != reference_algo_name(L):
            count_err += 1
    print(f'There are {count_err} errors')
