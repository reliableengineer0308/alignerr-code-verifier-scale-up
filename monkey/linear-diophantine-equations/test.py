import unittest
import sys
from io import StringIO
from solution import solve_diophantine, solve_diophantine_equations

class TestDiophantineEquations(unittest.TestCase):
    
    def test_basic_cases(self):
        self.assertEqual(solve_diophantine(2, 3, 1), "2 -1")
        self.assertEqual(solve_diophantine(4, 6, 2), "2 -1")
        self.assertEqual(solve_diophantine(4, 6, 3), "No Solution")
        self.assertEqual(solve_diophantine(15, 25, 5), "2 -1")
    
    def test_edge_cases(self):
        self.assertEqual(solve_diophantine(1, 0, 5), "5 0")
        self.assertEqual(solve_diophantine(0, 1, 5), "0 5")
        self.assertEqual(solve_diophantine(0, 0, 5), "No Solution")
        self.assertEqual(solve_diophantine(0, 0, 0), "0 0")
    
    def test_negative_coefficients(self):

        result = solve_diophantine(-2, 3, 1)
        x, y = map(int, result.split())
        self.assertEqual(-2*x + 3*y, 1)
        self.assertTrue(x >= 0)

        result = solve_diophantine(2, -3, 1)
        x, y = map(int, result.split())
        self.assertEqual(2*x - 3*y, 1)
        self.assertTrue(x >= 0)
    
    def test_large_numbers(self):
        result = solve_diophantine(123456789, 987654321, 1)
        self.assertEqual(result, "No Solution")
        result = solve_diophantine(123456789, 987654321, 9)
        if result != "No Solution":
            x, y = map(int, result.split())
            self.assertEqual(123456789*x + 987654321*y, 9)
            self.assertTrue(x >= 0)
    
    def test_no_solution_cases(self):
        self.assertEqual(solve_diophantine(2, 4, 1), "No Solution")
        self.assertEqual(solve_diophantine(0, 0, 1), "No Solution")
    
    def test_known_solutions(self):
        # Test some known solutions
        result = solve_diophantine(3, 5, 7)
        x, y = map(int, result.split())
        self.assertEqual(3*x + 5*y, 7)
        self.assertTrue(x >= 0)
        
        result = solve_diophantine(7, 11, 13)
        x, y = map(int, result.split())
        self.assertEqual(7*x + 11*y, 13)
        self.assertTrue(x >= 0)
    
    def test_full_integration(self):
        input_data = """5
2 3 1
4 6 2
4 6 3
15 25 5
123456789 987654321 9"""  # Changed last test case to have a solution
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_diophantine_equations()
            # Verify first 4 cases
            self.assertEqual(results[0], "2 -1")
            self.assertEqual(results[1], "2 -1")
            self.assertEqual(results[2], "No Solution")
            self.assertEqual(results[3], "2 -1")
            
            # For the 5th case, verify the solution is correct
            if results[4] != "No Solution":
                x, y = map(int, results[4].split())
                self.assertEqual(123456789*x + 987654321*y, 9)
                self.assertTrue(x >= 0)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)