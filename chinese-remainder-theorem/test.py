import unittest
import sys
from io import StringIO
from solution import extended_gcd, modular_inverse_crt, chinese_remainder_theorem, solve_chinese_remainder

class TestChineseRemainderTheorem(unittest.TestCase):
    
    def test_extended_gcd(self):
        gcd, x, y = extended_gcd(35, 15)
        self.assertEqual(gcd, 5)
        self.assertEqual(35*x + 15*y, 5)
    
    def test_modular_inverse(self):
        self.assertEqual(modular_inverse_crt(3, 11), 4)
        self.assertEqual(modular_inverse_crt(10, 17), 12)
        self.assertIsNone(modular_inverse_crt(2, 4))  # No inverse
    
    def test_crt_basic(self):
        congruences = [(2, 3), (3, 5), (2, 7)]
        self.assertEqual(chinese_remainder_theorem(congruences), 23)
    
    def test_crt_no_solution(self):
        congruences = [(1, 2), (2, 4)]
        self.assertEqual(chinese_remainder_theorem(congruences), -1)
    
    def test_crt_single_congruence(self):
        congruences = [(5, 7)]
        self.assertEqual(chinese_remainder_theorem(congruences), 5)
    
    def test_full_integration(self):
        input_data = """2
3
2 3
3 5
2 7
2
1 2
2 4"""
        
        expected_output = ["23", "-1"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_chinese_remainder()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)