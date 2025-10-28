import unittest
from solution import closest_pair, euclidean_distance
import math

class TestClosestPair(unittest.TestCase):

    def test_basic_case(self):
        """Test with simple 4-point set."""
        points = [(0, 0), (1, 1), (2, 2), (3, 3)]
        dist, pair = closest_pair(points)
        expected_dist = math.sqrt(2)  # √2 ≈ 1.4142135623730951
        self.assertAlmostEqual(dist, expected_dist, places=10)
        self.assertIn(pair, [((0, 0), (1, 1)), ((1, 1), (2, 2)), ((2, 2), (3, 3))])


    def test_random_points(self):
        """Test with arbitrary point distribution."""
        points = [(1, 2), (4, 6), (7, 8), (2, 1)]
        dist, pair = closest_pair(points)
        expected_dist = math.sqrt(2)
        self.assertAlmostEqual(dist, expected_dist, places=10)
        # Allow both orderings of the pair
        self.assertTrue(pair == ((1, 2), (2, 1)) or pair == ((2, 1), (1, 2)))


    def test_collinear_points(self):
        """Test when all points lie on a line."""
        points = [(0, 5), (3, 5), (7, 5), (10, 5)]
        dist, pair = closest_pair(points)
        self.assertAlmostEqual(dist, 3.0, places=10)  # (0,5)-(3,5)
        self.assertIn(pair, [((0, 5), (3, 5)), ((3, 5), (7, 5)), ((7, 5), (10, 5))])


    def test_large_coordinates(self):
        """Test with large coordinate values."""
        points = [(-1000000, -1000000), (1000000, 1000000), (0, 0)]
        dist, pair = closest_pair(points)
        # Distance between (-1e6,-1e6) and (0,0)
        expected_dist = math.sqrt(2 * (10**12))
        self.assertAlmostEqual(dist, expected_dist, places=5)
        self.assertIn(pair, [((-1000000, -1000000), (0, 0)), ((0, 0), (-1000000, -1000000))])


    def test_minimal_input(self):
        """Test with exactly 2 points."""
        points = [(0, 0), (1, 1)]
        dist, pair = closest_pair(points)
        expected_dist = math.sqrt(2)
        self.assertAlmostEqual(dist, expected_dist, places=10)
        self.assertEqual(pair, ((0, 0), (1, 1)))

    def test_three_points(self):
        """Test with 3 points (smallest non-trivial case)."""
        points = [(0, 0), (1, 0), (2, 0)] # All on one line
        # Minimum distance: (0.0) - (1.0) = 1.0
        dist, pair = closest_pair(points)
        # Closest: (0,0)-(1,0) with distance 1.0
        self.assertAlmostEqual(dist, 1.0, places=10)
        self.assertIn(pair, [((0, 0), (1, 0)), ((1, 0), (0, 0))])


    def test_duplicate_points(self):
        """Test handling of duplicate points (should be treated as one)."""
        # According to problem statement, all points are distinct,
        # but we test robustness
        points = [(0, 0), (0, 0), (1, 1)]  # Duplicate (0,0)
        dist, pair = closest_pair(points)
        self.assertAlmostEqual(dist, 0.0, places=10)  # Distance between duplicates
        self.assertEqual(pair[0], pair[1])  # Both points are the same

    def test_vertical_alignment(self):
        """Test points aligned vertically."""
        points = [(5, 0), (5, 3), (5, 7), (5, 10)]
        dist, pair = closest_pair(points)
        self.assertAlmostEqual(dist, 3.0, places=10)  # (5,0)-(5,3)
        self.assertIn(pair, [((5, 0), (5, 3)), ((5, 3), (5, 7)), ((5, 7), (5, 10))])


    def test_single_point(self):
        """Test edge case with single point."""
        points = [(42, 42)]
        dist, pair = closest_pair(points)
        self.assertIsNone(dist)
        self.assertIsNone(pair)


    def test_empty_input(self):
        """Test empty input."""
        points = []
        dist, pair = closest_pair(points)
        self.assertIsNone(dist)
        self.assertIsNone(pair)


    def test_precision_boundary(self):
        """Test floating-point precision at boundary."""
        # Two very close points
        points = [(0.0, 0.0), (1e-10, 1e-10)]
        dist, pair = closest_pair(points)
        expected_dist = math.sqrt(2 * (1e-20))
        self.assertLess(abs(dist - expected_dist), 1e-10)
        self.assertEqual(pair, ((0.0, 0.0), (1e-10, 1e-10)))


if __name__ == "__main__":
    unittest.main()
