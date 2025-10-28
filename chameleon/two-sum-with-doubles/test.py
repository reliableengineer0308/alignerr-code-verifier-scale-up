import unittest
from solution import two_sum_with_doubles

class TestTwoSumWithDoubles(unittest.TestCase):

    def test_basic_case(self):
        """Basic case with one valid pair."""
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum_with_doubles(nums, target)
        self.assertEqual(result, [(0, 1)])  # 2 + 7 = 9

    def test_duplicate_values(self):
        """Case with duplicate values that form valid pairs."""
        nums = [3, 2, 4, 3]
        target = 6
        result = two_sum_with_doubles(nums, target)
        # Valid pairs:
        # - (0, 3): 3 (index 0) + 3 (index 3) = 6
        # - (1, 2): 2 (index 1) + 4 (index 2) = 6
        self.assertEqual(result, [(0, 3), (1, 2)])


    def test_multiple_pairs(self):
        """Multiple valid pairs possible."""
        nums = [1, 2, 3, 4, 5]
        target = 5
        result = two_sum_with_doubles(nums, target)
        # (0,3): 1+4=5, (1,2): 2+3=5
        self.assertEqual(result, [(0, 3), (1, 2)])

    def test_no_solution(self):
        """No valid pairs exist."""
        nums = [1, 2, 3]
        target = 10
        result = two_sum_with_doubles(nums, target)
        self.assertEqual(result, [])


    def test_exact_double(self):
        """Target is exactly double of a number (e.g., 5+5=10)."""
        nums = [5, 1, 5, 3]
        target = 10
        result = two_sum_with_doubles(nums, target)
        # Only pair: indices (0,2) → 5+5
        self.assertEqual(result, [(0, 2)])

    def test_empty_input(self):
        """Empty input should return empty list."""
        result = two_sum_with_doubles([], 5)
        self.assertEqual(result, [])


    def test_single_element(self):
        """Single element cannot form a pair."""
        result = two_sum_with_doubles([1], 2)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
