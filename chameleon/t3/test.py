import unittest
import sys
from io import StringIO
from solution import main

class TestSegmentTree(unittest.TestCase):

    def test_sample_case(self):
        input_data = """5 6
1 3 2 5 4
QUERY_SUM 0 4
UPDATE 1 3 2
QUERY_MIN 1 2  
QUERY_MAX 0 4
UPDATE 2 4 -1
QUERY_SUM 0 4"""

        expected_output = """15
4
7
18"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            main()
            
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, expected_output)
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    
    def test_single_element(self):
        input_data = """1 5
5
QUERY_MIN 0 0
QUERY_MAX 0 0
QUERY_SUM 0 0
UPDATE 0 0 3
QUERY_SUM 0 0"""
        
        expected_output = """5
5
5
8"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            main()
            
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, expected_output)
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    def test_range_operations(self):
        input_data = """3 5
10 20 30
QUERY_SUM 0 2
UPDATE 0 2 5
QUERY_MIN 0 2
UPDATE 1 1 -10
QUERY_SUM 0 2"""
        
        expected_output = """60
15
65"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            main()
            
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, expected_output)
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

if __name__ == '__main__':
    unittest.main()