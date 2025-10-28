import unittest
from solution import three_sum

class TestThreeSum(unittest.TestCase):

    def test_example_1(self):
        """Test case with multiple valid triplets."""
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(three_sum(nums), expected)

    def test_no_solution(self):
        """Test when no triplet sums to zero."""
        nums = [0, 1, 1]
        self.assertEqual(three_sum(nums), [])

    def test_all_zeros(self):
        """Test with three zeros."""
        nums = [0, 0, 0]
        self.assertEqual(three_sum(nums), [[0, 0, 0]])

    def test_all_positive(self):
        """Test with all positive numbers (no solution)."""
        nums = [1, 2, 3]
        self.assertEqual(three_sum(nums), [])

    def test_all_negative(self):
        """Test with all negative numbers (no solution)."""
        nums = [-3, -2, -1]
        self.assertEqual(three_sum(nums), [])

    def test_two_zeros_and_negative(self):
        """Test pattern: [-x, 0, 0]."""
        nums = [-2, 0, 0, 2]
        # Valid: (-2) + 0 + 2 = 0 → [-2,0,2]
        self.assertEqual(three_sum(nums), [[-2, 0, 2]])

    def test_duplicates_in_input(self):
        """Test input with many duplicates."""
        nums = [-1, -1, -1, 0, 1, 1, 1]
        # Valid triplets:
        # (-1) + (-1) + 2? → no 2
        # (-1) + 0 + 1 → yes
        expected = [[-1, 0, 1]]
        self.assertEqual(three_sum(nums), expected)

    def test_large_input(self):
        """Stress test with larger input."""
        import random
        nums = [random.randint(-100, 100) for _ in range(100)]
        result = three_sum(nums)
        # Just check it runs and output is list of lists
        self.assertIsInstance(result, list)
        for triplet in result:
            self.assertEqual(len(triplet), 3)
            self.assertEqual(sum(triplet), 0)

if __name__ == "__main__":
    unittest.main()
