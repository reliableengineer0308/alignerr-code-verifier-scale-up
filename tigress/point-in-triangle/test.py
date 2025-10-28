import unittest
from solution import is_point_in_triangle

class TestPointInTriangle(unittest.TestCase):
    
    def test_inside(self):
        """Point strictly inside triangle."""
        p = (0.5, 0.5)
        v1, v2, v3 = (0.0, 0.0), (2.0, 0.0), (0.0, 2.0)
        self.assertEqual(is_point_in_triangle(p, v1, v2, v3), "inside")
    
    
    def test_edge(self):
        """Point on triangle edge."""
        p = (1.0, 0.0)  # On base
        v1, v2, v3 = (0.0, 0.0), (2.0, 0.0), (0.0, 2.0)
        self.assertEqual(is_point_in_triangle(p, v1, v2, v3), "edge")
        
    def test_vertex(self):
        """Point coincides with vertex."""
        p = (0.0, 0.0)
        v1, v2, v3 = (0.0, 0.0), (2.0, 0.0), (0.0, 2.0)
        self.assertEqual(is_point_in_triangle(p, v1, v2, v3), "edge")  # Vertex is on edge
        
    def test_outside(self):
        """Point outside triangle."""
        p = (3.0, 3.0)
        v1, v2, v3 = (0.0, 0.0), (2.0, 0.0), (0.0, 2.0)
        self.assertEqual(is_point_in_triangle(p, v1, v2, v3), "outside")
        
    def test_degenerate_triangle(self):
        """Degenerate (line) triangle."""
        p = (1.0, 0.0)
        v1, v2, v3 = (0.0, 0.0), (2.0, 0.0), (4.0, 0.0)  # Collinear
        # Any point will be on edge or outside
        result = is_point_in_triangle(p, v1, v2, v3)
        self.assertIn(result, ["edge", "outside"])
        
    def test_float_precision(self):
        """Test with floating-point imprecision."""
        # Point very close to edge
        p = (1.0 + 1e-11, 0.0)
        v1, v2, v3 = (0.0, 0.0), (2.0, 0.0), (0.0, 2.0)
        self.assertEqual(is_point_in_triangle(p, v1, v2, v3), "edge")
        
    def test_large_coordinates(self):
        """Test with large coordinate values."""
        p = (300.0, 300.0)
        v1, v2, v3 = (0.0, 0.0), (1000.0, 0.0), (0.0, 1000.0)
        self.assertEqual(is_point_in_triangle(p, v1, v2, v3), "inside")
        
    def test_negative_coordinates(self):
        """Test with negative coordinates."""
        p = (-1.5, -1.5)
        v1, v2, v3 = (-2.0, -2.0), (0.0, -2.0), (-2.0, 0.0)
        self.assertEqual(is_point_in_triangle(p, v1, v2, v3), "inside")


if __name__ == "__main__":
    unittest.main()
