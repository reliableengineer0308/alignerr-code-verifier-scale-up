import unittest
from solution import merge

class TestMergeIntervals(unittest.TestCase):
    def test_basic_overlap(self):
        self.assertEqual(merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])

    def test_touching_intervals(self):
        self.assertEqual(merge([[1,4],[4,5]]), [[1,5]])

    def test_empty_input(self):
        self.assertEqual(merge([]), [])

    def test_single_interval(self):
        self.assertEqual(merge([[1,2]]), [[1,2]])

    def test_no_overlaps(self):
        self.assertEqual(merge([[1,2],[3,4],[5,6]]), [[1,2],[3,4],[5,6]])

    def test_all_overlap(self):
        self.assertEqual(merge([[1,5],[2,4],[3,6]]), [[1,6]])

    def test_zero_length_interval(self):
        self.assertEqual(merge([[5,5],[1,3]]), [[1,3],[5,5]])

    def test_reverse_order_input(self):
        # Algorithm should sort internally
        self.assertEqual(merge([[8,10],[1,3],[2,6]]), [[1,6],[8,10]])

    def test_duplicate_intervals(self):
        self.assertEqual(merge([[1,2],[1,2]]), [[1,2]])

    def test_nested_intervals(self):
        self.assertEqual(merge([[1,10],[2,3],[4,5]]), [[1,10]])

if __name__ == '__main__':
    unittest.main()
