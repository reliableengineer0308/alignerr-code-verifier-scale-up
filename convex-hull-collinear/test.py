import unittest
import sys
from io import StringIO
from solution import ConvexHull, Point, solve_convex_hull

class TestConvexHull(unittest.TestCase):
    
    def test_basic_case(self):
        points = [
            Point(0, 0), Point(0, 4), Point(4, 0),
            Point(4, 4), Point(2, 2), Point(1, 1),
            Point(3, 3), Point(2, 0)
        ]
        
        hull_solver = ConvexHull()
        result = hull_solver.convex_hull_with_collinear(points)
        
        self.assertEqual(len(result), 5)
        # Should include boundary points including collinear ones on edges
        self.assertTrue(any(p.x == 2 and p.y == 0 for p in result))  # (2,0) on bottom edge
        # Should NOT include internal collinear points
        self.assertFalse(any(p.x == 2 and p.y == 2 for p in result))  # (2,2) is internal
        self.assertFalse(any(p.x == 1 and p.y == 1 for p in result))  # (1,1) is internal
        self.assertFalse(any(p.x == 3 and p.y == 3 for p in result))  # (3,3) is internal
        
        # Check all points are unique
        self.assertEqual(len(result), len(set(result)))
    
    def test_straight_line(self):
        points = [
            Point(1, 1), Point(2, 2), Point(3, 3),
            Point(4, 4), Point(5, 5), Point(1, 3)
        ]
        
        hull_solver = ConvexHull()
        result = hull_solver.convex_hull_with_collinear(points)
        
        # All extreme points should be in hull
        self.assertIn(Point(1, 1), result)
        self.assertIn(Point(5, 5), result)
        self.assertIn(Point(1, 3), result)
        
        # Check no duplicates
        self.assertEqual(len(result), len(set(result)))
    
    def test_single_point(self):
        points = [Point(1, 1)]
        hull_solver = ConvexHull()
        result = hull_solver.convex_hull_with_collinear(points)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], Point(1, 1))
    
    def test_two_points(self):
        points = [Point(0, 0), Point(1, 1)]
        hull_solver = ConvexHull()
        result = hull_solver.convex_hull_with_collinear(points)
        
        self.assertEqual(len(result), 2)
        self.assertIn(Point(0, 0), result)
        self.assertIn(Point(1, 1), result)
    
    def test_rectangle_with_internal_collinear(self):
        points = [
            Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4),
            Point(2, 0), Point(4, 2), Point(2, 4), Point(0, 2),
            Point(1, 1), Point(3, 3)
        ]
        
        hull_solver = ConvexHull()
        result = hull_solver.convex_hull_with_collinear(points)
        
        # Should include all boundary points including collinear ones
        boundary_points = {Point(0,0), Point(4,0), Point(4,4), Point(0,4),
                          Point(2,0), Point(4,2), Point(2,4), Point(0,2)}
        
        for bp in boundary_points:
            self.assertIn(bp, result)
        
        # Internal points should not be in hull
        self.assertNotIn(Point(1, 1), result)
        self.assertNotIn(Point(3, 3), result)

def run_convex_hull_test():
    """Run specific test for convex hull"""
    test_input = """2
8
0 0
0 4
4 0
4 4
2 2
1 1
3 3
2 0
6
1 1
2 2
3 3
4 4
5 5
1 3"""
    
    print("=== Running Convex Hull Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_convex_hull()
        print("Results:")
        for result in results:
            print(result)
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_convex_hull_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)