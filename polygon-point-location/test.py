import unittest
import sys
from io import StringIO
from solution import PolygonPointLocation, solve_polygon_point_location

class TestPolygonPointLocation(unittest.TestCase):
    
    def test_square_polygon(self):
        vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
        polygon = PolygonPointLocation(vertices)
        
        # Test inside points
        self.assertEqual(polygon.query_point(2, 2), "INSIDE")
        self.assertEqual(polygon.query_point(1, 1), "INSIDE")
        self.assertEqual(polygon.query_point(3, 3), "INSIDE")
        
        # Test outside points
        self.assertEqual(polygon.query_point(5, 5), "OUTSIDE")
        self.assertEqual(polygon.query_point(-1, 2), "OUTSIDE")
        self.assertEqual(polygon.query_point(2, 5), "OUTSIDE")
        
        # Test boundary points
        self.assertEqual(polygon.query_point(2, 0), "BOUNDARY")
        self.assertEqual(polygon.query_point(4, 2), "BOUNDARY")
        self.assertEqual(polygon.query_point(0, 3), "BOUNDARY")
        self.assertEqual(polygon.query_point(2, 4), "BOUNDARY")
    
    def test_triangle_polygon(self):
        vertices = [(0, 0), (4, 0), (2, 4)]
        polygon = PolygonPointLocation(vertices)
        
        # Test inside points
        self.assertEqual(polygon.query_point(2, 2), "INSIDE")
        self.assertEqual(polygon.query_point(1, 1), "INSIDE")
        
        # Test outside points
        self.assertEqual(polygon.query_point(3, 3), "OUTSIDE")
        self.assertEqual(polygon.query_point(0, 2), "OUTSIDE")
        
        # Test boundary points
        self.assertEqual(polygon.query_point(2, 0), "BOUNDARY")
        self.assertEqual(polygon.query_point(1, 2), "BOUNDARY")
    
    def test_dynamic_updates(self):
        vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
        polygon = PolygonPointLocation(vertices)
        
        # Initial state
        self.assertEqual(polygon.query_point(2, 2), "INSIDE")
        self.assertEqual(polygon.query_point(5, 2), "OUTSIDE")
        
        # Update vertex
        polygon.update_vertex(1, 6, 0)  # Change (4,0) to (6,0)
        
        # After update
        self.assertEqual(polygon.query_point(3, 2), "INSIDE")
        self.assertEqual(polygon.query_point(5, 1), "INSIDE")
        self.assertEqual(polygon.query_point(2, 0), "BOUNDARY")

def run_polygon_test():
    """Run specific test for polygon point location"""
    test_input = """4
0 0
4 0
4 4
0 4
7
QUERY 2 2
QUERY 5 5
QUERY 2 0
UPDATE 1 6 0
QUERY 3 2
QUERY 5 1
QUERY 2 0"""
    
    print("=== Running Polygon Point Location Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_polygon_point_location()
        print("Results:")
        for result in results:
            print(result)
        
        print("\nExpected Output:")
        print("INSIDE")
        print("OUTSIDE")
        print("BOUNDARY")
        print("INSIDE")
        print("OUTSIDE")
        print("BOUNDARY")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_polygon_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)