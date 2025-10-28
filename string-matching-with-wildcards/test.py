import unittest
from solution import is_match



class TestStringMatchingWithWildCards(unittest.TestCase):

    def test_exact_match(self):
        """Test exact string match without wildcards."""
        self.assertTrue(is_match("abc", "abc"))
        self.assertFalse(is_match("abc", "abd"))


    def test_single_question_mark(self):
        """Test single '?' wildcard matching any single character."""
        self.assertTrue(is_match("a", "?"))
        self.assertTrue(is_match("x", "?"))
        self.assertTrue(is_match("cat", "c?t"))
        self.assertFalse(is_match("ct", "c?t"))  # too short
        self.assertFalse(is_match("cart", "c?t"))  # too long


    def test_asterisk_empty_match(self):
        """Test '*' matching empty sequence."""
        self.assertTrue(is_match("", "*"))
        self.assertTrue(is_match("", "*****"))
        self.assertTrue(is_match("a", "*a"))
        self.assertTrue(is_match("b", "b*"))

    def test_asterisk_full_match(self):
        """Test '*' matching entire string."""
        self.assertTrue(is_match("hello", "*"))
        self.assertTrue(is_match("world", "**"))
        self.assertTrue(is_match("test", "t*t"))
        self.assertTrue(is_match("programming", "pro*ing"))

    def test_combined_wildcards(self):
        """Test patterns with both '?' and '*'."""
        self.assertTrue(is_match("adceb", "*a*b"))
        self.assertTrue(is_match("abcd", "a*d"))
        self.assertTrue(is_match("xyz", "x?z"))
        self.assertFalse(is_match("acdcb", "a*c?b"))  # '?' needs exactly one char, but 'cb' is two
        
        # Corrected test: "c*a*b" should NOT match "aab"
        # Reason: 'c' in pattern doesn't match 'a' in string
        self.assertFalse(is_match("aab", "c*a*b"))  # Was True → now False

    def test_edge_empty_strings(self):
        """Test edge cases with empty strings."""
        self.assertTrue(is_match("", ""))  # both empty
        self.assertFalse(is_match("a", ""))  # non-empty string, empty pattern
        self.assertFalse(is_match("", "?"))  # empty string, '?' → needs one char (was True → now False)
        self.assertTrue(is_match("", "*"))  # empty string, '*' → matches empty

    def test_consecutive_asterisks(self):
        """Test multiple consecutive '*' characters."""
        self.assertTrue(is_match("abc", "a**c"))
        self.assertTrue(is_match("hello", "h**l*o"))
        self.assertTrue(is_match("test", "****"))
        self.assertTrue(is_match("", "**"))

    def test_pattern_starts_or_ends_with_asterisk(self):
        """Test patterns starting or ending with '*'."""
        self.assertTrue(is_match("start", "*art"))
        self.assertTrue(is_match("end", "en*"))
        self.assertTrue(is_match("middle", "*dd*"))
        self.assertFalse(is_match("short", "*long*"))  # no overlap

    def test_no_wildcards_mismatch(self):
        """Test non-matching strings without wildcards."""
        self.assertFalse(is_match("abc", "def"))
        self.assertFalse(is_match("hello", "world"))
        self.assertFalse(is_match("same", "sane"))  # one letter different


    def test_long_strings(self):
        """Stress test with longer strings."""
        s = "a" * 1000
        p = "a" * 1000
        self.assertTrue(is_match(s, p))  # exact match

        p = "*a*a*"
        self.assertTrue(is_match(s, p))  # '*' can match any parts
        p = "?" * 1000
        self.assertTrue(is_match(s, p))  # each '?' matches one 'a'

    def test_complex_patterns(self):
        """Test complex patterns with mixed wildcards and literals."""
        self.assertTrue(is_match("alphabet", "a*ph*et"))
        self.assertTrue(is_match("wildcard", "w*d?a*d"))
        self.assertFalse(is_match("mismatch", "m*s?p"))  # 's?' expects one char after 's', but 'si' is two
        self.assertTrue(is_match(
            "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba",
            "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"))
        self.assertFalse(is_match(
            "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
            "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))


    def test_performance_and_bounds(self):
        """Check performance and boundary conditions."""
        # Test maximum allowed size (2000 chars)
        s = "a" * 2000
        p = "?" * 2000
        self.assertTrue(is_match(s, p))
        p = "*" + "a" * 1999 + "*"
        self.assertTrue(is_match(s, p))

    def test_case_sensitivity(self):
        """Ensure case sensitivity (only lowercase expected)."""
        self.assertFalse(is_match("Hello", "hello"))  # uppercase vs lowercase
        self.assertFalse(is_match("Test", "test"))


if __name__ == '__main__':
    unittest.main()
