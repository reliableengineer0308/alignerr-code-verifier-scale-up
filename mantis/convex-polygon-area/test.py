import unittest
from solution import polygon_area
import math
import random

class TestPolygonArea(unittest.TestCase):
    """Test suite for polygon_area() function using Shoelace formula."""

    def test_rectangle(self):
        """Test a standard 4x3 rectangle (area = 12.0)."""
        vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
        self.assertEqual(polygon_area(vertices), 12.0)

    def test_triangle(self):
        """Test a triangle with base=2, height=3 (area = 3.0)."""
        vertices = [(1, 1), (3, 1), (2, 4)]
        self.assertEqual(polygon_area(vertices), 3.0)

    def test_rotated_square(self):
        """Test a rotated square (diagonal=2, area = 2.0)."""
        vertices = [(0, 0), (1, 1), (0, 2), (-1, 1)]
        self.assertEqual(polygon_area(vertices), 2.0)

    def test_clockwise_counterclockwise(self):
        """Verify both CW and CCW vertex orders yield same area."""
        # Counter-clockwise (CCW)
        ccw = [(0, 0), (2, 0), (2, 2), (0, 2)]
        # Clockwise (CW)
        cw = [(0, 0), (0, 2), (2, 2), (2, 0)]
        
        self.assertAlmostEqual(polygon_area(ccw), 4.0, places=6)
        self.assertAlmostEqual(polygon_area(cw), 4.0, places=6)

    def test_degenerate_cases(self):
        """Test edge cases: single point and collinear points."""
        # Single point (area = 0.0)
        single_point = [(5, 5)]
        self.assertEqual(polygon_area(single_point), 0.0)
        
        # Collinear points (line segment, area = 0.0)
        collinear = [(0, 0), (1, 0), (2, 0), (3, 0)]
        self.assertEqual(polygon_area(collinear), 0.0)

    def test_large_coordinates(self):
        """Test large coordinate values (2000x2000 square)."""
        vertices = [(-1000, -1000), (1000, -1000), (1000, 1000), (-1000, 1000)]
        expected = 4_000_000.0  # 2000 × 2000
        self.assertEqual(polygon_area(vertices), expected)

    def test_negative_coordinates(self):
        """Test polygons with negative coordinates."""
        vertices = [(-3, -2), (-1, -2), (-2, 1)]
        # Triangle with base=2, height=3 → area=3.0
        self.assertEqual(polygon_area(vertices), 3.0)

    def test_complex_polygon(self):
        """Test a regular pentagon (5 vertices)."""
        n = 5
        radius = 2
        vertices = []
        for i in range(n):
            angle = 2 * math.pi * i / n
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            vertices.append((x, y))
        
        # Area of regular pentagon: (5/2) × R² × sin(2π/5)
        expected = (5 / 2) * (radius ** 2) * math.sin(2 * math.pi / 5)
        self.assertAlmostEqual(polygon_area(vertices), expected, places=5)


    def test_floating_point_precision(self):
        """Test floating-point precision with fractional coordinates."""
        vertices = [(0.1, 0.2), (3.1, 0.2), (3.1, 2.2), (0.1, 2.2)]
        expected = 3.0 * 2.0  # width × height
        self.assertAlmostEqual(polygon_area(vertices), expected, places=6)

    def test_self_intersecting_polygon(self):
        """Test self-intersecting polygon (bowtie shape). Shoelace formula returns net area, 
        where overlapping regions with opposite orientations cancel out."""
        vertices = (0, 0), (2, 2), (0, 4), (2, 0)
        
        # Manual calculation:
        # (0*2 - 2*0) + (2*4 - 0*2) + (0*0 - 2*4) + (2*0 - 0*0) = 0 + 8 - 8 + 0 = 0
        # Area = 0.5 * |0| = 0.0
        expected = 0.0
        
        self.assertAlmostEqual(polygon_area(vertices), expected, places=6)

    def test_random_convex_polygon(self):
        """Test randomly generated convex polygon."""
        random.seed(42)
        n = 6
        radius = 10
        angles = sorted(random.uniform(0, 2 * math.pi) for _ in range(n))
        vertices = []
        
        for angle in angles:
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            vertices.append((round(x, 6), round(y, 6)))
        
        
        area = polygon_area(vertices)
        self.assertGreater(area, 0.0)  # Area must be positive
        
        # Test rotation invariance
        rotated = vertices[1:] + vertices[:1]
        self.assertAlmostEqual(polygon_area(rotated), area, places=6)

    def test_edge_coordinate_limits(self):
        """Test minimal and maximal coordinate values."""
        # Minimal coordinates
        min_vertices = [(-1000, -1000), (-999, -1000), (-1000, -999)]
        min_area = 0.5
        self.assertAlmostEqual(polygon_area(min_vertices), min_area, places=6)
        
        
        # Maximal coordinates
        max_vertices = [(1000, 1000), (999, 1000), (1000, 999)]
        max_area = 0.5
        self.assertAlmostEqual(polygon_area(max_vertices), max_area, places=6)


if __name__ == "__main__":
    unittest.main()
