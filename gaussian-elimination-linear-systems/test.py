import unittest
import sys
from io import StringIO
from solution import solve_linear_system, gaussian_elimination

class TestGaussianElimination(unittest.TestCase):
    
    def test_unique_solution_3x3(self):
        """Test 3x3 system with unique solution"""
        input_data = """3
2 1 -1 8
-3 -1 2 -11
-2 1 2 -3"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_linear_system()
            self.assertEqual(results[0], "Solution")
            self.assertAlmostEqual(float(results[1]), 2.0, places=5)
            self.assertAlmostEqual(float(results[2]), 3.0, places=5)
            self.assertAlmostEqual(float(results[3]), -1.0, places=5)
        finally:
            sys.stdin = old_stdin
    
    def test_no_solution(self):
        """Test inconsistent system"""
        input_data = """2
1 1 1
1 1 2"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_linear_system()
            self.assertEqual(results, ["No solution"])
        finally:
            sys.stdin = old_stdin
    
    def test_infinite_solutions(self):
        """Test system with infinite solutions"""
        input_data = """2
1 1 1
2 2 2"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_linear_system()
            self.assertEqual(results, ["Infinite solutions"])
        finally:
            sys.stdin = old_stdin
    
    def test_single_equation(self):
        """Test 1x1 system"""
        input_data = """1
2 4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_linear_system()
            self.assertEqual(results[0], "Solution")
            self.assertAlmostEqual(float(results[1]), 2.0, places=5)
        finally:
            sys.stdin = old_stdin
    
    def test_zero_determinant_but_consistent(self):
        """Test system with zero determinant but consistent"""
        input_data = """2
1 2 3
2 4 6"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_linear_system()
            self.assertEqual(results, ["Infinite solutions"])
        finally:
            sys.stdin = old_stdin

class TestGaussianFunction(unittest.TestCase):
    
    def test_gaussian_unique(self):
        """Test Gaussian elimination function with unique solution"""
        matrix = [
            [2, 1, -1, 8],
            [-3, -1, 2, -11],
            [-2, 1, 2, -3]
        ]
        status, solution = gaussian_elimination(matrix, 3)
        self.assertEqual(status, 'unique')
        self.assertAlmostEqual(solution[0], 2.0, places=5)
        self.assertAlmostEqual(solution[1], 3.0, places=5)
        self.assertAlmostEqual(solution[2], -1.0, places=5)
    
    def test_gaussian_no_solution(self):
        """Test Gaussian elimination with no solution"""
        matrix = [
            [1, 1, 1],
            [1, 1, 2]
        ]
        status, solution = gaussian_elimination(matrix, 2)
        self.assertEqual(status, 'no_solution')
    
    def test_gaussian_infinite(self):
        """Test Gaussian elimination with infinite solutions"""
        matrix = [
            [1, 1, 1],
            [2, 2, 2]
        ]
        status, solution = gaussian_elimination(matrix, 2)
        self.assertEqual(status, 'infinite')

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """3
2 1 -1 8
-3 -1 2 -11
-2 1 2 -3"""
    
    print("=== Running Gaussian Elimination Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_linear_system()
        print("Results:")
        for result in results:
            print(result)
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    # Run specific test first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)