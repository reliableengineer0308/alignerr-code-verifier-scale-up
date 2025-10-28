import unittest
from solution import max_subarray_sum_constrained

class TestMaxSubarraySumConstrained(unittest.TestCase):

    def test_basic_case(self):
        """Test with normal positive/negative mix."""
        result = max_subarray_sum_constrained([1, -2, 3, 4, -1, 2], 2, 4)
        self.assertEqual(result, 8)  # [3,4,-1,2] sum=8

    def test_all_negative(self):
        """Test when all elements are negative."""
        result = max_subarray_sum_constrained([-1, -2, -3], 1, 3)
        self.assertEqual(result, -1)  # Best: [-1]

    def test_exact_length(self):
        """Test when min_len == max_len."""
        result = max_subarray_sum_constrained([5, 2, -1, 3], 3, 3)
        self.assertEqual(result, 6)  # [5,2,-1] sum=6


    def test_single_element(self):
        """Test minimal valid subarray (length 1)."""
        result = max_subarray_sum_constrained([42], 1, 1)
        self.assertEqual(result, 42)

    def test_empty_array(self):
        """Test empty input array."""
        result = max_subarray_sum_constrained([], 1, 5)
        self.assertEqual(result, 0)

    def test_impossible_constraints(self):
        """Test when constraints can't be met."""
        result = max_subarray_sum_constrained([1, 2], 5, 10)
        self.assertEqual(result, 0)  # min_len > array length

    def test_positive_only(self):
        """Test with all positive numbers."""
        result = max_subarray_sum_constrained([1, 2, 3, 4], 2, 3)
        self.assertEqual(result, 9)  # [2,3,4] sum=9

    def test_negative_min_len(self):
        """Test with min_len close to array length."""
        result = max_subarray_sum_constrained([3, -1, 4, -2], 4, 4)
        self.assertEqual(result, 4)  # Only possible: entire array sum=4

    def test_large_array(self):
        """Test performance with larger input."""
        arr = [1] * 1000  # All ones
        result = max_subarray_sum_constrained(arr, 50, 100)
        self.assertEqual(result, 100)  # Max sum with length 100

    def test_mixed_edge_cases(self):
        """Test combination of edge conditions."""
        # Array with one element, tight constraints
        result1 = max_subarray_sum_constrained([-5], 1, 1)
        self.assertEqual(result1, -5)
        
        # Large max_len but small array
        result2 = max_subarray_sum_constrained([2, -3, 1], 1, 10)
        self.assertEqual(result2, 2)  # Best: [2]

if __name__ == "__main__":
    unittest.main()
