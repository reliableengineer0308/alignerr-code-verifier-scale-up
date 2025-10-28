import unittest
from solution import max_subarray

class TestMaximumSubarray(unittest.TestCase):
    
    def test_example_1(self):
        """Test case with mixed positive/negative numbers."""
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray(nums), 6)  # [4,-1,2,1]
    
    
    def test_single_element(self):
        """Test with single element."""
        self.assertEqual(max_subarray([1]), 1)
        self.assertEqual(max_subarray([-5]), -5)
    
    
    def test_all_positive(self):
        """Test when all numbers are positive."""
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(max_subarray(nums), sum(nums))  # Entire array
    
    def test_all_negative(self):
        """Test when all numbers are negative."""
        nums = [-5, -2, -8, -1]
        self.assertEqual(max_subarray(nums), -1)  # Largest single element
    
    def test_mixed_edge(self):
        """Test edge case with alternating signs."""
        nums = [-1, 2, -3, 4, -5]
        self.assertEqual(max_subarray(nums), 4)  # Just [4]
    
    
    def test_two_elements(self):
        """Test with exactly two elements."""
        self.assertEqual(max_subarray([2, -1]), 2)
        self.assertEqual(max_subarray([-1, 2]), 2)
        self.assertEqual(max_subarray([-3, -2]), -2)
    
    
    def test_large_input(self):
        """Stress test with large array."""
        import random
        random.seed(42)
        nums = [random.randint(-100, 100) for _ in range(10000)]
        result = max_subarray(nums)
        # Basic validation: result should be >= max(nums)
        self.assertGreaterEqual(result, max(nums))
        # And <= sum of all positive numbers (rough upper bound)
        pos_sum = sum(x for x in nums if x > 0)
        if pos_sum > 0:
            self.assertLessEqual(result, pos_sum)
    
    
    def test_identical_elements(self):
        """Test with all elements the same."""
        self.assertEqual(max_subarray([3, 3, 3]), 9)  # Entire array
        self.assertEqual(max_subarray([-2, -2, -2]), -2)  # Single element
    
    
    def test_peak_valley(self):
        """Test pattern with clear peak."""
        nums = [1, -2, 3, -4, 5, -6, 7]
        self.assertEqual(max_subarray(nums), 7)  # Last element

if __name__ == "__main__":
    unittest.main()
