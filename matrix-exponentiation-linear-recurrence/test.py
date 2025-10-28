import unittest
from solution import solve_linear_recurrence

class TestMatrixExponentiation(unittest.TestCase):
    def test_fibonacci(self):
        k = 2
        coefficients = [1, 1]
        initial = [1, 1]
        n = 10
        result = solve_linear_recurrence(k, coefficients, initial, n)
        self.assertEqual(result, 55)
    
    def test_tribonacci(self):
        k = 3
        coefficients = [1, 1, 1]
        initial = [1, 1, 2]
        n = 8
        result = solve_linear_recurrence(k, coefficients, initial, n)
        self.assertEqual(result, 44)
    
    def test_custom_recurrence(self):
        k = 3
        coefficients = [2, 3, 1]
        initial = [1, 2, 3]
        n = 6
        result = solve_linear_recurrence(k, coefficients, initial, n)
        self.assertEqual(result, 116)
    
    def test_small_n(self):
        k = 2
        coefficients = [1, 1]
        initial = [1, 1]
        n = 2
        result = solve_linear_recurrence(k, coefficients, initial, n)
        self.assertEqual(result, 1)
    
    def test_large_coefficients(self):
        k = 2
        coefficients = [10**9, 10**9]
        initial = [1, 1]
        n = 3
        result = solve_linear_recurrence(k, coefficients, initial, n)
        expected = (10**9 + 10**9) % (10**9 + 7)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()