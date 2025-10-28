def group_anagrams(strs):
    """
    Groups anagrams together.
    Time: O(n*k*log k), Space: O(n*k)
    where n = number of strings, k = max length of string
    """
    anagram_groups = {}
    
    for s in strs:
        # Create canonical form by sorting characters
        sorted_s = ''.join(sorted(s))
        
        # Add to corresponding group
        if sorted_s not in anagram_groups:
            anagram_groups[sorted_s] = []
        anagram_groups[sorted_s].append(s)
    
    
    # Return all groups as list of lists
    return list(anagram_groups.values())
