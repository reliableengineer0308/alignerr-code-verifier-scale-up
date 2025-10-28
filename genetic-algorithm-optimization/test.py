import unittest
import sys
from io import StringIO
from solution import solve_genetic_algorithm, objective_function, GeneticAlgorithm
import numpy as np

class TestGeneticAlgorithm(unittest.TestCase):
    
    def test_objective_function(self):
        """Test objective function calculation"""
        # Test known values
        val1 = objective_function(3.0)
        val2 = objective_function(5.0)
        val3 = objective_function(7.0)
        
        # Check if values are reasonable
        self.assertTrue(-10 < val1 < 10)
        self.assertTrue(-10 < val2 < 10)
        self.assertTrue(-10 < val3 < 10)
    
    def test_genetic_algorithm_initialization(self):
        """Test GA initialization"""
        ga = GeneticAlgorithm(50, 100, 0.05)
        ga.initialize_population()
        
        self.assertEqual(len(ga.population), 50)
        self.assertEqual(len(ga.fitness), 50)
        
        # Check bounds
        for individual in ga.population:
            self.assertTrue(2.7 <= individual <= 7.5)
    
    def test_tournament_selection(self):
        """Test tournament selection"""
        ga = GeneticAlgorithm(10, 10, 0.05)
        ga.population = np.array([3.0, 4.0, 5.0, 6.0, 2.7, 7.5, 4.5, 3.5, 5.5, 6.5])
        ga.fitness = [objective_function(x) for x in ga.population]
        
        selected = ga.tournament_selection()
        self.assertTrue(2.7 <= selected <= 7.5)
    
    def test_blend_crossover(self):
        """Test BLX-α crossover"""
        ga = GeneticAlgorithm(10, 10, 0.05)
        parent1, parent2 = 4.0, 5.0
        child1, child2 = ga.blend_crossover(parent1, parent2)
        
        # Check bounds
        self.assertTrue(2.7 <= child1 <= 7.5)
        self.assertTrue(2.7 <= child2 <= 7.5)
    
    def test_gaussian_mutation(self):
        """Test Gaussian mutation"""
        ga = GeneticAlgorithm(10, 10, 1.0)  # 100% mutation rate for testing
        individual = 5.0
        mutated = ga.gaussian_mutation(individual)
        
        self.assertTrue(2.7 <= mutated <= 7.5)
    
    def test_small_ga(self):
        """Test GA with small parameters"""
        input_data = "50 100 0.05"
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_genetic_algorithm()
            self.assertEqual(len(results), 2)
            
            # Parse results
            best_x, best_fitness = map(float, results[0].split())
            convergence_data = results[1]
            
            # Check bounds
            self.assertTrue(2.7 <= best_x <= 7.5)
            self.assertTrue(-10 <= best_fitness <= 10)
            
            # Check convergence data format
            self.assertTrue(len(convergence_data) > 0)
            convergence_values = [float(x) for x in convergence_data.split(',')]
            self.assertTrue(all(-10 <= x <= 10 for x in convergence_values))
            
        finally:
            sys.stdin = old_stdin
    
    def test_medium_ga(self):
        """Test GA with medium parameters"""
        input_data = "100 200 0.1"
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_genetic_algorithm()
            self.assertEqual(len(results), 2)
            
            best_x, best_fitness = map(float, results[0].split())
            
            # Check bounds
            self.assertTrue(2.7 <= best_x <= 7.5)
            self.assertTrue(-10 <= best_fitness <= 10)
            
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = "100 200 0.05"
    
    print("=== Running Genetic Algorithm Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_genetic_algorithm()
        print("Results:")
        print(f"Best solution: {results[0]}")
        print(f"Convergence data: {results[1]}")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    # Run specific test first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)