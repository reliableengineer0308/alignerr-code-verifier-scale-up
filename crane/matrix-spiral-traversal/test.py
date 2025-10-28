import unittest
from solution import spiral_order

class TestSpiralOrder(unittest.TestCase):

    def test_normal_3x3(self):
        """Test with standard 3x3 matrix."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(spiral_order(matrix), expected)

    def test_rectangular_3x4(self):
        """Test with rectangular 3x4 matrix."""
        matrix = [
            [1,  2,  3,  4],
            [5,  6,  7,  8],
            [9, 10, 11, 12]
        ]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(spiral_order(matrix), expected)

    def test_single_row(self):
        """Test with single row matrix."""
        matrix = [[1, 2, 3, 4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(spiral_order(matrix), expected)


    def test_single_column(self):
        """Test with single column matrix."""
        matrix = [[1], [2], [3], [4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(spiral_order(matrix), expected)

    def test_single_element(self):
        """Test with 1x1 matrix."""
        matrix = [[42]]
        expected = [42]
        self.assertEqual(spiral_order(matrix), expected)


    def test_empty_matrix(self):
        """Test with empty matrix."""
        matrix = []
        expected = []
        self.assertEqual(spiral_order(matrix), expected)

    def test_empty_row(self):
        """Test with matrix containing empty row."""
        matrix = [[]]
        expected = []
        self.assertEqual(spiral_order(matrix), expected)

    def test_2x2(self):
        """Test with minimal 2x2 matrix."""
        matrix = [[1, 2], [3, 4]]
        expected = [1, 2, 4, 3]
        self.assertEqual(spiral_order(matrix), expected)

if __name__ == "__main__":
    unittest.main()
