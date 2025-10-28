import unittest
import sys
from io import StringIO
from solution import PartitionNumbers, solve_partition_numbers

class TestPartitionNumbers(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = PartitionNumbers(10)
        
        self.assertEqual(calculator.get_partition(0, 1000000007), 1)
        self.assertEqual(calculator.get_partition(1, 1000000007), 1)
        self.assertEqual(calculator.get_partition(2, 1000000007), 2)
        self.assertEqual(calculator.get_partition(3, 1000000007), 3)
        self.assertEqual(calculator.get_partition(4, 1000000007), 5)
        self.assertEqual(calculator.get_partition(5, 1000000007), 7)
    
    def test_known_sequence(self):
        calculator = PartitionNumbers(6)
        partitions = calculator.compute_partitions(1000000007)
        
        expected = [1, 1, 2, 3, 5, 7, 11]  # p(6) = 11
        for i, val in enumerate(expected):
            self.assertEqual(partitions[i], val)
    
    def test_different_modulus(self):
        calculator = PartitionNumbers(5)
        
        self.assertEqual(calculator.get_partition(3, 100), 3)
        self.assertEqual(calculator.get_partition(4, 10), 5)
        self.assertEqual(calculator.get_partition(5, 5), 2)  # 7 mod 5 = 2
    
    def test_full_integration(self):
        input_data = """6
0 1000000007
1 1000000007
2 1000000007
3 1000000007
4 1000000007
5 1000000007"""
        
        expected_output = ["1", "1", "2", "3", "5", "7"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_partition_numbers()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)