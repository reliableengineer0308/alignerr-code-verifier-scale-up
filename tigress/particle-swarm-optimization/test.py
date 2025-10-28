import unittest
import sys
from io import StringIO
from solution import solve_pso, rastrigin_function, ParticleSwarmOptimization
import numpy as np

class TestParticleSwarmOptimization(unittest.TestCase):
    
    def test_rastrigin_function(self):
        """Test Rastrigin function calculation"""
        # Test at global minimum
        x_min = [0, 0]
        fitness_min = rastrigin_function(x_min)
        self.assertAlmostEqual(fitness_min, 0.0, places=6)
        
        # Test at other points
        x1 = [1, 1]
        fitness1 = rastrigin_function(x1)
        self.assertGreater(fitness1, 0)
        
        x2 = [-2, 3]
        fitness2 = rastrigin_function(x2)
        self.assertGreater(fitness2, 0)
    
    def test_pso_initialization(self):
        """Test PSO initialization"""
        pso = ParticleSwarmOptimization(2, 10, 100, 0.7, 2.0, 2.0)
        
        self.assertEqual(pso.positions.shape, (10, 2))
        self.assertEqual(pso.velocities.shape, (10, 2))
        self.assertEqual(len(pso.pbest_fitness), 10)
        
        # Check bounds
        for pos in pso.positions:
            self.assertTrue(all(-5.12 <= x <= 5.12 for x in pos))
    
    def test_velocity_update(self):
        """Test velocity update"""
        pso = ParticleSwarmOptimization(2, 10, 100, 0.7, 2.0, 2.0)
        
        velocity = np.array([0.1, 0.2])
        position = np.array([1.0, 1.0])
        pbest = np.array([0.5, 0.5])
        gbest = np.array([0.0, 0.0])
        
        new_velocity = pso.update_velocity(velocity, position, pbest, gbest)
        
        self.assertEqual(new_velocity.shape, (2,))
        # Velocity should be within reasonable bounds
        self.assertTrue(all(abs(v) <= 2.048 for v in new_velocity))  # 0.2 * (5.12 - (-5.12))
    
    def test_position_update(self):
        """Test position update"""
        pso = ParticleSwarmOptimization(2, 10, 100, 0.7, 2.0, 2.0)
        
        position = np.array([4.0, -4.0])
        velocity = np.array([2.0, -2.0])
        
        new_position = pso.update_position(position, velocity)
        
        self.assertEqual(new_position.shape, (2,))
        # Position should be within bounds
        self.assertTrue(all(-5.12 <= x <= 5.12 for x in new_position))
    
    def test_small_pso(self):
        """Test PSO with small parameters"""
        input_data = "2 20 50 0.7 2.0 2.0"
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_pso()
            self.assertEqual(len(results), 3)
            
            best_position = [float(x) for x in results[0].split(',')]
            best_fitness = float(results[1])
            convergence_data = results[2]
            
            # Check dimensions
            self.assertEqual(len(best_position), 2)
            
            # Check bounds
            self.assertTrue(all(-5.12 <= x <= 5.12 for x in best_position))
            self.assertTrue(0 <= best_fitness <= 100)  # Reasonable range for 2D Rastrigin
            
            # Check convergence data format
            self.assertTrue(len(convergence_data) > 0)
            
        finally:
            sys.stdin = old_stdin
    
    def test_medium_pso(self):
        """Test PSO with medium parameters"""
        input_data = "3 30 100 0.8 1.8 2.2"
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_pso()
            self.assertEqual(len(results), 3)
            
            best_position = [float(x) for x in results[0].split(',')]
            best_fitness = float(results[1])
            
            # Check dimensions
            self.assertEqual(len(best_position), 3)
            
            # Check bounds
            self.assertTrue(all(-5.12 <= x <= 5.12 for x in best_position))
            self.assertTrue(0 <= best_fitness <= 150)  # Reasonable range for 3D Rastrigin
            
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = "2 30 100 0.7 2.0 2.0"
    
    print("=== Running Particle Swarm Optimization Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_pso()
        print("Results:")
        print(f"Best position: {results[0]}")
        print(f"Best fitness: {results[1]}")
        print(f"Convergence data: {results[2]}")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    # Run specific test first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)