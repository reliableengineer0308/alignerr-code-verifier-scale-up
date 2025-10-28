import unittest
import sys
from io import StringIO
from solution import BoundedVoronoi, Point, solve_bounded_voronoi

class TestBoundedVoronoi(unittest.TestCase):
    
    def test_square_sites(self):
        sites = [
            Point(0, 0),
            Point(4, 0),
            Point(4, 4),
            Point(0, 4)
        ]
        
        voronoi = BoundedVoronoi(sites)
        vertices, edges = voronoi.compute_bounded_voronoi()
        
        # Should have vertices and edges
        self.assertGreater(len(vertices), 0)
        self.assertGreater(len(edges), 0)
    
    def test_triangle_sites(self):
        sites = [
            Point(0, 0),
            Point(3, 0),
            Point(1, 3)
        ]
        
        voronoi = BoundedVoronoi(sites)
        vertices, edges = voronoi.compute_bounded_voronoi()
        
        # Should have vertices and edges
        self.assertGreater(len(vertices), 0)
        self.assertGreater(len(edges), 0)
    
    def test_four_points(self):
        sites = [
            Point(0, 0),
            Point(2, 0),
            Point(2, 2),
            Point(0, 2)
        ]
        
        voronoi = BoundedVoronoi(sites)
        vertices, edges = voronoi.compute_bounded_voronoi()
        
        # Should have vertices and edges
        self.assertGreater(len(vertices), 0)
        self.assertGreater(len(edges), 0)

def run_bounded_voronoi_test():
    """Run specific test for bounded Voronoi"""
    test_input = """4
0 0
4 0
4 4
0 4"""
    
    print("=== Running Bounded Voronoi Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_bounded_voronoi()
        print("Results:")
        for result in results:
            print(result)
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_bounded_voronoi_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)