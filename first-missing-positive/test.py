import unittest
from solution import first_missing_positive

class TestFirstMissingPositive(unittest.TestCase):
    """Unit tests for first_missing_positive function."""


    def test_example_1(self):
        """Test: [1,2,0] → 3 (1 and 2 present, 3 missing)"""
        self.assertEqual(first_missing_positive([1, 2, 0]), 3)


    def test_example_2(self):
        """Test: [3,4,-1,1] → 2 (1 present, 2 missing)"""
        self.assertEqual(first_missing_positive([3, 4, -1, 1]), 2)

    def test_example_3(self):
        """Test: [7,8,9,11,12] → 1 (no 1 present)"""
        self.assertEqual(first_missing_positive([7, 8, 9, 11, 12]), 1)

    def test_example_4(self):
        """Test single element: [1] → 2"""
        self.assertEqual(first_missing_positive([1]), 2)


    def test_example_5(self):
        """Test all negatives: [-1,-2,-3] → 1"""
        self.assertEqual(first_missing_positive([-1, -2, -3]), 1)


    def test_empty_array(self):
        """Edge: empty array → smallest missing is 1"""
        self.assertEqual(first_missing_positive([]), 1)


    def test_single_negative(self):
        """[-5] → 1 missing"""
        self.assertEqual(first_missing_positive([-5]), 1)

    def test_single_zero(self):
        """[0] → 1 missing"""
        self.assertEqual(first_missing_positive([0]), 1)

    def test_duplicates(self):
        """Test array with duplicates: [1, 1, 1] → 2 (only 1 present)"""
        self.assertEqual(first_missing_positive([1, 1, 1]), 2)

    def test_duplicate_with_gap(self):
        """[1, 2, 2, 3] → 4 (1,2,3 present → next missing is 4)"""
        self.assertEqual(first_missing_positive([1, 2, 2, 3]), 4)

    def test_duplicates(self):
        """Test array with duplicates: [1, 1, 1] → 2 (only 1 present)"""
        self.assertEqual(first_missing_positive([1, 1, 1]), 2)


    def test_duplicate_with_gap(self):
        """[1, 2, 2, 3] → 4 (1,2,3 present → next missing is 4)"""
        self.assertEqual(first_missing_positive([1, 2, 2, 3]), 4)

    def test_all_ones(self):
        """[1, 1, 1, 1] → 2"""
        self.assertEqual(first_missing_positive([1] * 4), 2)

    def test_missing_in_middle(self):
        """[3, 4, 1, -1] → after placement: [1, _, 3, 4] → missing 2"""
        self.assertEqual(first_missing_positive([3, 4, 1, -1]), 2)

    def test_already_sorted(self):
        """[1, 2, 3, 4] → 5 (all present → next is n+1)"""
        self.assertEqual(first_missing_positive([1, 2, 3, 4]), 5)

    def test_reverse_sorted(self):
        """[4, 3, 2, 1] → after placement → [1,2,3,4] → missing 5"""
        self.assertEqual(first_missing_positive([4, 3, 2, 1]), 5)

    def test_large_n_all_present(self):
        """Large array with all 1..n → answer is n+1"""
        n = 1000
        nums = list(range(1, n + 1))
        self.assertEqual(first_missing_positive(nums), n + 1)

    def test_large_n_missing_first(self):
        """Large array missing 1 → answer is 1"""
        n = 1000
        nums = list(range(2, n + 2))  # 2 to 1001
        self.assertEqual(first_missing_positive(nums), 1)

    def test_large_n_missing_middle(self):
        """Large array: 1..500,502..1001 → missing 501"""
        nums = list(range(1, 501)) + list(range(502, 1002))
        self.assertEqual(first_missing_positive(nums), 501)

    def test_with_zeros(self):
        """[0, 0, 0] → no positive → 1 missing"""
        self.assertEqual(first_missing_positive([0, 0, 0]), 1)

    def test_mixed_with_large_numbers(self):
        """[100, -50, 200, 1] → only 1 is valid → missing 2"""
        self.assertEqual(first_missing_positive([100, -50, 200, 1]), 2)

    def test_only_two_elements(self):
        """[2, 1] → both present → missing 3"""
        self.assertEqual(first_missing_positive([2, 1]), 3)

    def test_two_elements_missing_one(self):
        """[3, 4] → missing 1"""
        self.assertEqual(first_missing_positive([3, 4]), 1)


    def test_negative_and_zero_only(self):
        """[-10, -1, 0] → no positives → missing 1"""
        self.assertEqual(first_missing_positive([-10, -1, 0]), 1)

    def test_single_large_positive(self):
        """[100000] → missing 1 (since 1 not present)"""
        self.assertEqual(first_missing_positive([100000]), 1)

    def test_boundary_n(self):
        """n = 10^5, all 1..99999 present → missing 100000"""
        n = 100000
        nums = list(range(1, n))  # 1 to 99999
        self.assertEqual(first_missing_positive(nums), n)

    def test_permuted_large_array(self):
        """Large shuffled array with one missing"""
        import random
        n = 5000
        missing = 42
        nums = list(range(1, n + 1))
        nums.remove(missing)
        random.shuffle(nums)
        self.assertEqual(first_missing_positive(nums), missing)

    def test_performance_stress(self):
        """Stress test with 10^5 random integers"""
        import random
        # Generate 100k random integers in [-1e5, 1e5]
        nums = [random.randint(-100000, 100000) for _ in range(100000)]
        result = first_missing_positive(nums)
        # Just verify it runs and returns int
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)



if __name__ == '__main__':
    unittest.main()


