import unittest
from solution import topological_sort


class TestTopologicalSort(unittest.TestCase):


    def test_empty_graph(self):
        """Empty graph returns empty list."""
        self.assertEqual(topological_sort({}), [])


    def test_single_node(self):
        """Single node with no edges."""
        graph = {"A": []}
        self.assertEqual(topological_sort(graph), ["A"])


    def test_linear_chain(self):
        """Simple linear dependency: A → B → C."""
        graph = {
            "A": ["B"],
            "B": ["C"],
            "C": []
        }
        result = topological_sort(graph)
        self.assertEqual(result, ["A", "B", "C"])

    def test_fork_dependency(self):
        """Fork: A depends on B and C."""
        graph = {
            "A": [],
            "B": ["A"],
            "C": ["A"]
        }
        result = topological_sort(graph)
        # Valid orders: ["B", "C", "A"] or ["C", "B", "A"]
        self.assertIn(result, [["B", "C", "A"], ["C", "B", "A"]])

    def test_join_dependency(self):
        """Join: A and B both depend on C."""
        graph = {
            "A": ["C"],
            "B": ["C"],
            "C": []
        }
        result = topological_sort(graph)
        # C must be last; A and B can be in any order before C
        self.assertTrue(result.index("C") == 2)
        self.assertIn("A", result[:2])
        self.assertIn("B", result[:2])


    def test_disconnected_components(self):
        """Two independent chains: A→B and C→D."""
        graph = {
            "A": ["B"],
            "B": [],
            "C": ["D"],
            "D": []
        }
        result = topological_sort(graph)
        # A before B, C before D; relative order of chains arbitrary
        self.assertTrue(result.index("A") < result.index("B"))
        self.assertTrue(result.index("C") < result.index("D"))


    def test_cycle_detection(self):
        """Graph with a cycle: A → B → A."""
        graph = {
            "A": ["B"],
            "B": ["A"]
        }
        result = topological_sort(graph)
        self.assertEqual(result, [])  # Cycle → empty list

    def test_complex_dag(self):
        """Complex DAG with multiple dependencies."""
        graph = {
            "A": ["C"],
            "B": ["C", "D"],
            "C": ["E"],
            "D": ["F"],
            "E": ["H"],
            "F": ["G"],
            "G": ["H"],
            "H": []
        }
        result = topological_sort(graph)
        # Validate dependencies
        self.assertTrue(result.index("A") < result.index("C"))
        self.assertTrue(result.index("B") < result.index("C"))
        self.assertTrue(result.index("C") < result.index("E"))
        self.assertTrue(result.index("E") < result.index("H"))
        self.assertTrue(result.index("B") < result.index("D"))
        self.assertTrue(result.index("D") < result.index("F"))
        self.assertTrue(result.index("F") < result.index("G"))
        self.assertTrue(result.index("G") < result.index("H"))


    def test_isolated_nodes(self):
        """Graph with isolated nodes (no edges)."""
        graph = {
            "X": [],
            "Y": [],
            "Z": []
        }
        result = topological_sort(graph)
        # All nodes are independent; any order is valid
        self.assertEqual(len(result), 3)
        self.assertSetEqual(set(result), {"X", "Y", "Z"})


    def test_multiple_roots(self):
        """Multiple root nodes (indegree 0) with shared dependencies."""
        graph = {
            "P": ["R"],
            "Q": ["R"],
            "R": ["S"],
            "S": []
        }
        result = topological_sort(graph)
        # P and Q can be in any order, then R, then S
        self.assertTrue(result.index("P") < result.index("R"))
        self.assertTrue(result.index("Q") < result.index("R"))
        self.assertTrue(result.index("R") < result.index("S"))
        # Check that P and Q are at the start (order between them doesn't matter)
        first_two = set(result[:2])
        self.assertSetEqual(first_two, {"P", "Q"})


    def test_self_loop(self):
        """Node with self-loop (A → A) → cycle."""
        graph = {
            "A": ["A"]
        }
        result = topological_sort(graph)
        self.assertEqual(result, [])  # Self-loop = cycle

    def test_redundant_edges(self):
        """Graph with redundant edges (same edge listed multiple times)."""
        graph = {
            "A": ["B", "B"],  # B listed twice
            "B": []
        }
        result = topological_sort(graph)
        self.assertEqual(result, ["A", "B"])  # Duplicates shouldn't affect result


    def test_large_dag(self):
        """Larger DAG to test scalability."""
        # Linear chain of 10 nodes
        graph = {str(i): [str(i+1)] for i in range(9)}
        graph["9"] = []
        result = topological_sort(graph)
        expected = [str(i) for i in range(10)]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
