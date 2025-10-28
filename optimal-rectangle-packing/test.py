import unittest
from solution import optimal_rectangle_packing


class TestOptimalRectanglePacking(unittest.TestCase):


    def test_empty_input(self):
        """Empty input should return area 0 and empty placement."""
        area, placement = optimal_rectangle_packing([])
        self.assertEqual(area, 0)
        self.assertEqual(placement, [])


    def test_single_rectangle(self):
        """Single rectangle: area equals its own area."""
        rectangles = [(4, 5)]
        area, placement = optimal_rectangle_packing(rectangles)
        self.assertEqual(area, 20)  # 4 * 5
        self.assertEqual(len(placement), 1)
        self.assertEqual(placement[0], (0, 0, 4, 5))

    def test_two_non_overlapping(self):
        """Two rectangles that fit side by side."""
        rectangles = [(2, 3), (3, 2)]
        area, placement = optimal_rectangle_packing(rectangles)
        # Optimal: place side by side → width=5, height=3 → area=15
        expected_area = 15
        self.assertLessEqual(area, expected_area)
        # Verify no overlap
        self._assert_no_overlap(placement)

    def test_identical_rectangles(self):
        """Four 2x2 rectangles: should pack into 4x4 square (area=16)."""
        rectangles = [(2, 2)] * 4
        area, placement = optimal_rectangle_packing(rectangles)
        self.assertLessEqual(area, 16)
        self._assert_no_overlap(placement)
        # Check all rectangles are placed
        self.assertEqual(len(placement), 4)

    def test_tall_and_wide(self):
        """Mix of tall and wide rectangles."""
        rectangles = [(1, 6), (6, 1), (3, 3)]
        area, placement = optimal_rectangle_packing(rectangles)
        # Theoretical minimum area: sum of areas = 6 + 6 + 9 = 21
        # Actual packing may need more due to geometry
        self.assertGreaterEqual(area, 21)
        self._assert_no_overlap(placement)

    def test_nested_fit(self):
        """Small rectangle fits inside gap of larger ones."""
        rectangles = [(5, 5), (2, 2), (3, 1)]
        area, placement = optimal_rectangle_packing(rectangles)
        # 5x5 dominates; others should fit around/inside
        self.assertGreaterEqual(area, 25)
        self.assertLessEqual(area, 40)  # Loose upper bound
        self._assert_no_overlap(placement)

    def test_large_heuristic_fallback(self):
        """Test heuristic (FFD) for >10 rectangles."""
        # 12 rectangles (forces heuristic mode)
        rectangles = [(2, 2)] * 12
        area, placement = optimal_rectangle_packing(rectangles)
        # Each 2x2 = 4 area; total min area = 48
        # Heuristic may use more due to inefficiency
        self.assertGreaterEqual(area, 48)
        self.assertEqual(len(placement), 12)
        self._assert_no_overlap(placement)


    def test_edge_case_thin_rectangles(self):
        """Very thin rectangles (e.g., 1x10)."""
        rectangles = [(1, 10), (10, 1)]
        area, placement = optimal_rectangle_packing(rectangles)
        self.assertGreaterEqual(area, 20)
        self.assertLessEqual(area, 110)
        self._assert_no_overlap(placement)


    def _assert_no_overlap(self, placement):
        """Helper: check that no two rectangles in placement overlap."""
        for i, rect1 in enumerate(placement):
            for j, rect2 in enumerate(placement):
                if i == j:
                    continue
                x1, y1, w1, h1 = rect1
                x2, y2, w2, h2 = rect2
                # Check if rect1 and rect2 overlap
                if not (x1 + w1 <= x2 or x2 + w2 <= x1 or
                        y1 + h1 <= y2 or y2 + h2 <= y1):
                    self.fail(f"Overlap detected between rect {i} {rect1} and rect {j} {rect2}")


if __name__ == '__main__':
    unittest.main()
