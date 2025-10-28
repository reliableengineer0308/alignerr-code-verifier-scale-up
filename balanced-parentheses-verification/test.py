import unittest
from solution import is_balanced

class TestBalancedParentheses(unittest.TestCase):
    
    def test_empty_string(self):
        """Empty string is balanced."""
        self.assertTrue(is_balanced(""))
    
    def test_no_brackets(self):
        """String with no brackets is balanced."""
        self.assertTrue(is_balanced("abc123#@#"))
    
    
    def test_single_pair(self):
        """Single pair of brackets."""
        self.assertTrue(is_balanced("()"))
        self.assertTrue(is_balanced("[]"))
        self.assertTrue(is_balanced("{}"))
    
    def test_nested_brackets(self):
        """Nested brackets of same type."""
        self.assertTrue(is_balanced("((()))"))
        self.assertTrue(is_balanced("[[[]]]"))
        self.assertTrue(is_balanced("{{{}}}"))
    
    
    def test_mixed_brackets(self):
        """Mixed types with correct nesting."""
        self.assertTrue(is_balanced("([{}])"))
        self.assertTrue(is_balanced("{[()]}"))
        self.assertTrue(is_balanced("[](){}"))
    
    
    def test_unbalanced_opening(self):
        """Unmatched opening brackets."""
        self.assertFalse(is_balanced("((("))
        self.assertFalse(is_balanced("[{"))
        self.assertFalse(is_balanced("{[()]"))
    
    
    def test_unbalanced_closing(self):
        """Unmatched closing brackets."""
        self.assertFalse(is_balanced(")))"))
        self.assertFalse(is_balanced("]]]"))
        self.assertFalse(is_balanced("}]{"))
    
    
    def test_mismatched_brackets(self):
        """Mismatched bracket types."""
        self.assertFalse(is_balanced("([)]"))
        self.assertFalse(is_balanced("{[(})"))
        self.assertFalse(is_balanced("(]"))
    
    
    def test_complex_balanced(self):
        """Complex balanced string."""
        s = "a(b[c{d}e]f)g{h[i]j}k"
        self.assertTrue(is_balanced(s))
    
    def test_complex_unbalanced(self):
        """Complex unbalanced string."""
        s = "a(b[c{d]e}f)g"
        self.assertFalse(is_balanced(s))

if __name__ == '__main__':
    unittest.main()
