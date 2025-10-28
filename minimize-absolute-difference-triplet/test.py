import unittest
from solution import minimize_abs_diff_triplet

class TestMinimizeAbsDiffTriplet(unittest.TestCase):
    """
    Test suite for the minimize_abs_diff_triplet function.
    Validates correctness across various input scenarios.
    """

    def test_consecutive_numbers(self):
        """Test with numbers that form a clear optimal triplet."""
        result = minimize_abs_diff_triplet([1, 5, 3, 9, 2])
        self.assertIsNotNone(result[0])  # Triplet should exist
        self.assertEqual(result[1], 4.0)  # Expected min value: 2*(3-1) = 4
        a, b, c = result[0]
        computed = abs(a - b) + abs(b - c) + abs(c - a)
        self.assertEqual(computed, 4)  # Verify formula holds

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        result = minimize_abs_diff_triplet([-5, -2, -8, -1])
        self.assertIsNotNone(result[0])
        self.assertEqual(result[1], 8.0)  # (-5,-2,-1): 2*(-1 - (-5)) = 8
        a, b, c = result[0]
        computed = abs(a - b) + abs(b - c) + abs(c - a)
        self.assertEqual(computed, 8)

    def test_all_same_value(self):
        """Test when all elements are identical."""
        result = minimize_abs_diff_triplet([7, 7, 7])
        self.assertIsNotNone(result[0])
        self.assertEqual(result[1], 0.0)  # All equal → sum = 0
        a, b, c = result[0]
        computed = abs(a - b) + abs(b - c) + abs(c - a)
        self.assertEqual(computed, 0)

    def test_large_range(self):
        """Test with wide value range to check robustness."""
        result = minimize_abs_diff_triplet([100, -40, 70, -30, 80])
        self.assertIsNotNone(result[0])
        a, b, c = result[0]
        computed = abs(a - b) + abs(b - c) + abs(c - a)
        # Validate using mathematical identity: sum = 2*(max - min)
        expected = 2 * (max(a, b, c) - min(a, b, c))
        self.assertEqual(computed, expected)

    def test_sorted_input(self):
        """Test with already sorted input."""
        result = minimize_abs_diff_triplet([1, 2, 3, 4, 5])
        self.assertIsNotNone(result[0])
        self.assertEqual(result[1], 4.0)  # (1,2,3): 2*(3-1)=4
        a, b, c = result[0]
        computed = abs(a - b) + abs(b - c) + abs(c - a)
        self.assertEqual(computed, 4)

    def test_reverse_sorted(self):
        """Test with reverse-sorted input."""
        result = minimize_abs_diff_triplet([5, 4, 3, 2, 1])
        self.assertIsNotNone(result[0])
        self.assertEqual(result[1], 4.0)  # Same as sorted case
        a, b, c = result[0]
        computed = abs(a - b) + abs(b - c) + abs(c - a)
        self.assertEqual(computed, 4)

    def test_small_array(self):
        """Test minimal valid input (3 elements)."""
        result = minimize_abs_diff_triplet([10, 20, 30])
        self.assertIsNotNone(result[0])
        self.assertEqual(result[1], 40.0)  # (10,20,30): 2*(30-10)=40
        a, b, c = result[0]
        computed = abs(a - b) + abs(b - c) + abs(c - a)
        self.assertEqual(computed, 40)


    def test_array_with_duplicates(self):
        """Test with duplicate values."""
        result = minimize_abs_diff_triplet([1, 1, 5, 5, 9, 9])
        self.assertIsNotNone(result[0])
        a, b, c = result[0]
        computed = abs(a - b) + abs(b - c) + abs(c - a)
        expected = 2 * (max(a, b, c) - min(a, b, c))
        self.assertEqual(computed, expected)
        # Optimal triplet should have difference ≤ 8 (e.g., (1,1,5))
        self.assertLessEqual(computed, 8)

    def test_no_valid_triplet(self):
        """Test invalid input (less than 3 elements)."""
        result = minimize_abs_diff_triplet([42])  # Only 1 element
        self.assertIsNone(result[0])
        self.assertIsNone(result[1])

    def test_mixed_signs_close_values(self):
        """Test with mixed signs and close values."""
        result = minimize_abs_diff_triplet([-1, 0, 1, 100])
        self.assertIsNotNone(result[0])
        self.assertEqual(result[1], 4.0)  # (-1,0,1): 2*(1 - (-1)) = 4
        a, b, c = result[0]
        computed = abs(a - b) + abs(b - c) + abs(c - a)
        self.assertEqual(computed, 4)

if __name__ == "__main__":
    unittest.main()
