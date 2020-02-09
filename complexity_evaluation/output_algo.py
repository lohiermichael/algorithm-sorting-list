import time
from jedi.evaluate.context import function
from typing import *
import statistics
import matplotlib.pyplot as plt
import pandas as pd
from inputs import InputList


class AlgoAnalysis:
    def __init__(self, algo: function):
        """
        For a given problem in algorithmic that takes a standardized input (for instance: a list)
        this class will give information of the running time of the algorithm. It will also
        give an approximate of the complexity of the algorithm
        Parameters
        ----------
        algo: The algorithm as a function
        """
        self.algo = algo
        self.algo_name = algo.__name__

    def __repr__(self):
        return f'AlgoAnalysis(name={self.algo_name})'

    def calculate_time_single_list(self, input_l: list) -> float:
        """
        Calculate the computation time of an algo on a specific list
        Parameters
        ----------
        input_l (list): Input list of the algorithm

        Returns
        -------
        float: computation time in ms
        """
        start_time = time.time()
        _ = self.algo(input_l)
        end_time = time.time()

        return end_time - start_time

    def calculate_time_multiple_lists(self, range_length: int, harmonization: bool = True,
                                      factor_harmonization: int = 5, **kwargs) -> pd.Series:
        """
        Generate random input lists of variate length within the range size
        and perform the time computation
        Parameters
        ----------
        range_length: range of length of the input lists to test: from 1 to range_length
        harmonization: remove the noise by trying several times the same algo for different
                        lists of a given length and taking the average running time
        factor_harmonization: if harmonization is True, this value is the number of trials
                            of different lists of the same size to harmonize
        kwargs: the other arguments of the input lists
        Returns
        -------
        List[float]
        """
        if harmonization:
            res_time_l = []
            for l_length in range(1, range_length + 1):
                times_with_l_length = []
                for _ in range(factor_harmonization):
                    times_with_l_length.append(self.calculate_time_single_list(input_l=
                                                                               InputList(l_length=l_length,
                                                                                         **kwargs)))
                res_time_l.append(statistics.mean(times_with_l_length))

        else:
            res_time_l = [self.calculate_time_single_list(input_l=InputList(l_length=l_length, **kwargs))
                          for l_length in range(1, range_length + 1)]

        # Transform in Series to plot the result with a simple .plot() later
        res_time = pd.Series(res_time_l)
        res_time.index = res_time.index + 1
        res_time.name = f"Harmonization {factor_harmonization}"

        return res_time


if __name__ == '__main__':
    test_input_list = InputList(l_length=100000, max_value=1000000000)
    # print(test_input_list)
    # print(sorted(test_input_list))
    algo_test = AlgoAnalysis(sorted)
    print(algo_test)
    fig, ax = plt.subplots(figsize=(10, 10))
    for factor_harmonization in range(1, 10, 1):
        res = algo_test.calculate_time_multiple_lists(range_length=100, factor_harmonization=factor_harmonization)
        res.plot(legend=res.name)
    plt.show()
