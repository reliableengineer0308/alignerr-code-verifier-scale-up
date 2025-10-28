import unittest
from solution import trap

class TestTrappingRainWater(unittest.TestCase):

    def test_example_1(self):
        """Test with classic example from problem."""
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(trap(height), 6)

    def test_example_2(self):
        """Test with another sample input."""
        height = [4, 2, 0, 3, 2, 5]
        self.assertEqual(trap(height), 9)

    def test_empty_array(self):
        """Test empty input."""
        height = []
        self.assertEqual(trap(height), 0)

    def test_single_bar(self):
        """Test single element array."""
        height = [5]
        self.assertEqual(trap(height), 0)

    def test_two_bars(self):
        """Test two elements - no water can be trapped."""
        height = [2, 3]
        self.assertEqual(trap(height), 0)

    def test_ascending_order(self):
        """Test strictly increasing sequence."""
        height = [1, 2, 3, 4, 5]
        self.assertEqual(trap(height), 0)

    def test_descending_order(self):
        """Test strictly decreasing sequence."""
        height = [5, 4, 3, 2, 1]
        self.assertEqual(trap(height), 0)

    def test_flat_terrain(self):
        """Test all same heights."""
        height = [3, 3, 3, 3]
        self.assertEqual(trap(height), 0)

    def test_deep_valley(self):
        """Test deep valley between two high bars."""
        height = [5, 1, 1, 1, 5]
        self.assertEqual(trap(height), 12)  # 4 units each in 3 middle positions

    def test_small_valley(self):
        """Test minimal valley."""
        height = [2, 0, 1]
        self.assertEqual(trap(height), 1)

if __name__ == "__main__":
    unittest.main()
