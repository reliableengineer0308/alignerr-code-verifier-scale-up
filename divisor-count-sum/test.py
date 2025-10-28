import unittest
import sys
from io import StringIO
from solution import DivisorCalculator, solve_divisor_problem

class TestDivisorCalculator(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = DivisorCalculator(100)
        
        self.assertEqual(calculator.get_divisor_info(1), (1, 1))
        self.assertEqual(calculator.get_divisor_info(12), (6, 28))
        self.assertEqual(calculator.get_divisor_info(100), (9, 217))
    
    def test_prime_numbers(self):
        calculator = DivisorCalculator(1000000)
        
        self.assertEqual(calculator.get_divisor_info(999983), (2, 999984))
        self.assertEqual(calculator.get_divisor_info(17), (2, 18))
    
    def test_perfect_squares(self):
        calculator = DivisorCalculator(1000)
        
        self.assertEqual(calculator.get_divisor_info(36), (9, 91))  # 1+2+3+4+6+9+12+18+36=91
        self.assertEqual(calculator.get_divisor_info(100), (9, 217))
    
    def test_full_integration(self):
        input_data = """5
1
12
100
999983
1000000"""
        
        expected_output = [
            "1 1",
            "6 28", 
            "9 217",
            "2 999984",
            "49 2480437"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_divisor_problem()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)