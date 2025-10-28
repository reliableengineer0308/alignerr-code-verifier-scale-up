import unittest
from solution import minCostConnectPoints

class TestMinCostConnectPoints(unittest.TestCase):
    def test_example_1(self):
        points = [[0,0], [2,2], [3,10], [5,2], [7,0]]
        result = minCostConnectPoints(points)
        self.assertEqual(result, 20)

    def test_example_2(self):
        points = [[3,12], [-2,5], [-4,1]]
        result = minCostConnectPoints(points)
        self.assertEqual(result, 18)

    def test_single_point(self):
        points = [[1,1]]
        result = minCostConnectPoints(points)
        self.assertEqual(result, 0)

    def test_two_points(self):
        points = [[0,0], [1,1]]
        result = minCostConnectPoints(points)
        # Manhattan: |0-1| + |0-1| = 2
        self.assertEqual(result, 2)

    def test_three_collinear(self):
        points = [[0,0], [2,0], [4,0]]
        result = minCostConnectPoints(points)
        # Connect: 0→2 (cost=2), 2→4 (cost=2) → total=4
        self.assertEqual(result, 4)

    def test_negative_coordinates(self):
        points = [[-1,-1], [0,0], [1,1]]
        result = minCostConnectPoints(points)
        # 0→1: cost=2, 1→2: cost=2 → total=4 (or similar MST)
        self.assertEqual(result, 4)

    def test_large_coordinates(self):
        points = [[1000000, -1000000], [-1000000, 1000000]]
        result = minCostConnectPoints(points)
        # |1e6 - (-1e6)| + |-1e6 - 1e6| = 2e6 + 2e6 = 4e6
        self.assertEqual(result, 4000000)


if __name__ == "__main__":
    unittest.main()
