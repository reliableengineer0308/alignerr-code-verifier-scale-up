import unittest
import sys
from io import StringIO
from solution import solve_euler_tour, EulerTourTree, FenwickTree

class TestEulerTourTree(unittest.TestCase):
    
    def test_simple_tree(self):
        """Test simple tree structure"""
        input_data = """5 3
1 2 3 4 5
1 2
1 3
2 4
2 5
QUERY 4 5
UPDATE 2 10
QUERY 1 5"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_euler_tour()
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0], "11")  # 4->2->5 = 4+2+5=11
            self.assertEqual(results[1], "16")  # 1->2->5 = 1+10+5=16
        finally:
            sys.stdin = old_stdin
    
    def test_linear_tree(self):
        """Test linear tree (chain)"""
        input_data = """4 3
10 20 30 40
1 2
2 3
3 4
QUERY 1 4
UPDATE 2 50
QUERY 1 4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_euler_tour()
            self.assertEqual(len(results), 2)
            # 1->2->3->4 = 10+20+30+40 = 100
            # After update: 1->50->30->40 = 10+50+30+40 = 130
            self.assertEqual(results[0], "100")
            self.assertEqual(results[1], "130")
        finally:
            sys.stdin = old_stdin
    
    def test_star_tree(self):
        """Test star-shaped tree"""
        input_data = """4 3
5 10 15 20
1 2
1 3
1 4
QUERY 2 3
UPDATE 1 30
QUERY 2 4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_euler_tour()
            self.assertEqual(len(results), 2)
            # 2->1->3 = 10+5+15 = 30
            # After update: 2->30->4 = 10+30+20 = 60
            self.assertEqual(results[0], "30")
            self.assertEqual(results[1], "60")
        finally:
            sys.stdin = old_stdin
    
    def test_single_node(self):
        """Test single node tree"""
        input_data = """1 3
100
QUERY 1 1
UPDATE 1 200
QUERY 1 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_euler_tour()
            self.assertEqual(results, ["100", "200"])
        finally:
            sys.stdin = old_stdin

class TestFenwickTree(unittest.TestCase):
    def test_fenwick_operations(self):
        fenw = FenwickTree(10)
        fenw.update(1, 5)
        fenw.update(2, 3)
        self.assertEqual(fenw.query(1), 5)
        self.assertEqual(fenw.query(2), 8)
        self.assertEqual(fenw.range_query(1, 2), 8)

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """5 3
1 2 3 4 5
1 2
1 3
2 4
2 5
QUERY 4 5
UPDATE 2 10
QUERY 1 5"""
    
    print("=== Running Euler Tour Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_euler_tour()
        print("Results:")
        for i, result in enumerate(results, 1):
            print(f"Test {i}: {result}")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    # Run specific test first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)