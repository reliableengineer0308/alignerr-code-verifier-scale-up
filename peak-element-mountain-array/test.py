import unittest
import sys
from io import StringIO
from solution import find_peak_index, solve_peak_element

class TestPeakElement(unittest.TestCase):
    
    def test_basic_case(self):
        arr = [1, 3, 5, 4, 2]
        result = find_peak_index(arr)
        self.assertEqual(result, 2)
    
    def test_symmetric_mountain(self):
        arr = [1, 2, 3, 4, 3, 2, 1]
        result = find_peak_index(arr)
        self.assertEqual(result, 3)
    
    def test_small_mountain(self):
        arr = [0, 1, 0, -1]
        result = find_peak_index(arr)
        self.assertEqual(result, 1)
    
    def test_three_element(self):
        arr = [1, 3, 1]
        result = find_peak_index(arr)
        self.assertEqual(result, 1)
    
    def test_full_integration(self):
        input_data = """3
5
1 3 5 4 2
7
1 2 3 4 3 2 1
4
0 1 0 -1"""
        
        expected_output = [
            "Case #1: 2",
            "Case #2: 3", 
            "Case #3: 1"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_peak_element()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)