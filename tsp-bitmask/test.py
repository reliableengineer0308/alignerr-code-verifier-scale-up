import unittest
import sys
from io import StringIO
from solution import solve_tsp, solve_tsp_cases

class TestTSP(unittest.TestCase):
    
    def test_tsp_4_cities(self):
        """Test TSP with 4 cities (classic example)"""
        dist = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]
        result = solve_tsp(dist)
        self.assertEqual(result, 80)
    
    def test_tsp_3_cities(self):
        """Test TSP with 3 cities"""
        dist = [
            [0, 1, 2],
            [1, 0, 3],
            [2, 3, 0]
        ]
        result = solve_tsp(dist)
        self.assertEqual(result, 6)
    
    def test_tsp_5_cities(self):
        """Test TSP with 5 cities - CORRECTED EXPECTATION"""
        dist = [
            [0, 14, 4, 10, 20],
            [14, 0, 7, 8, 7],
            [4, 7, 0, 7, 16],
            [10, 8, 7, 0, 17],
            [20, 7, 16, 17, 0]
        ]
        result = solve_tsp(dist)
        # Let's calculate the actual optimal path:
        # Path: 0→2→3→1→4→0 = 4 + 7 + 8 + 7 + 20 = 46
        # Path: 0→2→1→4→3→0 = 4 + 7 + 7 + 17 + 10 = 45
        # Path: 0→3→1→4→2→0 = 10 + 8 + 7 + 16 + 4 = 45
        # The actual minimum is 45, not 36
        self.assertEqual(result, 45)  # CORRECTED EXPECTATION
    
    def test_tsp_2_cities(self):
        """Test TSP with only 2 cities"""
        dist = [
            [0, 5],
            [5, 0]
        ]
        result = solve_tsp(dist)
        self.assertEqual(result, 10)  # 0→1→0 = 5+5=10
    
    def test_tsp_symmetric(self):
        """Test symmetric property"""
        dist = [
            [0, 3, 1],
            [3, 0, 2],
            [1, 2, 0]
        ]
        result = solve_tsp(dist)
        # Path: 0→2→1→0 = 1+2+3=6
        self.assertEqual(result, 6)
    
    def test_solve_tsp_cases_single(self):
        """Test main function with single test case"""
        input_data = """1
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_tsp_cases()
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0], "80")
        finally:
            sys.stdin = old_stdin
    
    def test_solve_tsp_cases_multiple(self):
        """Test main function with multiple test cases"""
        input_data = """2
3
0 1 2
1 0 3
2 3 0
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_tsp_cases()
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0], "6")
            self.assertEqual(results[1], "80")
        finally:
            sys.stdin = old_stdin
    
    def test_tsp_large_values(self):
        """Test TSP with larger distance values"""
        dist = [
            [0, 100, 200, 150],
            [100, 0, 120, 180],
            [200, 120, 0, 90],
            [150, 180, 90, 0]
        ]
        result = solve_tsp(dist)
        # Should find a valid path: 0→1→2→3→0 = 100+120+90+150=460
        self.assertEqual(result, 460)
    
    def test_tsp_identical_cities(self):
        """Test TSP where some paths have same cost"""
        dist = [
            [0, 5, 5, 5],
            [5, 0, 5, 5],
            [5, 5, 0, 5],
            [5, 5, 5, 0]
        ]
        result = solve_tsp(dist)
        # Any path will have same cost: 5*4 = 20
        self.assertEqual(result, 20)

def run_specific_test():
    """Run specific test cases to verify functionality"""
    print("=== Testing TSP with Bitmask DP ===")
    
    # Test 1: Classic 4-city problem
    print("\n1. Classic 4-City Problem:")
    dist1 = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    result1 = solve_tsp(dist1)
    print(f"4 cities result: {result1} (expected: 80)")
    print(f"Optimal path: 0→1→3→2→0 = 10+25+30+15=80")
    
    # Test 2: 3-city problem
    print("\n2. 3-City Problem:")
    dist2 = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]
    result2 = solve_tsp(dist2)
    print(f"3 cities result: {result2} (expected: 6)")
    print(f"Optimal path: 0→1→2→0 = 1+3+2=6")
    
    # Test 3: 2-city problem
    print("\n3. 2-City Problem:")
    dist3 = [
        [0, 5],
        [5, 0]
    ]
    result3 = solve_tsp(dist3)
    print(f"2 cities result: {result3} (expected: 10)")
    print(f"Optimal path: 0→1→0 = 5+5=10")
    
    # Test 4: 5-city problem with detailed calculation
    print("\n4. 5-City Problem:")
    dist4 = [
        [0, 14, 4, 10, 20],
        [14, 0, 7, 8, 7],
        [4, 7, 0, 7, 16],
        [10, 8, 7, 0, 17],
        [20, 7, 16, 17, 0]
    ]
    result4 = solve_tsp(dist4)
    print(f"5 cities result: {result4}")
    print("Possible paths and costs:")
    print("0→2→3→1→4→0 = 4 + 7 + 8 + 7 + 20 = 46")
    print("0→2→1→4→3→0 = 4 + 7 + 7 + 17 + 10 = 45")
    print("0→3→1→4→2→0 = 10 + 8 + 7 + 16 + 4 = 45")
    print(f"Actual minimum: {result4} (expected: 45)")
    
    # Test 5: Identical distances
    print("\n5. Identical Distances:")
    dist5 = [
        [0, 5, 5, 5],
        [5, 0, 5, 5],
        [5, 5, 0, 5],
        [5, 5, 5, 0]
    ]
    result5 = solve_tsp(dist5)
    print(f"Identical distances result: {result5} (expected: 20)")
    print(f"Any path: 5×4=20")

if __name__ == '__main__':
    # Run specific tests first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)