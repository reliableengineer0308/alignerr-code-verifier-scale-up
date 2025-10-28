import unittest
import sys
from io import StringIO
from solution import solve_min_cost_max_flow

class TestMinCostMaxFlow(unittest.TestCase):
    
    def test_simple_case(self):
        input_data = """1
4 5
0 3
0 1 10 1
0 2 10 2
1 2 5 -1
1 3 10 3
2 3 10 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_min_cost_max_flow()
            self.assertEqual(results[0], "Case #1: 20 70")
            flows = list(map(int, results[1].split()))
            self.assertEqual(len(flows), 5)
        finally:
            sys.stdin = old_stdin
    
    def test_negative_cycle(self):
        input_data = """1
3 3
0 2
0 1 10 -5
1 2 10 -3
2 0 10 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_min_cost_max_flow()
            self.assertTrue(results[0].startswith("Case #1:"))
        finally:
            sys.stdin = old_stdin
    
    def test_no_negative_cycle(self):
        input_data = """1
3 2
0 2
0 1 10 2
1 2 10 3"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_min_cost_max_flow()
            self.assertEqual(results[0], "Case #1: 10 50")
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    test_input = """1
4 5
0 3
0 1 10 1
0 2 10 2
1 2 5 -1
1 3 10 3
2 3 10 1"""
    
    print("=== Running Min Cost Max Flow Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_min_cost_max_flow()
        print("Results:")
        for result in results:
            print(result)
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_specific_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)