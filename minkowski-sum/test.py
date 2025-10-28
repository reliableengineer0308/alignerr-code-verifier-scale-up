import unittest
import sys
from io import StringIO
from solution import MinkowskiSum, Point, solve_minkowski_sum, cross

class TestMinkowskiSum(unittest.TestCase):
    
    def test_square_and_triangle(self):
        polyA = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
        polyB = [Point(0, 0), Point(1, 0), Point(0, 1)]
        
        solver = MinkowskiSum()
        result = solver.minkowski_sum(polyA, polyB)
        
        # Result should be a convex polygon with 5 vertices (pentagon)
        self.assertEqual(len(result), 5)  # 수정: 6 → 5
        
        # Check specific expected points
        expected_points = {
            Point(0,0), Point(3,0), Point(3,2), 
            Point(2,3), Point(0,3)
        }
        self.assertEqual(set(result), expected_points)
        
        # Check that all points are in counter-clockwise order
        for i in range(len(result)):
            a = result[i]
            b = result[(i + 1) % len(result)]
            c = result[(i + 2) % len(result)]
            cross_product = cross(a, b, c)
            self.assertGreaterEqual(cross_product, -1e-9)
    
    def test_two_squares(self):
        polyA = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
        polyB = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
        
        solver = MinkowskiSum()
        result = solver.minkowski_sum(polyA, polyB)
        
        # Minkowski sum of two unit squares is a square from (0,0) to (2,2)
        expected_points = {Point(0,0), Point(2,0), Point(2,2), Point(0,2)}
        self.assertEqual(set(result), expected_points)
    
    def test_degenerate_case(self):
        polyA = [Point(0, 0), Point(1, 0)]
        polyB = [Point(0, 0), Point(0, 1)]
        
        solver = MinkowskiSum()
        result = solver.minkowski_sum(polyA, polyB)
        
        # Should form a parallelogram
        self.assertEqual(len(result), 4)

def run_minkowski_test():
    """Run specific test for Minkowski sum"""
    test_input = """4
0 0
2 0
2 2
0 2
3
0 0
1 0
0 1"""
    
    print("=== Running Minkowski Sum Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_minkowski_sum()
        print("Results:")
        for result in results:
            print(result)
        
        print("\nCorrected Expected Output:")
        print("5")
        print("0 0")
        print("3 0") 
        print("3 2")
        print("2 3")
        print("0 3")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_minkowski_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)