import unittest
import sys
from io import StringIO
from solution import solve_suffix_automaton

class TestSuffixAutomaton(unittest.TestCase):
    
    def test_basic_search(self):
        input_data = """1
abracadabra
3
ab
cad
xyz
5
COUNT ab
FIRST cad
ALL ab
COUNT xyz
FIRST xyz"""
        
        expected = [
            "Case #1:",
            "2", "4", "0 7", "0", "-1"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_suffix_automaton()
            self.assertEqual(results, expected)
        finally:
            sys.stdin = old_stdin
    
    def test_overlapping_patterns(self):
        input_data = """1
aaaaa
2
aa
aaa
6
COUNT aa
COUNT aaa
ALL aa
ALL aaa
FIRST aa
FIRST aaa"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_suffix_automaton()
            self.assertEqual(results[0], "Case #1:")
            self.assertEqual(results[1], "4")  # COUNT aa
            self.assertEqual(results[2], "3")  # COUNT aaa
            # ALL aa should have 4 positions: 0,1,2,3
            self.assertEqual(len(results[3].split()), 4)
            # ALL aaa should have 3 positions: 0,1,2  
            self.assertEqual(len(results[4].split()), 3)
            self.assertEqual(results[5], "0")  # FIRST aa
            self.assertEqual(results[6], "0")  # FIRST aaa
        finally:
            sys.stdin = old_stdin
    
    def test_multiple_patterns_special_chars(self):
        input_data = """1
hello@world@hello
3
hello
@
@world
5
COUNT hello
FIRST @
ALL @
COUNT @world
ALL @world"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_suffix_automaton()
            self.assertEqual(results[0], "Case #1:")
            self.assertEqual(results[1], "2")  # COUNT hello
            self.assertEqual(results[2], "5")  # FIRST @
            self.assertEqual(results[3], "5 11")  # ALL @
            self.assertEqual(results[4], "1")  # COUNT @world
            self.assertEqual(results[5], "5")  # ALL @world
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    test_input = """1
abracadabra
3
ab
cad
xyz
5
COUNT ab
FIRST cad
ALL ab
COUNT xyz
FIRST xyz"""
    
    print("=== Running Suffix Automaton Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_suffix_automaton()
        print("Results:")
        for result in results:
            print(result)
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_specific_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)