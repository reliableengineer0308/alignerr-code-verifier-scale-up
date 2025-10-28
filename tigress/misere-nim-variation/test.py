import unittest
import sys
from io import StringIO
from solution import solve_misere_nim, calculate_grundy

class TestMisereNim(unittest.TestCase):
    
    def test_calculate_grundy(self):
        """Test Grundy number calculation"""
        self.assertEqual(calculate_grundy("normal", 3), 3)
        self.assertEqual(calculate_grundy("normal", 1), 1)
        self.assertEqual(calculate_grundy("special", 1), 1)
        self.assertEqual(calculate_grundy("special", 2), 2)
        self.assertEqual(calculate_grundy("special", 3), 3)
        self.assertEqual(calculate_grundy("special", 4), 0)
        self.assertEqual(calculate_grundy("special", 5), 1)
    
    def test_example_1(self):
        """Test example 1 from prompt"""
        input_data = """2
2
normal 3
special 2
1
special 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_misere_nim()
            self.assertEqual(results, ["First", "Second"])
        finally:
            sys.stdin = old_stdin
    
    def test_example_2(self):
        """Test example 2 from prompt"""
        input_data = """1
3
normal 1
normal 1
special 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_misere_nim()
            self.assertEqual(results, ["First"])
        finally:
            sys.stdin = old_stdin
    
    def test_example_3(self):
        """Test example 3 from prompt"""
        input_data = """1
2
normal 2
special 4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_misere_nim()
            self.assertEqual(results, ["First"])
        finally:
            sys.stdin = old_stdin
    
    def test_all_normal_size_one_odd(self):
        """Test all normal piles of size 1, odd count"""
        input_data = """1
3
normal 1
normal 1
normal 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_misere_nim()
            self.assertEqual(results, ["Second"])  # Odd count → First loses
        finally:
            sys.stdin = old_stdin
    
    def test_all_normal_size_one_even(self):
        """Test all normal piles of size 1, even count"""
        input_data = """1
2
normal 1
normal 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_misere_nim()
            self.assertEqual(results, ["First"])  # Even count → First wins
        finally:
            sys.stdin = old_stdin
    
    def test_all_special_size_one_odd(self):
        """Test all special piles of size 1, odd count"""
        input_data = """1
3
special 1
special 1
special 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_misere_nim()
            self.assertEqual(results, ["Second"])  # Odd count → First loses
        finally:
            sys.stdin = old_stdin
    
    def test_mixed_piles_winning(self):
        """Test mixed piles where first player wins"""
        input_data = """1
2
normal 5
special 3"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_misere_nim()
            self.assertEqual(results, ["First"])  # 5 ⊕ 3 = 6 ≠ 0
        finally:
            sys.stdin = old_stdin
    
    def test_mixed_piles_losing(self):
        """Test mixed piles where first player loses"""
        input_data = """1
2
normal 2
special 2"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_misere_nim()
            self.assertEqual(results, ["Second"])  # 2 ⊕ 2 = 0
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """3
2
normal 3
special 2
1
special 1
3
normal 1
normal 1
special 1"""
    
    print("=== Running Misère Nim Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_misere_nim()
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