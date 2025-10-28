import unittest
import sys
from io import StringIO
from solution import main

class TestTwoSAT(unittest.TestCase):
    
    def test_sample_case(self):
        input_data = """3 4
1 2
-2 -3
-1 3
3 -2"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            result = main()
            
            output = sys.stdout.getvalue().strip()
            
            self.assertIn("SATISFIABLE", output)
            # Should have assignment for 3 variables
            lines = output.split('\n')
            self.assertEqual(len(lines), 2)
            assignment = list(map(int, lines[1].split()))
            self.assertEqual(len(assignment), 3)
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    def test_unsatisfiable(self):
        input_data = """1 2
1 1
-1 -1"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            result = main()
            
            output = sys.stdout.getvalue().strip()
            
            self.assertIn("UNSATISFIABLE", output)
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    def test_simple_satisfiable(self):
        input_data = """1 1
1 -1"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            result = main()
            
            output = sys.stdout.getvalue().strip()
            
            self.assertIn("SATISFIABLE", output)
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

if __name__ == '__main__':
    unittest.main()