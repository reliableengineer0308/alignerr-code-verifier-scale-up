import unittest
from solution import length_of_lis

class TestLongestIncreasingSubsequence(unittest.TestCase):
    
    def test_example_1(self):
        """Test with classic example from problem."""
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(length_of_lis(nums), 4)
    

    def test_example_2(self):
        """Test with another sample input."""
        nums = [0, 1, 0, 3, 2, 3]
        self.assertEqual(length_of_lis(nums), 4)

    def test_all_equal(self):
        """Test when all elements are the same."""
        nums = [7, 7, 7, 7, 7]
        self.assertEqual(length_of_lis(nums), 1)

    def test_single_element(self):
        """Test single element array."""
        nums = [42]
        self.assertEqual(length_of_lis(nums), 1)

    def test_descending_order(self):
        """Test strictly decreasing sequence."""
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(length_of_lis(nums), 1)


    def test_ascending_order(self):
        """Test strictly increasing sequence."""
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(length_of_lis(nums), 5)


    def test_empty_array(self):
        """Test empty input."""
        nums = []
        self.assertEqual(length_of_lis(nums), 0)

    def test_small_case(self):
        """Test minimal case with two elements."""
        nums = [2, 1]
        self.assertEqual(length_of_lis(nums), 1)
        nums = [1, 2]
        self.assertEqual(length_of_lis(nums), 2)

    def test_complex_case(self):
        """Test a more complex case with repeated values."""
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        # Valid LIS examples:
        # - 1 → 2 → 5 → 9 (indices 1,6,9,5)
        # - 1 → 4 → 5 → 6 (indices 1,2,4,7)
        # All have length = 4
        self.assertEqual(length_of_lis(nums), 4)  # Fixed from 5 to 4


if __name__ == "__main__":
    unittest.main()
