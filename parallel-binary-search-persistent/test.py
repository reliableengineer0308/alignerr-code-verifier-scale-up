import unittest
import sys
from io import StringIO
from solution import ParallelBinarySearch, process_parallel_binary_search

class TestParallelBinarySearch(unittest.TestCase):
    
    def test_simple_case(self):
        arr = [3, 1, 4, 2, 5]
        queries = [(1, 3, 2), (2, 5, 3), (1, 5, 1)]
        
        pbs = ParallelBinarySearch(arr, queries)
        results = pbs.solve()
        
        expected = [3, 4, 1]
        self.assertEqual(results, expected)
    
    def test_all_elements_same(self):
        arr = [5, 5, 5, 5, 5, 5]
        queries = [(1, 3, 2), (2, 4, 1), (3, 6, 3), (1, 6, 4)]
        
        pbs = ParallelBinarySearch(arr, queries)
        results = pbs.solve()
        
        expected = [5, 5, 5, 5]
        self.assertEqual(results, expected)
    
    def test_large_range_with_duplicates(self):
        arr = [10, 20, 10, 30, 20, 10, 40, 30]
        queries = [(1, 4, 2), (2, 6, 3), (3, 8, 1), (1, 8, 5), (4, 7, 2)]
        
        pbs = ParallelBinarySearch(arr, queries)
        results = pbs.solve()
        
        expected = [10, 20, 10, 20, 20]
        self.assertEqual(results, expected)
    
    def test_single_element(self):
        arr = [42]
        queries = [(1, 1, 1)]
        
        pbs = ParallelBinarySearch(arr, queries)
        results = pbs.solve()
        
        expected = [42]
        self.assertEqual(results, expected)
    
    def test_negative_numbers(self):
        arr = [-5, -2, -8, -1, -3]
        queries = [(1, 3, 2), (2, 5, 1), (1, 5, 3)]
        
        pbs = ParallelBinarySearch(arr, queries)
        results = pbs.solve()
        
        expected = [-5, -8, -3]
        self.assertEqual(results, expected)
    
    def test_process_function(self):
        input_data = """5
3 1 4 2 5
3
1 3 2
2 5 3
1 5 1"""
        
        results = process_parallel_binary_search(input_data)
        expected = [3, 4, 1]
        self.assertEqual(results, expected)
    
    def test_kth_smallest_edge_cases(self):
        # Test first element
        arr = [1, 2, 3, 4, 5]
        queries = [(1, 5, 1)]
        pbs = ParallelBinarySearch(arr, queries)
        results = pbs.solve()
        self.assertEqual(results, [1])
        
        # Test last element  
        queries = [(1, 5, 5)]
        pbs = ParallelBinarySearch(arr, queries)
        results = pbs.solve()
        self.assertEqual(results, [5])
        
        # Test middle element
        queries = [(1, 5, 3)]
        pbs = ParallelBinarySearch(arr, queries)
        results = pbs.solve()
        self.assertEqual(results, [3])
    
    def test_empty_cases(self):
        # Empty array
        pbs = ParallelBinarySearch([], [])
        results = pbs.solve()
        self.assertEqual(results, [])
        
        # Empty queries
        pbs = ParallelBinarySearch([1, 2, 3], [])
        results = pbs.solve()
        self.assertEqual(results, [])
    
    def test_single_query_large_k(self):
        arr = [1, 2, 3, 4, 5]
        queries = [(1, 5, 5)]  # k = 5, should return 5
        pbs = ParallelBinarySearch(arr, queries)
        results = pbs.solve()
        self.assertEqual(results, [5])

def run_specific_test():
    """Run specific test case from prompt example"""
    print("=== Running Example Test ===")
    
    # Example 1 from prompt
    arr = [3, 1, 4, 2, 5]
    queries = [(1, 3, 2), (2, 5, 3), (1, 5, 1)]
    
    pbs = ParallelBinarySearch(arr, queries)
    results = pbs.solve()
    
    print("Input array:", arr)
    print("Queries:", queries)
    print("Results:", results)
    print("Expected: [3, 4, 1]")
    print("Test passed:", results == [3, 4, 1])
    
    # Example 2 from prompt
    arr2 = [5, 5, 5, 5, 5, 5]
    queries2 = [(1, 3, 2), (2, 4, 1), (3, 6, 3), (1, 6, 4)]
    
    pbs2 = ParallelBinarySearch(arr2, queries2)
    results2 = pbs2.solve()
    
    print("\nInput array:", arr2)
    print("Queries:", queries2)
    print("Results:", results2)
    print("Expected: [5, 5, 5, 5]")
    print("Test passed:", results2 == [5, 5, 5, 5])
    
    # Example 3 from prompt
    arr3 = [10, 20, 10, 30, 20, 10, 40, 30]
    queries3 = [(1, 4, 2), (2, 6, 3), (3, 8, 1), (1, 8, 5), (4, 7, 2)]
    
    pbs3 = ParallelBinarySearch(arr3, queries3)
    results3 = pbs3.solve()
    
    print("\nInput array:", arr3)
    print("Queries:", queries3)
    print("Results:", results3)
    print("Expected: [10, 20, 10, 20, 20]")
    print("Test passed:", results3 == [10, 20, 10, 20, 20])

if __name__ == '__main__':
    run_specific_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)