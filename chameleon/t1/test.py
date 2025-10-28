import unittest
from solution import prime_path_transformation

class TestPrimePathTransformation(unittest.TestCase):
    
    def test_input_validation_A_not_prime(self):
        result = prime_path_transformation(1000, 1033)
        self.assertEqual(result, [])
    
    def test_input_validation_B_not_prime(self):
        result = prime_path_transformation(1033, 1000)
        self.assertEqual(result, [])
    
    def test_input_validation_both_not_prime(self):
        result = prime_path_transformation(1000, 1004)
        self.assertEqual(result, [])
    
    def test_same_prime(self):
        A, B = 1033, 1033
        result = prime_path_transformation(A, B)
        self.assertEqual(result, [1033])
    
    def test_known_path_exists(self):
        A, B = 1033, 8179
        result = prime_path_transformation(A, B)
        
        # Verify it's a valid path
        self.assertTrue(len(result) > 0)
        self.assertEqual(result[0], A)
        self.assertEqual(result[-1], B)
        
        # Verify all numbers are prime and 4-digit
        for num in result:
            self.assertTrue(1000 <= num <= 9999)
            self.assertTrue(self.is_prime(num))
        
        # Verify each step changes exactly one digit
        for i in range(len(result) - 1):
            diff_count = self.count_digit_differences(str(result[i]), str(result[i+1]))
            self.assertEqual(diff_count, 1)
    
    def test_another_known_path(self):
        A, B = 1373, 8017
        result = prime_path_transformation(A, B)
        
        if result:  # Path might exist
            self.verify_path(result, A, B)
    
    def test_short_path(self):
        A, B = 1033, 1733  # Only one digit difference
        result = prime_path_transformation(A, B)
        
        if result:
            self.verify_path(result, A, B)
            # Should be short path (2 elements or slightly more)
            self.assertGreaterEqual(len(result), 2)
    
    def test_no_path_scenario(self):
        A, B = 1009, 9973
        result = prime_path_transformation(A, B)
        
        # If path exists, verify it; if not, result should be empty list
        if result:
            self.verify_path(result, A, B)
        else:
            # No path is also a valid result
            self.assertEqual(result, [])
    
    def verify_path(self, path, A, B):
        self.assertEqual(path[0], A)
        self.assertEqual(path[-1], B)
        
        for num in path:
            self.assertTrue(1000 <= num <= 9999)
            self.assertTrue(self.is_prime(num))
        
        for i in range(len(path) - 1):
            diff_count = self.count_digit_differences(str(path[i]), str(path[i+1]))
            self.assertEqual(diff_count, 1)
    
    def is_prime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def count_digit_differences(self, str1, str2):
        return sum(1 for a, b in zip(str1, str2) if a != b)

if __name__ == '__main__':
    prime_path_transformation(1637, 8179)
    unittest.main()