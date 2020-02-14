from complexity_evaluation.output_algo import AlgoAnalysis
from typing import *
import pandas as pd
from inputs import InputList
from sorting_algorithms.merge_sort import merge_sort
import matplotlib.pyplot as plt


class CollectionAlgos(List[AlgoAnalysis]):
    def __init__(self, *args):
        """
        You pass a as arguments one or several names of algorithms
        to create the object
        Parameters
        ----------
        args: Tuple of algorithms as functions
        """
        super().__init__()
        self.list_algorithms = list(args)
        self.list_algorithms_name = [algo.__name__ for algo in self.list_algorithms]
        self._construct()

    def __str__(self):
        return 'CollectionAlgos(' + ', '.join(self.list_algorithms_name) + ')'

    def _construct(self):
        """
        Build the object CollectionAlgosList as a list of AlgoAnalysis objects
        Returns
        -------
        None
        """
        for algo in self.list_algorithms:
            self.append(AlgoAnalysis(algo))

    def have_same_output(self, l: list) -> bool:
        """
         Inform if the results of all the passed
        algorithms return the same output for a given list

        Parameters
        ----------
        l (list): Input list of the passed algorithms

        Returns
        -------
        bool
        """
        return len(set(map(tuple, [algo(l) for algo in self.list_algorithms]))) == 1

    def calculate_time_single_list(self, **kwargs) -> Dict[str, List[float]]:
        """
        Generate an random input list and compute the time evaluation of each
        algorithm on this list
        Parameters
        ----------
        l_length (int): Length of the input list
        min_value (int): Minimal value of the elements of the list
        max_value (int): Maximal value of the elements of the list
        distinct_elements (bool): distinct elements in the list

        Returns
        -------
        Dict(str, List[float]): dictionary with list of time of computation for each algorithm
        """
        # Generate a random listNone
        random_list = InputList(**kwargs)

        # First assert that they all have the same results, if not who cares how fast they are
        assert self.have_same_output(random_list), "The time evaluation is not significant as the outputs of" \
                                                   "the algorithms differ"

        return {algo_analysis.algo_name: algo_analysis.calculate_time_single_list(input_l=random_list)
                for algo_analysis in self}

    def calculate_time_multiple_lists(self,
                                      range_length: int,
                                      harmonization: bool = True,
                                      f_harmonization=10,
                                      worst_case: bool = False,
                                      **kwargs):
        """
        Generate random input lists of variate length within the range size
        and perform the time computation for the different algorithms
        Parameters
        ----------
        range_length: range of length of the input lists to test: from 1 to range_length
        harmonization: reduce noise of the curve
        f_harmonization: harmonization factor, an integer or a list the bigger n the smoother the curve will be
        worst_case: will compare the algorithms in the worst case (reversed list) in the context of sorting algorithm

        Returns
        -------
        List[List]
        """
        # Each dictionary is a row, with (key, value) pairs of the future dataFrame
        # The key of this big dictionary is the length of the list on which is perform the algorithms
        # as future index of the dataFrame
        # The key of the sub-dictionaries is the name of the algorithm that is performed
        # as future column of the dataFrame
        # The values of the dataFrame are the times of computation

        dict_of_series = {algo_name: algo.calculate_time_multiple_lists(range_length=range_length,
                                                                        harmonization=harmonization,
                                                                        f_harmonization=f_harmonization,
                                                                        worst_case=worst_case,
                                                                        **kwargs).iloc[:, -1]
                          for algo, algo_name in zip(self, self.list_algorithms_name)}
        return pd.DataFrame.from_dict(data=dict_of_series)


if __name__ == '__main__':
    compare_algo = CollectionAlgos(sorted, merge_sort)
    test_list = InputList()
    df = compare_algo.calculate_time_multiple_lists(range_length=1000, harmonization=False)
    df.plot()
    plt.show()