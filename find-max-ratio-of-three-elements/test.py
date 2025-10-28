import unittest
from solution import maxRatioOfThree

class TestMaxRatioOfThree(unittest.TestCase):
    def test_basic_case(self):
        self.assertAlmostEqual(maxRatioOfThree([2, 3, 4, 8]), 8/(2*3), places=6)
        # 8/6 = 1.333... wait no: 8/(2×3)=8/6≈1.333? No: 8/6=1.333 but expected was 0.666?
        # Correction: 8/(2×3) = 8/6 ≈ 1.333 → but earlier said 0.666. Mistake!
        # Let's recalculate: 8/(2×3)=8/6=4/3≈1.333
        # So expected output should be 1.333333
        self.assertAlmostEqual(maxRatioOfThree([2,3,4,8]), 1.333333, places=5)
        
    def test_all_ones(self):
        self.assertAlmostEqual(maxRatioOfThree([1, 1, 1]), 1.0, places=6)
        # 1 / (1 * 1) = 1.0


    def test_three_elements(self):
        self.assertAlmostEqual(maxRatioOfThree([10, 20, 30]), 30 / (10 * 20), places=6)
        # 30 / 200 = 0.15

    def test_single_element(self):
        self.assertEqual(maxRatioOfThree([7]), 0.0)
        # Less than 3 elements → return 0

    def test_four_elements_decreasing(self):
        # nums = [5, 4, 3, 2]
        # Possible triplets:
        # (0,1,2): 3/(5*4) = 0.15
        # (0,1,3): 2/(5*4) = 0.1
        # (0,2,3): 2/(5*3) ≈ 0.133
        # (1,2,3): 2/(4*3) ≈ 0.1667
        self.assertAlmostEqual(maxRatioOfThree([5, 4, 3, 2]), 2 / (4 * 3), places=6)

    def test_large_values(self):
        # Test with large numbers but valid ratio
        self.assertAlmostEqual(maxRatioOfThree([1000, 500, 1000000]), 
                             1000000 / (1000 * 500), places=6)
        # 1e6 / 5e5 = 2.0

    def test_duplicate_values(self):
        # [2, 2, 8] → 8/(2*2) = 2.0
        self.assertAlmostEqual(maxRatioOfThree([2, 2, 8]), 2.0, places=6)

    def test_increasing_sequence(self):
        # [1, 2, 3, 4, 5]
        # Best: (0,1,4) → 5/(1*2) = 2.5
        self.assertAlmostEqual(maxRatioOfThree([1, 2, 3, 4, 5]), 5 / (1 * 2), places=6)

    def test_peak_in_middle(self):
        # [3, 1, 4] → only one triplet: 4/(3*1) ≈ 1.333
        self.assertAlmostEqual(maxRatioOfThree([3, 1, 4]), 4 / (3 * 1), places=6)

    def test_minimum_product_early(self):
        # [1, 100, 100, 50]
        # Best triplet: (i=0, j=1, k=2) → 100 / (1 * 100) = 1.0
        # Not at k=3, because 50 is smaller than 100
        self.assertAlmostEqual(
            maxRatioOfThree([1, 100, 100, 50]),
            100 / (1 * 100),  # = 1.0
            places=6
        )

    def test_precision_boundary(self):
        # Test floating-point precision
        result = maxRatioOfThree([999, 998, 997999])
        expected = 997999 / (999 * 998)
        self.assertAlmostEqual(result, expected, places=6)


if __name__ == '__main__':
    unittest.main()
