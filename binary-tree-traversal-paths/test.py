import unittest
from solution import TreeNode, binary_tree_paths

class TestBinaryTreePaths(unittest.TestCase):
    
    def test_single_node(self):
        """Test tree with only root node."""
        root = TreeNode(1)
        expected = ["1"]
        self.assertEqual(binary_tree_paths(root), expected)
    
    
    def test_example_1(self):
        """Test example: 1,2,3,None,5 -> ["1->2->5", "1->3"]"""
        # Construct tree:
        #     1
        #    / \
        #   2   3
        #    \
        #     5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        
        expected = ["1->2->5", "1->3"]
        self.assertEqual(sorted(binary_tree_paths(root)), sorted(expected))
    
    
    def test_skewed_left(self):
        """Test left-skewed tree: 3->2->1"""
        # Tree: 3 <- 2 <- 1 (all left children)
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        expected = ["3->2->1"]
        self.assertEqual(binary_tree_paths(root), expected)
    
    
    def test_skewed_right(self):
        """Test right-skewed tree: 1->2->3"""
        # Tree: 1 -> 2 -> 3 (all right children)
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        expected = ["1->2->3"]
        self.assertEqual(binary_tree_paths(root), expected)
    
    
    def test_balanced_tree(self):
        """Test balanced tree with multiple paths."""
        # Tree:
        #       4
        #      / \
        #     2   6
        #    / \ / \
        #   1  3 5  7
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        
        expected = [
            "4->2->1",
            "4->2->3",
            "4->6->5",
            "4->6->7"
        ]
        self.assertEqual(sorted(binary_tree_paths(root)), sorted(expected))
    
    
    def test_tree_with_one_leaf_only(self):
        """Test tree where only one path leads to a leaf."""
        # Tree:
        #     1
        #    /
        #   2
        #  /
        # 3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        expected = ["1->2->3"]
        self.assertEqual(binary_tree_paths(root), expected)
    
    
    def test_tree_with_different_value_signs(self):
        """Test tree containing both positive and negative values."""
        # Tree:
        #     0
        #    / \
        #  -1   2
        #    \   \
        #    -3   4
        root = TreeNode(0)
        root.left = TreeNode(-1)
        root.right = TreeNode(2)
        root.left.right = TreeNode(-3)
        root.right.right = TreeNode(4)
        
        expected = [
            "0->-1->-3",
            "0->2->4"
        ]
        self.assertEqual(sorted(binary_tree_paths(root)), sorted(expected))
    
    
    def test_empty_tree(self):
        """Test empty tree (root is None)."""
        root = None
        expected = []
        self.assertEqual(binary_tree_paths(root), expected)
    
    def test_tree_with_zero_values(self):
        """Test tree containing multiple zero values."""
        # Tree:
        #     0
        #    / \
        #   0   0
        #  /     \
        # 0       0
        root = TreeNode(0)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        root.left.left = TreeNode(0)
        root.right.right = TreeNode(0)
        
        expected = [
            "0->0->0",
            "0->0->0"
        ]  # Two distinct paths, same string representation
        result = binary_tree_paths(root)
        self.assertEqual(len(result), 2)
        self.assertIn("0->0->0", result)  # Verify the pattern exists
        # Since both paths yield same string, we check count and presence
        self.assertEqual(result.count("0->0->0"), 2)


if __name__ == '__main__':
    unittest.main()
