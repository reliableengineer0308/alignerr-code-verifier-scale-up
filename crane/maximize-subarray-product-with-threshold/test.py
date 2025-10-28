import unittest
from solution import max_constrained_subarray

class TestMaxConstrainedSubarray(unittest.TestCase):
    def test_example_1(self):
        """Basic case with mixed signs."""
        result = max_constrained_subarray([2, 3, -2, 4], 2, 3)
        self.assertEqual(result, 6.0)

    def test_with_zeros(self):
        """Case with zeros."""
        result = max_constrained_subarray([-2, 0, -1], 2, 0)
        self.assertEqual(result, 0.0)

    def test_no_valid_subarray(self):
        """No element meets threshold."""
        result = max_constrained_subarray([1, 2, 3, 4, 5], 3, 6)
        self.assertIsNone(result)

    def test_all_zeros(self):
        """All zeros, threshold is zero."""
        result = max_constrained_subarray([0, 0, 0], 2, 0)
        self.assertEqual(result, 0.0)

    def test_k_equals_1(self):
        """k = 1: pick largest valid element."""
        result = max_constrained_subarray([5, -3, 8, -1], 1, 4)
        self.assertEqual(result, 8.0)  # Only 5,8 >=4; 8 is larger

    def test_k_equals_length(self):
        """k equals array length: only one possible subarray."""
        result = max_constrained_subarray([2, -3, 4], 3, -5)
        expected = 2 * (-3) * 4  # = -24
        self.assertEqual(result, float(expected))

    def test_alternating_signs(self):
        """Subarrays with alternating signs; check sign handling."""
        result = max_constrained_subarray([-1, 2, -3, 4, -5], 3, 1)
        # Valid subarrays:
        # [-1,2,-3] → product = 6 (valid: 2≥1)
        # [2,-3,4] → product = -24 (valid: 2,4≥1)
        # [-3,4,-5] → product = 60 (valid: 4≥1)
        self.assertEqual(result, 60.0)

    def test_negative_threshold(self):
        """Threshold is negative; check if negative elements qualify."""
        result = max_constrained_subarray([-5, -2, -3, -1], 2, -2)
        # Subarrays:
        # [-5,-2] → product=10, valid (-2≥-2) → candidate=10
        # [-2,-3] → product=6, valid (-2≥-2) → candidate=6
        # [-3,-1] → product=3, valid (-1≥-2) → candidate=3
        self.assertEqual(result, 10.0)  # Max is 10


    def test_single_valid_element(self):
        """Only one element meets threshold; ensure it's included."""
        result = max_constrained_subarray([10, -20, 30], 2, 25)
        # Only subarray with 30: [-20,30] → product=-600
        self.assertEqual(result, -600.0)


    def test_all_negative_valid(self):
        """All elements negative but some meet threshold."""
        result = max_constrained_subarray([-4, -3, -2, -1], 2, -3)
        # Valid subarrays:
        # [-4,-3] → product=12 (valid: -3≥-3)
        # [-3,-2] → product=6 (valid: -3,-2≥-3)
        # [-2,-1] → product=2 (valid: -2,-1≥-3)
        self.assertEqual(result, 12.0)


    def test_edge_case_single_element(self):
        """k=1: pick the largest element ≥ threshold."""
        result = max_constrained_subarray([5, 1, 8, 3], 1, 4)
        # Valid elements: 5,8 ≥4 → max=8
        self.assertEqual(result, 8.0)


if __name__ == "__main__":
    unittest.main()

