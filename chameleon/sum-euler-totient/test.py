import unittest
import sys
from io import StringIO
from solution import TotientSum, solve_totient_sum

class TestTotientSum(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = TotientSum(100)
        
        self.assertEqual(calculator.get_sum(1), 1)
        self.assertEqual(calculator.get_sum(2), 2)
        self.assertEqual(calculator.get_sum(3), 4)
        self.assertEqual(calculator.get_sum(10), 32)
        self.assertEqual(calculator.get_sum(100), 3044)
    
    def test_small_values(self):
        calculator = TotientSum(10)
        
        # φ(1)=1, φ(2)=1, φ(3)=2, φ(4)=2, φ(5)=4, φ(6)=2, φ(7)=6, φ(8)=4, φ(9)=6, φ(10)=4
        # Sum = 1+1+2+2+4+2+6+4+6+4 = 32
        self.assertEqual(calculator.get_sum(10), 32)
    
    def test_edge_cases(self):
        calculator = TotientSum(1000)
        
        self.assertEqual(calculator.get_sum(1), 1)
        self.assertEqual(calculator.get_sum(0), 0)
    
    def test_full_integration(self):
        input_data = """5
1
2
3
10
100"""
        
        expected_output = ["1", "2", "4", "32", "3044"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_totient_sum()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)