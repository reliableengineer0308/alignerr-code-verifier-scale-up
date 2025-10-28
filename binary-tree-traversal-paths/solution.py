# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root):
    """
    Returns all root-to-leaf paths in a binary tree.
    
    Args:
        root: TreeNode - root of the binary tree (or None)
    
    Returns:
        List[str] - all root-to-leaf paths as "val1->val2->...->valN"
    """
    if not root:
        return []
    
    result = []
    path = []  # To store current path values
    
    def dfs(node):
        # Add current node to path
        path.append(str(node.val))
        
        # Check if it's a leaf node
        if not node.left and not node.right:
            # Leaf: add path to result
            result.append("->".join(path))
        else:
            # Continue DFS on children
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        # Backtrack: remove current node from path
        path.pop()
    
    
    dfs(root)
    return result
