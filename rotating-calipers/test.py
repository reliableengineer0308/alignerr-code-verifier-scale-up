import unittest
import sys
from io import StringIO
from solution import RotatingCalipers, Point, solve_rotating_calipers

class TestRotatingCalipers(unittest.TestCase):
    
    def test_collinear_points(self):
        points = [
            Point(0, 0), Point(1, 1), Point(2, 2),
            Point(3, 3), Point(4, 4), Point(5, 5)
        ]
        
        solver = RotatingCalipers()
        max_dist_sq, p1, p2 = solver.maximum_distance(points)
        
        self.assertEqual(max_dist_sq, 50)  # (0,0) to (5,5): 5^2 + 5^2 = 50
        self.assertEqual((p1, p2), (Point(0, 0), Point(5, 5)))
    
    def test_square_points(self):
        points = [
            Point(0, 0), Point(4, 0), Point(4, 4),
            Point(0, 4), Point(1, 1), Point(2, 2),
            Point(3, 3), Point(2, 0)
        ]
        
        solver = RotatingCalipers()
        max_dist_sq, p1, p2 = solver.maximum_distance(points)
        
        self.assertEqual(max_dist_sq, 32)  # (0,0) to (4,4): 4^2 + 4^2 = 32
        # Could be (0,0)-(4,4) or (0,4)-(4,0)
        possible_pairs = [(Point(0, 0), Point(4, 4)), (Point(0, 4), Point(4, 0))]
        self.assertIn((p1, p2), possible_pairs)
    
    def test_two_points(self):
        points = [Point(0, 0), Point(3, 4)]
        solver = RotatingCalipers()
        max_dist_sq, p1, p2 = solver.maximum_distance(points)
        
        self.assertEqual(max_dist_sq, 25)  # 3^2 + 4^2 = 25
    
    def test_triangle(self):
        points = [Point(0, 0), Point(4, 0), Point(2, 4)]
        solver = RotatingCalipers()
        max_dist_sq, p1, p2 = solver.maximum_distance(points)
        
        # Maximum distance should be between base points
        self.assertEqual(max_dist_sq, 20)

def run_rotating_calipers_test():
    """Run specific test for rotating calipers"""
    test_input = """2
6
0 0
1 1
2 2
3 3
4 4
5 5
8
0 0
4 0
4 4
0 4
1 1
2 2
3 3
2 0"""
    
    print("=== Running Rotating Calipers Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_rotating_calipers()
        print("Results:")
        for result in results:
            print(result)
        
        print("\nExpected Output:")
        print("Case #1: 50")
        print("0 0")
        print("5 5")
        print("Case #2: 32")
        print("0 0")
        print("4 4")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_rotating_calipers_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)