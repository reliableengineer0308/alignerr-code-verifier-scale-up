import unittest
from solution import max_area

class TestContainerWithMostWater(unittest.TestCase):

    def test_example_1(self):
        """Test case from problem description."""
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(max_area(height), 49)

    def test_minimal_array(self):
        """Test with exactly 2 elements."""
        height = [1, 1]
        self.assertEqual(max_area(height), 1)

    def test_ascending_order(self):
        """Test when heights are in ascending order."""
        height = 1, 2, 3, 4, 5
        # Best pair: (1,4) → min(2,5)*3 = 6
        self.assertEqual(max_area(height), 6)

    def test_descending_order(self):
        """Test when heights are in descending order."""
        height = 5, 4, 3, 2, 1
        # Best pair: (0,3) → min(5,2)*3 = 6
        self.assertEqual(max_area(height), 6)

    def test_all_same_height(self):
        """Test when all lines have the same height."""
        height = [3, 3, 3, 3]
        # Any pair gives area = 3 * (j-i); max at ends: 3*3 = 9
        self.assertEqual(max_area(height), 9)

    def test_single_peak(self):
        """Test with one very tall line in middle."""
        height = [1, 1, 9, 1, 1]
        # Best: between index 0 and 4 → min(1,1)*4 = 4
        # Or between 0 and 2 → min(1,9)*2 = 2; between 2 and 4 → same
        # So max is 4
        self.assertEqual(max_area(height), 4)

    def test_zero_height(self):
        """Test when one line has zero height."""
        height = [0, 5, 3, 8]
        # Line at index 0 can't contribute (height=0)
        # Best between index 1 and 3: min(5,8)*2 = 10
        self.assertEqual(max_area(height), 10)

    def test_large_input(self):
        """Stress test with large input (10^5 elements)."""
        import random
        height = [random.randint(1, 1000) for _ in range(10**4)]
        # Just test that it runs without error
        result = max_area(height)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
