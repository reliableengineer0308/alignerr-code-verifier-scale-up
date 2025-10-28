import unittest
from solution import product_except_self

class TestProductExceptSelf(unittest.TestCase):
    """Unit tests for product_except_self function."""

    def test_example_1(self):
        """Test: [1,2,3,4] → [24,12,8,6]"""
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_example_2(self):
        """Test with zero: [-1,1,0,-3,3] → [0,0,9,0,0]"""
        self.assertEqual(product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])


    def test_example_3(self):
        """Test two elements: [2,3] → [3,2]"""
        self.assertEqual(product_except_self([2, 3]), [3, 2])

    def test_all_ones(self):
        """[1,1,1,1] → each product is 1×1×1 = 1"""
        self.assertEqual(product_except_self([1] * 4), [1] * 4)

    def test_single_zero(self):
        """[0,1,2,3] → only index 0 gets 1×2×3=6; others get 0"""
        self.assertEqual(product_except_self([0, 1, 2, 3]), [6, 0, 0, 0])

    def test_two_zeros(self):
        """Multiple zeros → all products are 0"""
        self.assertEqual(product_except_self([1, 0, 0, 2]), [0, 0, 0, 0])

    def test_negative_numbers(self):
        """[-2, -3] → [-3, -2]"""
        self.assertEqual(product_except_self([-2, -3]), [-3, -2])

    def test_mixed_negatives(self):
        """[-1, 2, -3, 4] → products with sign handled correctly"""
        expected = [2 * (-3) * 4, (-1) * (-3) * 4, (-1) * 2 * 4, (-1) * 2 * (-3)]
        self.assertEqual(product_except_self([-1, 2, -3, 4]), expected)

    def test_large_input(self):
        """Large array of ones → all products equal to 1^(n-1) = 1"""
        n = 10000
        nums = [1] * n
        expected = [1] * n  # Each element is product of 9999 ones
        self.assertEqual(product_except_self(nums), expected)


    def test_large_with_single_zero(self):
        """Large array with one zero → only that index gets non-zero product"""
        n = 5000
        nums = [2] * n  # All 2s
        nums[1000] = 0  # Insert zero at index 1000

        
        # Only index 1000 should have non-zero value (product of all other 2s)
        expected = [0] * n
        expected[1000] = 2 ** (n - 1)  # Product of 4999 twos
        
        self.assertEqual(product_except_self(nums), expected)

    def test_large_with_two_zeros(self):
        """Two zeros → all products become zero"""
        n = 3000
        nums = [5] * n
        nums[500] = 0
        nums[1500] = 0
        expected = [0] * n
        self.assertEqual(product_except_self(nums), expected)

    def test_alternating_signs(self):
        """Alternating positive/negative → sign pattern in result"""
        nums = [1, -1, 1, -1, 1]
        # Products:
        # index 0: (-1)*1*(-1)*1 = 1
        # index 1: 1*1*(-1)*1 = -1
        # etc.
        expected = [1, -1, 1, -1, 1]
        self.assertEqual(product_except_self(nums), expected)

    def test_power_of_two_elements(self):
        """Powers of two → products are powers of two"""
        nums = [2, 4, 8]  # 2^1, 2^2, 2^3
        # Expected:
        # index 0: 4*8 = 32 = 2^5
        # index 1: 2*8 = 16 = 2^4
        # index 2: 2*4 = 8 = 2^3
        expected = [32, 16, 8]
        self.assertEqual(product_except_self(nums), expected)


    def test_boundary_min_values(self):
        """All -30 → handle min constraint"""
        nums = [-30, -30]
        expected = [-30, -30]  # Each is product of the other
        self.assertEqual(product_except_self(nums), expected)


    def test_boundary_max_values(self):
        """All 30 → handle max constraint"""
        nums = [30, 30, 30]
        expected = [900, 900, 900]  # 30*30 for each
        self.assertEqual(product_except_self(nums), expected)


    def test_mixed_small_large(self):
        """Mix of small and large numbers"""
        nums = [1, 10, 100, 1000]
        expected = [
            10 * 100 * 1000,    # 1,000,000
            1 * 100 * 1000,     # 100,000
            1 * 10 * 1000,      # 10,000
            1 * 10 * 100         # 1,000
        ]
        self.assertEqual(product_except_self(nums), expected)


    def test_performance_stress(self):
        """Stress test with 10^4 random integers"""
        import random
        # Generate 10k random ints in [-30, 30]
        import random
        nums = [random.randint(-30, 30) for _ in range(10000)]
        
        result = product_except_self(nums)
        # Verify basic properties
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(nums))
        # Check no division was used (we can't verify directly, but ensure logic holds)
        # This test confirms it runs within time and returns valid list


    def test_identical_elements(self):
        """All elements identical → symmetric result"""
        nums = [7, 7, 7, 7]
        expected = [7*7*7] * 4  # 343 at each position
        self.assertEqual(product_except_self(nums), expected)


    def test_three_elements(self):
        """Minimal case with 3 elements"""
        nums = [2, 3, 4]
        expected = [3*4, 2*4, 2*3]  # [12, 8, 6]
        self.assertEqual(product_except_self(nums), expected)


    def test_with_leading_trailing_ones(self):
        """Ones at boundaries don't affect product magnitude"""
        nums = [1, 5, 1, 6, 1]
        expected = [
            5 * 1 * 6 * 1,  # 30
            1 * 1 * 6 * 1,   # 6
            1 * 5 * 6 * 1,  # 30
            1 * 5 * 1 * 1,  # 5
            1 * 5 * 1 * 6   # 30
        ]
        self.assertEqual(product_except_self(nums), expected)



if __name__ == '__main__':
    unittest.main()
