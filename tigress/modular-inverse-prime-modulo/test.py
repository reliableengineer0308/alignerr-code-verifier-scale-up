import unittest
import sys
from io import StringIO
from solution import modular_inverse, solve_modular_inverse

class TestModularInverse(unittest.TestCase):
    
    def test_basic_cases(self):
        self.assertEqual(modular_inverse(3, 11), 4)
        self.assertEqual(modular_inverse(10, 17), 12)
        self.assertEqual(modular_inverse(5, 5), -1)
    
    def test_large_prime(self):
        # Large prime: 1000000007
        # 2 * 500000004 = 1000000008 ≡ 1 mod 1000000007
        self.assertEqual(modular_inverse(2, 1000000007), 500000004)
        
        # 123456789 * 18633540 = 2300240249991060
        # Let's verify: 123456789 * 186335460 mod 1000000007
        result = (123456789 * 186335460) % 1000000007
        if result == 1:
            self.assertEqual(modular_inverse(123456789, 1000000007), 186335460)
        else:
            # Recalculate the correct inverse
            correct_inverse = pow(123456789, 1000000005, 1000000007)
            self.assertEqual(modular_inverse(123456789, 1000000007), correct_inverse)
    
    def test_edge_cases(self):
        self.assertEqual(modular_inverse(1, 2), 1)
        self.assertEqual(modular_inverse(2, 3), 2)
        
        # 1000000000 * 857142863 mod 1000000007 should be 1
        result = (1000000000 * 857142863) % 1000000007
        if result == 1:
            self.assertEqual(modular_inverse(1000000000, 1000000007), 857142863)
        else:
            # Recalculate the correct inverse
            correct_inverse = pow(1000000000, 1000000005, 1000000007)
            self.assertEqual(modular_inverse(1000000000, 1000000007), correct_inverse)
    
    def test_full_integration(self):
        input_data = """3
3 11
10 17
5 5"""
        
        expected_output = ["4", "12", "-1"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_modular_inverse()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)