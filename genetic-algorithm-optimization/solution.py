import sys
import math
import random
import numpy as np

def objective_function(x):
    """
    Multimodal function to maximize:
    f(x) = sin(x) + sin(10*x/3) + log(x) - 0.84*x + 3
    Domain: x ∈ [2.7, 7.5]
    """
    return math.sin(x) + math.sin(10 * x / 3) + math.log(x) - 0.84 * x + 3

class GeneticAlgorithm:
    def __init__(self, population_size, generations, mutation_rate, 
                 lower_bound=2.7, upper_bound=7.5, tournament_size=3, alpha=0.5):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.tournament_size = tournament_size
        self.alpha = alpha
        
        self.population = []
        self.fitness = []
        self.best_individual = None
        self.best_fitness = -float('inf')
        self.convergence_data = []
        
    def initialize_population(self):
        """Initialize population with random values within bounds"""
        self.population = np.random.uniform(
            self.lower_bound, self.upper_bound, self.population_size
        )
        self.evaluate_population()
        
    def evaluate_population(self):
        """Evaluate fitness of entire population"""
        self.fitness = [objective_function(x) for x in self.population]
        
        # Update best individual
        current_best_idx = np.argmax(self.fitness)
        current_best_fitness = self.fitness[current_best_idx]
        
        if current_best_fitness > self.best_fitness:
            self.best_fitness = current_best_fitness
            self.best_individual = self.population[current_best_idx]
            
    def tournament_selection(self):
        """Select parents using tournament selection"""
        tournament_indices = np.random.choice(
            self.population_size, self.tournament_size, replace=False
        )
        tournament_fitness = [self.fitness[i] for i in tournament_indices]
        winner_idx = tournament_indices[np.argmax(tournament_fitness)]
        return self.population[winner_idx]
    
    def blend_crossover(self, parent1, parent2):
        """Perform BLX-α crossover"""
        min_val = min(parent1, parent2)
        max_val = max(parent1, parent2)
        range_val = max_val - min_val
        
        # Expand range by alpha
        lower = min_val - self.alpha * range_val
        upper = max_val + self.alpha * range_val
        
        # Ensure within bounds
        lower = max(lower, self.lower_bound)
        upper = min(upper, self.upper_bound)
        
        # Generate offspring
        offspring1 = np.random.uniform(lower, upper)
        offspring2 = np.random.uniform(lower, upper)
        
        return offspring1, offspring2
    
    def gaussian_mutation(self, individual):
        """Apply Gaussian mutation"""
        if random.random() < self.mutation_rate:
            # Mutation with 10% of the range
            mutation_range = (self.upper_bound - self.lower_bound) * 0.1
            mutated = individual + np.random.normal(0, mutation_range)
            # Ensure within bounds
            mutated = np.clip(mutated, self.lower_bound, self.upper_bound)
            return mutated
        return individual
    
    def evolve(self):
        """Run genetic algorithm evolution"""
        self.initialize_population()
        
        for generation in range(self.generations):
            new_population = []
            
            # Elitism: keep best individual
            new_population.append(self.best_individual)
            
            # Generate new population
            while len(new_population) < self.population_size:
                # Selection
                parent1 = self.tournament_selection()
                parent2 = self.tournament_selection()
                
                # Crossover
                offspring1, offspring2 = self.blend_crossover(parent1, parent2)
                
                # Mutation
                offspring1 = self.gaussian_mutation(offspring1)
                offspring2 = self.gaussian_mutation(offspring2)
                
                new_population.extend([offspring1, offspring2])
            
            # Ensure population size is correct
            self.population = np.array(new_population[:self.population_size])
            self.evaluate_population()
            
            # Record convergence data
            self.convergence_data.append(self.best_fitness)
            
            # Early stopping if converged
            if (generation > 100 and 
                abs(self.convergence_data[-1] - self.convergence_data[-100]) < 1e-6):
                break
    
    def get_results(self):
        """Get formatted results"""
        best_x = round(self.best_individual, 6)
        best_fitness = round(self.best_fitness, 6)
        
        # Sample convergence data (first 5, last 5, and some in between)
        if len(self.convergence_data) <= 10:
            convergence_str = ",".join(f"{x:.3f}" for x in self.convergence_data)
        else:
            sampled_data = (
                self.convergence_data[:5] + 
                self.convergence_data[-5:] +
                self.convergence_data[len(self.convergence_data)//2-2:len(self.convergence_data)//2+3]
            )
            convergence_str = ",".join(f"{x:.3f}" for x in sampled_data)
        
        return best_x, best_fitness, convergence_str

def solve_genetic_algorithm():
    input = sys.stdin.read().split()
    if not input:
        return []
    
    population_size = int(input[0])
    generations = int(input[1])
    mutation_rate = float(input[2])
    
    # Set random seed for reproducibility
    random.seed(42)
    np.random.seed(42)
    
    # Run genetic algorithm
    ga = GeneticAlgorithm(population_size, generations, mutation_rate)
    ga.evolve()
    
    best_x, best_fitness, convergence_data = ga.get_results()
    
    # Format output
    results = []
    results.append(f"{best_x} {best_fitness}")
    results.append(convergence_data)
    
    return results

if __name__ == "__main__":
    results = solve_genetic_algorithm()
    for result in results:
        print(result)