import unittest
import sys
from io import StringIO
from solution import solve_ant_colony, AntColonyOptimization
import numpy as np

class TestAntColonyOptimization(unittest.TestCase):
    
    def create_test_grid(self):
        """Create a simple test grid"""
        grid = [
            list(".........."),
            list(".#.#.#.#.."),
            list(".#.#.#.#.."),
            list(".S........"),
            list(".#.#.#.#.."),
            list(".#.#.#.#.."),
            list(".......#.."),
            list(".#.#.#.#.."),
            list(".#.#.#.E.."),
            list("..........")
        ]
        return grid
    
    def create_simple_test_grid(self):
        """Create a simpler test grid for neighbor testing"""
        grid = [
            list("....."),
            list(".#.#."),
            list(".S..."),
            list(".#.#."),
            list("...E.")
        ]
        return grid
    
    def test_grid_parsing(self):
        """Test grid parsing and start/end detection"""
        grid = self.create_test_grid()
        aco = AntColonyOptimization(grid, 10, 10, 0.3)
        
        self.assertEqual(aco.start_pos, (3, 1))
        self.assertEqual(aco.end_pos, (8, 7))
        self.assertEqual(aco.rows, 10)
        self.assertEqual(aco.cols, 10)
    
    def test_is_valid_position(self):
        """Test position validation"""
        grid = self.create_test_grid()
        aco = AntColonyOptimization(grid, 10, 10, 0.3)
        
        # Valid positions
        self.assertTrue(aco.is_valid_position((3, 1)))  # Start
        self.assertTrue(aco.is_valid_position((3, 2)))  # Empty
        self.assertTrue(aco.is_valid_position((8, 7)))  # End
        
        # Invalid positions
        self.assertFalse(aco.is_valid_position((1, 1)))  # Obstacle
        self.assertFalse(aco.is_valid_position((0, 10))) # Out of bounds
        self.assertFalse(aco.is_valid_position((-1, 0))) # Out of bounds
    
    def test_get_neighbors(self):
        """Test neighbor generation"""
        grid = self.create_simple_test_grid()
        aco = AntColonyOptimization(grid, 10, 10, 0.3)
        
        # Test neighbors for position (2, 1) - 'S' position
        neighbors = aco.get_neighbors((2, 1))
        expected_neighbors = [(2, 0), (2, 2)]
        
        self.assertEqual(set(neighbors), set(expected_neighbors))
        self.assertEqual(len(neighbors), 2)
    
    def test_manhattan_distance(self):
        """Test Manhattan distance calculation"""
        grid = self.create_test_grid()
        aco = AntColonyOptimization(grid, 10, 10, 0.3)
        
        dist1 = aco.manhattan_distance((0, 0), (3, 4))
        self.assertEqual(dist1, 7)
        
        dist2 = aco.manhattan_distance((3, 1), (8, 7))
        self.assertEqual(dist2, 11)
    
    def test_heuristic_value(self):
        """Test heuristic value calculation"""
        grid = self.create_test_grid()
        aco = AntColonyOptimization(grid, 10, 10, 0.3)
        
        heuristic = aco.heuristic_value((3, 1))
        self.assertTrue(0 < heuristic < 1)
    
    def test_small_aco(self):
        """Test ACO with small grid"""
        input_data = """5 5
.....
.#.#.
.S...
.#.#.
...E.
10 20 0.3"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_ant_colony()
            self.assertEqual(len(results), 2)
            
            path_length = int(results[0])
            path_str = results[1]
            
            # Check if path is reasonable
            self.assertTrue(path_length >= 4)  # Minimum possible path
            self.assertTrue(path_length <= 25) # Maximum possible in 5x5 grid
            
            # Check path format
            path_points = path_str.split()
            self.assertEqual(len(path_points), path_length)
            
        finally:
            sys.stdin = old_stdin
    
    def test_path_construction(self):
        """Test that ACO can find a valid path"""
        grid = self.create_simple_test_grid()
        aco = AntColonyOptimization(grid, 10, 10, 0.3)
        
        # Test BFS fallback
        path = aco.find_shortest_path_bfs()
        self.assertIsNotNone(path)
        self.assertEqual(path[0], aco.start_pos)
        self.assertEqual(path[-1], aco.end_pos)
        
        # Check path validity
        for i in range(len(path) - 1):
            current = path[i]
            next_pos = path[i + 1]
            # Adjacent positions should differ by exactly 1 in one coordinate
            diff = abs(current[0] - next_pos[0]) + abs(current[1] - next_pos[1])
            self.assertEqual(diff, 1)

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """5 5
.....
.#.#.
.S...
.#.#.
...E.
10 20 0.3"""
    
    print("=== Running Ant Colony Optimization Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_ant_colony()
        print("Results:")
        print(f"Path length: {results[0]}")
        print(f"Path: {results[1]}")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    # Run specific test first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)