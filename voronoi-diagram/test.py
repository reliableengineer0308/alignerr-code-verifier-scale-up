import unittest
import sys
from io import StringIO
from solution import VoronoiDiagram, Point, solve_voronoi

class TestVoronoiDiagram(unittest.TestCase):
    
    def test_square_sites(self):
        sites = [
            Point(0, 0),  # site 0
            Point(4, 0),  # site 1
            Point(4, 4),  # site 2
            Point(0, 4),  # site 3
            Point(2, 2)   # site 4
        ]
        
        voronoi = VoronoiDiagram(sites)
        
        # Test various query points
        self.assertEqual(voronoi.find_closest_site(Point(1, 1)), 0)  # Close to site 0
        self.assertEqual(voronoi.find_closest_site(Point(3, 3)), 2)  # Close to center site 4
        self.assertEqual(voronoi.find_closest_site(Point(5, 5)), 2)  # Closest to site 1 (diagonal)
        self.assertEqual(voronoi.find_closest_site(Point(2, 0)), 0)  # On boundary, choose smaller index
        self.assertEqual(voronoi.find_closest_site(Point(2, 4)), 2)  # Close to site 2
        self.assertEqual(voronoi.find_closest_site(Point(0, 2)), 0)  # Close to site 3
    
    def test_three_sites(self):
        sites = [
            Point(0, 0),  # site 0
            Point(3, 0),  # site 1
            Point(1, 3)   # site 2
        ]
        
        voronoi = VoronoiDiagram(sites)
        
        self.assertEqual(voronoi.find_closest_site(Point(1, 1)), 0)  # Closer to site 0
        self.assertEqual(voronoi.find_closest_site(Point(2, 1)), 1)  # Closer to site 1
        self.assertEqual(voronoi.find_closest_site(Point(1, 2)), 2)  # Closer to site 2
    
    def test_two_sites(self):
        sites = [
            Point(0, 0),  # site 0
            Point(2, 2)   # site 1
        ]
        
        voronoi = VoronoiDiagram(sites)
        
        self.assertEqual(voronoi.find_closest_site(Point(1, 0)), 0)  # Closer to site 0
        self.assertEqual(voronoi.find_closest_site(Point(1, 2)), 1)  # Closer to site 1
        # On the perpendicular bisector - should choose smaller index
        self.assertEqual(voronoi.find_closest_site(Point(1, 1)), 0)

def run_voronoi_test():
    """Run specific test for Voronoi diagram"""
    test_input = """5
0 0
4 0
4 4
0 4
2 2
6
1 1
3 3
5 5
2 0
2 4
0 2"""
    
    print("=== Running Voronoi Diagram Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_voronoi()
        print("Results:")
        for result in results:
            print(result)
        
        print("\nExpected Output:")
        print("0")
        print("2")
        print("2")
        print("0")
        print("2")
        print("0")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_voronoi_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)