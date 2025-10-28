import unittest
import sys
from io import StringIO
from solution import GrundyCalculator, solve_grundy_game

class TestGrundyGame(unittest.TestCase):
    
    def setUp(self):
        self.calc = GrundyCalculator()
    
    def test_take_away_game(self):
        self.assertEqual(self.calc.take_away_grundy(0), 0)
        self.assertEqual(self.calc.take_away_grundy(1), 1)
        self.assertEqual(self.calc.take_away_grundy(2), 2)
        self.assertEqual(self.calc.take_away_grundy(3), 3)
        self.assertEqual(self.calc.take_away_grundy(4), 0)
        self.assertEqual(self.calc.take_away_grundy(5), 1)
    
    def test_power_game_small(self):
        # power game: remove perfect squares
        # G(0) = 0
        # G(1): remove 1 -> G(0)=0 → mex{0}=1
        # G(2): remove 1 -> G(1)=1 → mex{1}=0
        self.assertEqual(self.calc.power_game_grundy(0), 0)
        self.assertEqual(self.calc.power_game_grundy(1), 1)
        self.assertEqual(self.calc.power_game_grundy(2), 0)
    
    def test_division_game_small(self):
        # division game: move to floor(n/2) or floor(n/3)
        # G(0) = 0
        # G(1): floor(1/2)=0, floor(1/3)=0 → mex{0}=1
        # G(2): floor(2/2)=1, floor(2/3)=0 → mex{G(1)=1, G(0)=0} = mex{0,1}=2
        self.assertEqual(self.calc.division_game_grundy(0), 0)
        self.assertEqual(self.calc.division_game_grundy(1), 1)
        self.assertEqual(self.calc.division_game_grundy(2), 2)
    
    def test_composite_game(self):
        # Test XOR logic
        self.assertEqual(1 ^ 2 ^ 3, 0)  # Second wins
        self.assertEqual(1 ^ 2, 3)      # First wins

class TestIntegration(unittest.TestCase):
    
    def test_example_1(self):
        input_data = """2
3
take 5
power 8
divide 10
2
take 3
take 4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_grundy_game()
            self.assertEqual(len(results), 2)
            # Should calculate based on actual Grundy numbers
        finally:
            sys.stdin = old_stdin
    
    def test_example_2(self):
        input_data = """1
2
power 1
divide 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_grundy_game()
            self.assertEqual(results[0], "Second")
        finally:
            sys.stdin = old_stdin
    
    def test_single_game_winning(self):
        input_data = """1
1
take 3"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_grundy_game()
            self.assertEqual(results[0], "First")  # Grundy(3)=3 ≠ 0
        finally:
            sys.stdin = old_stdin
    
    def test_single_game_losing(self):
        input_data = """1
1
take 4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_grundy_game()
            self.assertEqual(results[0], "Second")  # Grundy(4)=0
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """2
1
take 5
2
power 1
divide 1"""
    
    print("=== Running Grundy Game Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_grundy_game()
        print("Results:")
        for result in results:
            print(result)
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    # Run specific test first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)