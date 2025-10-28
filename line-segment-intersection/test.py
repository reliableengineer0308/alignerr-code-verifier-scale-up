import unittest
from solution import segments_intersect



class TestSegmentIntersection(unittest.TestCase):
    """Test suite for the segments_intersect function."""


    def test_proper_intersection(self):
        """Two segments cross at an interior point (classic 'X' shape)."""
        a1, a2 = (0, 0), (2, 2)
        b1, b2 = (0, 2), (2, 0)
        self.assertTrue(
            segments_intersect(a1, a2, b1, b2),
            "Diagonal segments should intersect at (1,1)"
        )

    def test_endpoint_contact(self):
        """Segments share a single endpoint."""
        a1, a2 = (0, 0), (1, 1)
        b1, b2 = (1, 1), (2, 2)
        self.assertTrue(
            segments_intersect(a1, a2, b1, b2),
            "Segments sharing endpoint (1,1) should intersect"
        )

    def test_collinear_overlap(self):
        """Collinear segments with partial overlap on x-axis."""
        a1, a2 = (0, 0), (3, 0)
        b1, b2 = (1, 0), (2, 0)
        self.assertTrue(
            segments_intersect(a1, a2, b1, b2),
            "Collinear overlapping segments should intersect"
        )

    def test_parallel_non_overlapping(self):
        """Parallel horizontal segments with no overlap."""
        a1, a2 = (0, 0), (1, 0)
        b1, b2 = (2, 1), (3, 1)  # Offset vertically
        self.assertFalse(
            segments_intersect(a1, a2, b1, b2),
            "Parallel non-overlapping segments shouldn't intersect"
        )

    def test_vertical_horizontal_intersection(self):
        """Vertical and horizontal segments intersecting at right angle."""
        a1, a2 = (1, 0), (1, 3)  # Vertical
        b1, b2 = (0, 1), (3, 1)  # Horizontal
        self.assertTrue(
            segments_intersect(a1, a2, b1, b2),
            "Vertical and horizontal should intersect at (1,1)"
        )

    def test_near_miss(self):
        """Critical test: segments very close but NOT intersecting."""
        # Case 1: Clear offset (0.1 units) - should NOT intersect
        a1, a2 = (1, 0), (0, 1)
        b1, b2 = (1.1, 0), (0, 1.1)
        self.assertFalse(
            segments_intersect(a1, a2, b1, b2),
            "Near-miss with 0.1 offset should not intersect"
        )

        # Case 2: Tiny offset (0.001) - still no intersection
        b1_tiny, b2_tiny = (1.001, 0), (0, 1.001)
        self.assertTrue(
            segments_intersect(a1, a2, b1_tiny, b2_tiny),
            "Tiny 0.001 offset should still not intersect"
        )

        # Case 3: Exact touch at endpoint - SHOULD intersect
        b1_touch, b2_touch = (1.0, 0), (0, 1.0)
        self.assertTrue(
            segments_intersect(a1, a2, b1_touch, b2_touch),
            "Exact endpoint contact should count as intersection"
        )

    def test_degenerate_point_on_segment(self):
        """A point (degenerate segment) lying exactly on another segment."""
        point = (1, 1)
        segment_start, segment_end = (0, 0), (2, 2)
        self.assertTrue(
            segments_intersect(point, point, segment_start, segment_end),
            "Point (1,1) lies on diagonal segment (0,0)-(2,2)"
        )


    def test_degenerate_non_contact(self):
        """A point not lying on a segment."""
        point = (3, 3)
        segment_start, segment_end = (0, 0), (1, 1)
        self.assertFalse(
            segments_intersect(point, point, segment_start, segment_end),
            "Point (3,3) is not on segment (0,0)-(1,1)"
        )


    def test_floating_point_precision(self):
        """Test with floating-point coordinates near boundaries."""
        a1, a2 = (0.1, 0.1), (0.9, 0.9)
        b1, b2 = (0.1, 0.9), (0.9, 0.1)
        self.assertTrue(
            segments_intersect(a1, a2, b1, b2),
            "Floating-point diagonal cross should intersect near (0.5,0.5)"
        )


    def test_identical_segments(self):
        """Two identical segments should intersect completely."""
        a1, a2 = (1, 1), (3, 3)
        b1, b2 = (1, 1), (3, 3)
        self.assertTrue(
            segments_intersect(a1, a2, b1, b2),
            "Identical segments intersect fully"
        )


    def test_zero_length_both(self):
        """Both segments are zero-length (points)."""
        p1 = (1, 1)
        p2 = (2, 2)


        # Different points → no intersection
        self.assertFalse(
            segments_intersect(p1, p1, p2, p2),
            "Distinct points do not intersect"
        )


        # Same point → intersection
        self.assertTrue(
            segments_intersect(p1, p1, p1, p1),
            "Same point intersects itself"
        )

    def test_large_coordinates(self):
        """Test robustness with large coordinate values."""
        a1, a2 = (-1000, -1000), (1000, 1000)
        b1, b2 = (-1000, 1000), (1000, -1000)
        self.assertTrue(
            segments_intersect(a1, a2, b1, b2),
            "Large diagonal segments cross at origin"
        )



if __name__ == '__main__':
    unittest.main()
