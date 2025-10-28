import unittest
import sys
from io import StringIO
from solution import ClosestPairMaintainer, solve_closest_pair

class TestClosestPair(unittest.TestCase):
    
    def test_basic_operations(self):
        maintainer = ClosestPairMaintainer()
        
        maintainer.add_point(0, 0)
        maintainer.add_point(1, 1)
        self.assertEqual(maintainer.query(), 2)
        
        maintainer.add_point(3, 3)
        maintainer.add_point(2, 2)
        self.assertEqual(maintainer.query(), 2)
        
        maintainer.remove_point(1, 1)
        self.assertEqual(maintainer.query(), 2)
    
    def test_single_point(self):
        maintainer = ClosestPairMaintainer()
        maintainer.add_point(0, 0)
        self.assertEqual(maintainer.query(), 0)
    
    def test_no_points(self):
        maintainer = ClosestPairMaintainer()
        self.assertEqual(maintainer.query(), 0)
    
    def test_closer_pair(self):
        maintainer = ClosestPairMaintainer()
        maintainer.add_point(0, 0)
        maintainer.add_point(1, 1)
        maintainer.add_point(0, 1)
        
        # Closest pair should be (0,0)-(0,1) with distance 1
        self.assertEqual(maintainer.query(), 1)

def run_closest_pair_test():
    """Run specific test for closest pair"""
    test_input = """12
ADD 0 0
ADD 1 1
QUERY
ADD 3 3
ADD 2 2
QUERY
REMOVE 1 1
QUERY
ADD 0 1
ADD 1 0
QUERY
REMOVE 0 0
QUERY"""
    
    print("=== Running Closest Pair Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_closest_pair()
        print("Results:")
        for result in results:
            print(result)
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_closest_pair_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)