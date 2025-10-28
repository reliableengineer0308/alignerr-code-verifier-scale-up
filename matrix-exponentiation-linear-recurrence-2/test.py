import unittest
import sys
from io import StringIO
from solution import solve_linear_recurrence, mat_mult, mat_pow

class TestMatrixExponentiation(unittest.TestCase):
    
    def test_fibonacci(self):
        """Test Fibonacci sequence"""
        input_data = """1
2 10 1000
1 1
0 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_linear_recurrence()
            self.assertEqual(results[0], "55")
        finally:
            sys.stdin = old_stdin
    
    def test_fibonacci_small(self):
        """Test Fibonacci with small n"""
        input_data = """1
2 5 1000
1 1
0 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_linear_recurrence()
            self.assertEqual(results[0], "5")
        finally:
            sys.stdin = old_stdin
    
    def test_third_order_recurrence(self):
        """Test third order recurrence"""
        input_data = """1
3 5 100
2 1 1
1 1 2"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_linear_recurrence()
            # F(0)=1, F(1)=1, F(2)=2
            # F(3)=2*2 + 1*1 + 1*1 = 6
            # F(4)=2*6 + 1*2 + 1*1 = 15  
            # F(5)=2*15 + 1*6 + 1*2 = 38 mod 100 = 38
            self.assertEqual(results[0], "38")
        finally:
            sys.stdin = old_stdin
    
    def test_initial_value(self):
        """Test when n < k"""
        input_data = """1
3 1 100
2 1 1
1 1 2"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_linear_recurrence()
            self.assertEqual(results[0], "1")  # F(1) = 1
        finally:
            sys.stdin = old_stdin
    
    def test_zero_case(self):
        """Test n = 0"""
        input_data = """1
2 0 100
1 1
0 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_linear_recurrence()
            self.assertEqual(results[0], "0")  # F(0) = 0
        finally:
            sys.stdin = old_stdin

class TestMatrixOperations(unittest.TestCase):
    
    def test_matrix_multiplication(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = mat_mult(A, B, 1000)
        expected = [[19, 22], [43, 50]]
        self.assertEqual(result, expected)
    
    def test_matrix_exponentiation(self):
        matrix = [[1, 1], [1, 0]]
        result = mat_pow(matrix, 3, 1000)
        expected = mat_mult(mat_mult(matrix, matrix, 1000), matrix, 1000)
        self.assertEqual(result, expected)
    
    def test_identity_matrix(self):
        matrix = [[1, 0], [0, 1]]
        result = mat_pow(matrix, 5, 1000)
        self.assertEqual(result, matrix)

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """2
2 10 1000
1 1
0 1
3 5 100
2 1 1
1 1 2"""
    
    print("=== Running Matrix Exponentiation Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_linear_recurrence()
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