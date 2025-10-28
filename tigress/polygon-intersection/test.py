import unittest
import sys
from io import StringIO
from solution import PolygonIntersection, Point, solve_polygon_intersection

class TestPolygonIntersection(unittest.TestCase):
    
    def test_overlapping_squares(self):
        polyA = [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)]
        polyB = [Point(1, 1), Point(5, 1), Point(5, 5), Point(1, 5)]
        
        solver = PolygonIntersection()
        area = solver.intersection_area(polyA, polyB)
        
        self.assertAlmostEqual(area, 9.0, places=2)
    
    def test_contained_polygon(self):
        polyA = [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)]
        polyB = [Point(1, 1), Point(3, 1), Point(3, 3), Point(1, 3)]
        
        solver = PolygonIntersection()
        area = solver.intersection_area(polyA, polyB)
        
        self.assertAlmostEqual(area, 4.0, places=2)
    
    def test_disjoint_polygons(self):
        polyA = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
        polyB = [Point(3, 3), Point(5, 3), Point(5, 5), Point(3, 5)]
        
        solver = PolygonIntersection()
        area = solver.intersection_area(polyA, polyB)
        
        self.assertAlmostEqual(area, 0.0, places=2)
    
    def test_touching_polygons(self):
        polyA = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
        polyB = [Point(2, 0), Point(4, 0), Point(4, 2), Point(2, 2)]
        
        solver = PolygonIntersection()
        area = solver.intersection_area(polyA, polyB)
        
        # Touching at edge should have zero area
        self.assertAlmostEqual(area, 0.0, places=2)

def run_intersection_test():
    """Run specific test for polygon intersection"""
    test_input = """4
0 0
4 0
4 4
0 4
4
1 1
5 1
5 5
1 5"""
    
    print("=== Running Polygon Intersection Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_polygon_intersection()
        print("Results:")
        for result in results:
            print(result)
        
        print("\nExpected Output:")
        print("9.00")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_intersection_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)