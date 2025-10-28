import unittest
import sys
from io import StringIO
from solution import EulerianNumbers, solve_eulerian_numbers

class TestEulerianNumbers(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = EulerianNumbers(10)
        
        self.assertEqual(calculator.get_eulerian(0, 0, 1000000007), 1)
        self.assertEqual(calculator.get_eulerian(3, 1, 1000000007), 4)
        self.assertEqual(calculator.get_eulerian(4, 1, 1000000007), 11)
        self.assertEqual(calculator.get_eulerian(4, 2, 1000000007), 11)
        self.assertEqual(calculator.get_eulerian(5, 2, 1000000007), 66)
        self.assertEqual(calculator.get_eulerian(3, 3, 1000000007), 0)
    
    def test_edge_cases(self):
        calculator = EulerianNumbers(5)
        
        self.assertEqual(calculator.get_eulerian(1, 0, 1000000007), 1)
        self.assertEqual(calculator.get_eulerian(2, 0, 1000000007), 1)
        self.assertEqual(calculator.get_eulerian(2, 1, 1000000007), 1)
        self.assertEqual(calculator.get_eulerian(5, 4, 1000000007), 1)
        # A(0,k) for k > 0 should be 0
        self.assertEqual(calculator.get_eulerian(0, 1, 1000000007), 0)
    
    def test_different_modulus(self):
        calculator = EulerianNumbers(5)
        
        self.assertEqual(calculator.get_eulerian(3, 1, 100), 4)
        self.assertEqual(calculator.get_eulerian(4, 1, 10), 1)  # 11 mod 10 = 1
        self.assertEqual(calculator.get_eulerian(5, 2, 60), 6)  # 66 mod 60 = 6
    
    def test_known_values(self):
        calculator = EulerianNumbers(6)
        
        # Known Eulerian numbers from OEIS
        self.assertEqual(calculator.get_eulerian(3, 0, 1000000007), 1)
        self.assertEqual(calculator.get_eulerian(3, 1, 1000000007), 4)
        self.assertEqual(calculator.get_eulerian(3, 2, 1000000007), 1)
        
        self.assertEqual(calculator.get_eulerian(4, 0, 1000000007), 1)
        self.assertEqual(calculator.get_eulerian(4, 1, 1000000007), 11)
        self.assertEqual(calculator.get_eulerian(4, 2, 1000000007), 11)
        self.assertEqual(calculator.get_eulerian(4, 3, 1000000007), 1)
    
    def test_full_integration(self):
        input_data = """6
3 1 1000000007
4 1 1000000007
4 2 1000000007
5 2 1000000007
0 0 1000000007
3 3 1000000007"""
        
        expected_output = ["4", "11", "11", "66", "1", "0"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_eulerian_numbers()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)