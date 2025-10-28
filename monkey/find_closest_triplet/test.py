import unittest
from solution import find_closest_triplet


class TestClosestTripletSum(unittest.TestCase):
    def test_example_1(self):
        arr = [-1, 2, 1, -4]
        target = 1
        result, sum_val = find_closest_triplet(arr, target)
        self.assertIsNotNone(result)
        self.assertEqual(sum_val, 2)  # (-1 + 1 + 2) = 2 → |2-1|=1 (minimal)


    def test_all_ones_target_large_negative(self):
        arr = [1, 1, 1, 0]
        target = -100
        result, sum_val = find_closest_triplet(arr, target)
        self.assertIsNotNone(result)
        self.assertEqual(sum_val, 2)  # (1+1+0)=2 is closest possible


    def test_zero_triplet(self):
        arr = [0, 0, 0]
        target = 5
        result, sum_val = find_closest_triplet(arr, target)
        self.assertEqual(result, (0, 0, 0))
        self.assertEqual(sum_val, 0)

    def test_mixed_signs(self):
        arr = [4, 0, 5, -3]
        target = 4
        result, sum_val = find_closest_triplet(arr, target)
        # Possible sums: 1 (4+0-3), 2 (0+5-3), 6 (4+5-3)
        # Closest to 4: both 2 and 6 have |diff|=2 → either is acceptable
        self.assertTrue(abs(sum_val - 4) <= 2)


    def test_sorted_ascending(self):
        arr = [1, 2, 3, 4, 5]
        target = 10
        result, sum_val = find_closest_triplet(arr, target)
        # Best: 2+3+5=10 → exact match
        self.assertEqual(sum_val, 10)


    def test_negative_target(self):
        arr = [-5, -2, -1, 3]
        target = -8
        result, sum_val = find_closest_triplet(arr, target)
        # Best: -5 + -2 + -1 = -8 → exact match
        self.assertEqual(sum_val, -8)


    def test_large_array(self):
        import random
        arr = random.sample(range(-100, 100), 50)  # 50 unique random ints
        target = 0
        result, sum_val = find_closest_triplet(arr, target)
        self.assertIsNotNone(result)
        # Just test that it runs without error and returns valid triplet
        a, b, c = result
        self.assertIn(a, arr)
        self.assertIn(b, arr)
        self.assertIn(c, arr)
        self.assertNotEqual(arr.index(a), arr.index(b))
        self.assertNotEqual(arr.index(b), arr.index(c))
        self.assertNotEqual(arr.index(a), arr.index(c))


    def test_duplicate_values(self):
        arr = [2, 2, 2, 3]
        target = 7
        result, sum_val = find_closest_triplet(arr, target)
        # Best: 2+2+3=7 → exact
        self.assertEqual(sum_val, 7)

        self.assertEqual(set(result), {2, 2, 3})


if __name__ == "__main__":
    unittest.main()
