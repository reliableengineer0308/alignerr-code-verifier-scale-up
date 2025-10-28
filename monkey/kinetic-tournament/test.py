import unittest
import sys
from io import StringIO
from solution import KineticTournament, Line, solve_kinetic_tournament

class TestKineticTournament(unittest.TestCase):
    
    def test_basic_queries(self):
        lines = [
            Line(1, 0, 0),   # f(t) = t
            Line(-1, 5, 1),  # f(t) = -t + 5
            Line(0, 2, 2)    # f(t) = 2
        ]
        
        kt = KineticTournament(lines)
        
        # Test queries at different times
        self.assertAlmostEqual(kt.query_naive(0), 5.0, places=2)
        self.assertAlmostEqual(kt.query_naive(2), 3.0, places=2)
        self.assertAlmostEqual(kt.query_naive(4), 4.0, places=2)  # max(4, 1, 2) = 4
    
    def test_updates(self):
        lines = [
            Line(1, 0, 0),
            Line(-1, 5, 1),
            Line(0, 2, 2)
        ]
        
        kt = KineticTournament(lines)
        
        # Initial state
        self.assertAlmostEqual(kt.query_naive(0), 5.0, places=2)
        
        # Update second line to constant function
        kt.update(1, 0, 4)
        self.assertAlmostEqual(kt.query_naive(1), 4.0, places=2)  # max(1, 4, 2) = 4
        self.assertAlmostEqual(kt.query_naive(3), 4.0, places=2)  # max(3, 4, 2) = 4
    
    def test_single_line(self):
        lines = [Line(2, 1, 0)]  # f(t) = 2t + 1
        kt = KineticTournament(lines)
        
        self.assertAlmostEqual(kt.query_naive(0), 1.0, places=2)
        self.assertAlmostEqual(kt.query_naive(1), 3.0, places=2)
        self.assertAlmostEqual(kt.query_naive(2), 5.0, places=2)

def run_kinetic_tournament_test():
    """Run specific test for kinetic tournament"""
    test_input = """3 5
1 0
-1 5
0 2
QUERY 0
QUERY 2
UPDATE 1 0 4
QUERY 1
QUERY 3"""
    
    print("=== Running Kinetic Tournament Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_kinetic_tournament()
        print("Results:")
        for result in results:
            print(result)
        
        print("\nExpected Output:")
        print("5.00")
        print("3.00")
        print("4.00")
        print("4.00")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_kinetic_tournament_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)