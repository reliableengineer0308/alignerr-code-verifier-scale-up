import subprocess
import sys
from solution import process_queries

def run_test_case(test_num, n, values, edges, queries, expected):
    print(f"Running Test Case {test_num}...")
    
    results = process_queries(n, values, edges, queries)
    
    if len(results) != len(expected):
        print(f"FAIL: Test Case {test_num} - Result count mismatch")
        return False
    
    all_correct = True
    for i, (res, exp) in enumerate(zip(results, expected)):
        if res != exp:
            print(f"FAIL: Test Case {test_num} - Query {i}: got {res}, expected {exp}")
            all_correct = False
    
    if all_correct:
        print(f"PASS: Test Case {test_num}")
    
    return all_correct

def main():
    # Test Case 1: Simple Tree (from prompt)
    print("=== Test Case 1: Simple Tree ===")
    n1 = 5
    values1 = [10, 20, 5, 15, 30]
    edges1 = [(0, 1), (0, 2), (1, 3), (1, 4)]
    queries1 = [
        ("QUERY", 0, 4),
        ("UPDATE", 1, 25),
        ("QUERY", 0, 4),
        ("QUERY", 2, 3),
        ("UPDATE", 3, 40),
        ("QUERY", 3, 4)
    ]
    expected1 = [30, 30, 25, 40]
    
    run_test_case(1, n1, values1, edges1, queries1, expected1)
    print()

    # Test Case 2: Chain Tree (from prompt)
    print("=== Test Case 2: Chain Tree ===")
    n2 = 4
    values2 = [5, 10, 15, 20]
    edges2 = [(0, 1), (1, 2), (2, 3)]
    queries2 = [
        ("QUERY", 0, 3),
        ("UPDATE", 2, 25),
        ("QUERY", 0, 3)
    ]
    expected2 = [20, 25]
    
    run_test_case(2, n2, values2, edges2, queries2, expected2)
    print()

    # Test Case 3: Star Tree (from prompt)
    print("=== Test Case 3: Star Tree ===")
    n3 = 5
    values3 = [100, 1, 2, 3, 4]
    edges3 = [(0, 1), (0, 2), (0, 3), (0, 4)]
    queries3 = [
        ("QUERY", 1, 2),
        ("UPDATE", 0, 50),
        ("QUERY", 1, 3),
        ("QUERY", 2, 4)
    ]
    expected3 = [100, 50, 50]
    
    run_test_case(3, n3, values3, edges3, queries3, expected3)
    print()

    # Test Case 4: Single Node
    print("=== Test Case 4: Single Node ===")
    n4 = 1
    values4 = [42]
    edges4 = []
    queries4 = [
        ("QUERY", 0, 0),
        ("UPDATE", 0, 99),
        ("QUERY", 0, 0)
    ]
    expected4 = [42, 99]
    
    run_test_case(4, n4, values4, edges4, queries4, expected4)
    print()

    # Test Case 5: Binary Tree Structure
    print("=== Test Case 5: Binary Tree ===")
    n5 = 7
    values5 = [10, 5, 15, 3, 7, 12, 18]
    edges5 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    queries5 = [
        ("QUERY", 3, 6),  # 3->1->0->2->6: max(3,5,10,15,18)=18
        ("UPDATE", 0, 25),
        ("QUERY", 4, 5),  # 4->1->0->2->5: max(7,5,25,15,12)=25
        ("QUERY", 3, 4)   # 3->1->4: max(3,5,7)=7
    ]
    expected5 = [18, 25, 7]
    
    run_test_case(5, n5, values5, edges5, queries5, expected5)
    print()

    # Test Case 6: Large Values and Negative Numbers
    print("=== Test Case 6: Large and Negative Values ===")
    n6 = 3
    values6 = [-10**9, 10**9, 0]
    edges6 = [(0, 1), (1, 2)]
    queries6 = [
        ("QUERY", 0, 2),  # -10^9, 10^9, 0 → max=10^9
        ("UPDATE", 0, 500),
        ("QUERY", 0, 2),  # 500, 10^9, 0 → max=10^9
        ("UPDATE", 1, -1000),
        ("QUERY", 0, 2)   # 500, -1000, 0 → max=500
    ]
    expected6 = [10**9, 10**9, 500]
    
    run_test_case(6, n6, values6, edges6, queries6, expected6)

if __name__ == "__main__":
    main()