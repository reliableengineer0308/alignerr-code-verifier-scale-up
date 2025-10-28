import unittest
import sys
from io import StringIO
from solution import solve_dominator_tree

class TestDominatorTree(unittest.TestCase):
    
    def test_simple_dominator_chain(self):
        input_data = """1
4 3
0 1
1 2
2 3"""
        
        expected = [
            "Case #1:",
            "0", "0", "1", "2"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_dominator_tree()
            self.assertEqual(results, expected)
        finally:
            sys.stdin = old_stdin
    
    def test_complex_graph(self):
        input_data = """1
6 7
0 1
0 2
1 3
2 3
3 4
3 5
4 5"""
        
        expected = [
            "Case #1:",
            "0", "0", "0", "0", "3", "3"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_dominator_tree()
            self.assertEqual(results, expected)
        finally:
            sys.stdin = old_stdin
    
    def test_diamond_with_bypass(self):
        input_data = """1
5 5
0 1
0 2
1 3
2 3
1 4"""
        
        expected = [
            "Case #1:",
            "0", "0", "0", "0", "1"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_dominator_tree()
            self.assertEqual(results, expected)
        finally:
            sys.stdin = old_stdin
    
    def test_unreachable_nodes(self):
        input_data = """1
5 4
0 1
0 2
1 3
2 4"""
        
        expected = [
            "Case #1:",
            "0", "0", "0", "1", "2"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_dominator_tree()
            self.assertEqual(results, expected)
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    test_input = """1
6 7
0 1
0 2
1 3
2 3
3 4
3 5
4 5"""
    
    print("=== Running Dominator Tree Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_dominator_tree()
        print("Results:")
        for result in results:
            print(result)
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_specific_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)