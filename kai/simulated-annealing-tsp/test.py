import unittest
import sys
import math
from io import StringIO
from solution import solve_tsp, euclidean_distance, total_distance, two_opt_swap

class TestSimulatedAnnealingTSP(unittest.TestCase):
    
    def test_euclidean_distance(self):
        """Test Euclidean distance calculation"""
        dist = euclidean_distance((0, 0), (3, 4))
        self.assertAlmostEqual(dist, 5.0, places=6)
    
    def test_total_distance(self):
        """Test total distance calculation"""
        cities = [(0, 0), (1, 0), (1, 1), (0, 1)]
        distances = [
            [0, 1, math.sqrt(2), 1],
            [1, 0, 1, math.sqrt(2)],
            [math.sqrt(2), 1, 0, 1],
            [1, math.sqrt(2), 1, 0]
        ]
        tour = [0, 1, 2, 3]
        dist = total_distance(tour, distances)
        expected = 1 + 1 + 1 + 1  # Square perimeter
        self.assertAlmostEqual(dist, 4.0, places=6)
    
    def test_two_opt_swap(self):
        """Test 2-opt swap operation"""
        tour = [0, 1, 2, 3, 4]
        new_tour = two_opt_swap(tour, 1, 3)
        expected = [0, 3, 2, 1, 4]
        self.assertEqual(new_tour, expected)
    
    def test_small_tsp(self):
        """Test TSP with small number of cities"""
        input_data = """4
0 0
1 0
1 1
0 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_tsp()
            self.assertEqual(len(results), 2)
            distance = float(results[0])
            tour = list(map(int, results[1].split()))
            
            # Check valid tour
            self.assertEqual(len(tour), 4)
            self.assertEqual(len(set(tour)), 4)  # All cities visited
            self.assertTrue(0 <= distance <= 10.0)  # Reasonable distance
        finally:
            sys.stdin = old_stdin
    
    def test_medium_tsp(self):
        """Test TSP with medium number of cities"""
        input_data = """5
0 0
1 3
3 1
5 2
4 4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_tsp()
            self.assertEqual(len(results), 2)
            distance = float(results[0])
            tour = list(map(int, results[1].split()))
            
            # Check valid tour
            self.assertEqual(len(tour), 5)
            self.assertEqual(len(set(tour)), 5)  # All cities visited
            self.assertTrue(0 <= distance <= 20.0)  # Reasonable distance
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """5
0 0
1 3
3 1
5 2
4 4"""
    
    print("=== Running Simulated Annealing TSP Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_tsp()
        print("Results:")
        print(f"Distance: {results[0]}")
        print(f"Tour: {results[1]}")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    # Run specific test first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)