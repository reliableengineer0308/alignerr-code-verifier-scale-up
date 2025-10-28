import unittest
import sys
from io import StringIO
from solution import solve_max_xor_subarray

class TestMaxXorSubarray(unittest.TestCase):
    
    def test_basic_operations(self):
        input_data = """1
5 4
1 2 3 4 5
QUERY 0 4
UPDATE 2 10
QUERY 0 4
QUERY 1 3"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_max_xor_subarray()
            self.assertEqual(results[0], "Case #1:")
            # The actual values might vary based on implementation
            self.assertEqual(results[1], "7")
            self.assertEqual(results[2], "14")
            self.assertEqual(results[3], "14")
        finally:
            sys.stdin = old_stdin
    
    def test_all_same_elements(self):
        input_data = """1
4 4
5 5 5 5
QUERY 0 3
UPDATE 1 0
QUERY 0 3
QUERY 1 2"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_max_xor_subarray()
            self.assertEqual(results[0], "Case #1:")
            self.assertEqual(results[1], "5")
            self.assertEqual(results[2], "5")
            self.assertEqual(results[3], "5")
        finally:
            sys.stdin = old_stdin
    def large_example(self):
        input_data = """1
3 4
1000000000 0 1000000000
QUERY 0 2
UPDATE 1 1000000000
QUERY 0 2
QUERY 1 1"""
        
        expected_output = [
            "Case #1:",
            "1000000000",  # First query: max is 10^9
            "0",           # After update: all elements are 10^9, XORs are 0
            "0"            # Single element XOR is 0
        ]
        
        self._run_test(input_data, expected_output)
    
    def test_edge_case_large_numbers(self):
        input_data = """1
6 8
12345 98765 55555 11111 99999 88888
QUERY 0 5
UPDATE 2 12345
QUERY 0 5
UPDATE 4 0
QUERY 0 5
QUERY 1 4
UPDATE 3 77777
QUERY 2 5"""
        
        expected_output = [
            "Case #1:",
            "111092",
            "111092",
            "111092", 
            "111092",
            "128292"
        ]
        
        self._run_test(input_data, expected_output)
    
    def test_single_element_arrays(self):
        input_data = """2

1 3
42
QUERY 0 0
UPDATE 0 100
QUERY 0 0

2 5
5 10
QUERY 0 1
UPDATE 0 10
QUERY 0 1
UPDATE 1 5
QUERY 0 1"""
        
        expected_output = [
            "Case #1:",
            "42",   # Single element
            "100",  # After update
            
            "Case #2:",
            "15",   # 5⊕10=15
            "10",    #Single element
            "15"    # After update [10,5]: 10⊕5=15
        ]
        
        self._run_test(input_data, expected_output)
    
    def _run_test(self, input_data, expected_output):
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_max_xor_subarray()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)