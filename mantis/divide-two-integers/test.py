import unittest
from solution import divide

class TestIntegerDivision(unittest.TestCase):
    
    def test_basic_positive_division(self):
        self.assertEqual(divide(10, 3), 3)
        self.assertEqual(divide(15, 5), 3)
        self.assertEqual(divide(1, 1), 1)
        self.assertEqual(divide(100, 3), 33)
    
    def test_negative_division(self):
        self.assertEqual(divide(7, -3), -2)
        self.assertEqual(divide(-10, 3), -3)
        self.assertEqual(divide(-10, -3), 3)
        self.assertEqual(divide(-15, 4), -3)
    
    def test_overflow_cases(self):
        # Maximum and minimum 32-bit integer cases
        self.assertEqual(divide(-2147483648, -1), 2147483647)  # Overflow
        self.assertEqual(divide(-2147483648, 1), -2147483648)  # No overflow
        self.assertEqual(divide(2147483647, -1), -2147483647)  # No overflow
    
    def test_edge_cases(self):
        self.assertEqual(divide(0, 5), 0)  # Zero dividend
        self.assertEqual(divide(5, 1), 5)  # Division by 1
        self.assertEqual(divide(1, 2), 0)  # Dividend smaller than divisor
        self.assertEqual(divide(-1, 2), 0)  # Negative dividend smaller than divisor
    
    def test_large_numbers_complex(self):
        self.assertEqual(divide(1000000000, 1), 1000000000)
        self.assertEqual(divide(1000000000, 2), 500000000)
        self.assertEqual(divide(2147483647, 2), 1073741823)
        self.assertEqual(divide(-2147483648, 2), -1073741824)
    
    def test_complex_negative_division(self):
        self.assertEqual(divide(-2147483648, -3), 715827882)
        self.assertEqual(divide(1234567890, 12345), 100005)
    
    def test_powers_of_two(self):
        self.assertEqual(divide(1024, 2), 512)
        self.assertEqual(divide(1024, 4), 256)
        self.assertEqual(divide(1024, 8), 128)
        self.assertEqual(divide(1024, 16), 64)
    
    def test_negative_powers_of_two(self):
        self.assertEqual(divide(-1024, 2), -512)
        self.assertEqual(divide(1024, -4), -256)
        self.assertEqual(divide(-1024, -8), 128)
    
    def test_division_by_large_divisors(self):
        self.assertEqual(divide(100, 100), 1)
        self.assertEqual(divide(100, 101), 0)
        self.assertEqual(divide(100, 50), 2)
        self.assertEqual(divide(-100, 50), -2)
    
    def test_extreme_values(self):
        self.assertEqual(divide(2147483647, 2147483647), 1)
        self.assertEqual(divide(2147483647, -2147483647), -1)
        self.assertEqual(divide(-2147483648, -2147483648), 1)

if __name__ == '__main__':
    unittest.main()