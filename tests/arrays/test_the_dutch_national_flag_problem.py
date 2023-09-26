from src.arrays.the_dutch_national_flag_problem import dutch_flag_partition


class TestDutchFlagPartition:
    def test_dutch_flag_partition(self):
        arr = [0, 1, 2, 0, 2, 1, 1]
        pivot_index = 3
        dutch_flag_partition(pivot_index, arr)
        assert arr == [0, 0, 2, 2, 1, 1, 1]

    def test_dutch_flag_partition_empty_array(self):
        arr = []
        pivot_index = 0
        dutch_flag_partition(pivot_index, arr)
        assert arr == []

    def test_dutch_flag_partition_single_element_array(self):
        arr = [1]
        pivot_index = 0
        dutch_flag_partition(pivot_index, arr)
        assert arr == [1]

    def test_dutch_flag_partition_all_equal_elements(self):
        arr = [1, 1, 1, 1, 1]
        pivot_index = 2
        dutch_flag_partition(pivot_index, arr)
        assert arr == [1, 1, 1, 1, 1]

    def test_dutch_flag_partition_all_smaller_elements(self):
        arr = [1, 2, 3, 4, 5]
        pivot_index = 4
        dutch_flag_partition(pivot_index, arr)
        assert arr == [1, 2, 3, 4, 5]

    def test_dutch_flag_partition_all_larger_elements(self):
        arr = [5, 4, 3, 2, 1]
        pivot_index = 0
        dutch_flag_partition(pivot_index, arr)
        assert arr == [4, 3, 2, 1, 5]
