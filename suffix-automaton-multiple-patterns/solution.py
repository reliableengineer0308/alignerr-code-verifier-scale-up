import sys
sys.setrecursionlimit(300000)

class SuffixAutomaton:
    class State:
        __slots__ = ['length', 'link', 'next', 'first_pos', 'count', 'is_clone', 'end_positions']
        def __init__(self, length):
            self.length = length
            self.link = -1
            self.next = {}
            self.first_pos = -1
            self.count = 0
            self.is_clone = False
            self.end_positions = set()
    
    def __init__(self, text):
        self.states = []
        self.last = 0
        self.text = text
        
        # Initialize with root state
        root = self.State(0)
        root.first_pos = 0
        self.states.append(root)
        
        # Build automaton character by character
        for i, ch in enumerate(text):
            self.extend(ch, i + 1)
        
        # Precompute counts and end positions
        self._precompute_counts()
        self._precompute_end_positions()
    
    def extend(self, ch, pos):
        curr = len(self.states)
        new_state = self.State(self.states[self.last].length + 1)
        new_state.first_pos = pos - 1
        new_state.count = 1
        new_state.end_positions.add(pos - 1)  # End position
        self.states.append(new_state)
        
        p = self.last
        while p != -1 and ch not in self.states[p].next:
            self.states[p].next[ch] = curr
            p = self.states[p].link
        
        if p == -1:
            self.states[curr].link = 0
        else:
            q = self.states[p].next[ch]
            if self.states[p].length + 1 == self.states[q].length:
                self.states[curr].link = q
            else:
                clone = len(self.states)
                clone_state = self.State(self.states[p].length + 1)
                clone_state.next = self.states[q].next.copy()
                clone_state.link = self.states[q].link
                clone_state.first_pos = self.states[q].first_pos
                clone_state.is_clone = True
                self.states.append(clone_state)
                
                while p != -1 and self.states[p].next.get(ch) == q:
                    self.states[p].next[ch] = clone
                    p = self.states[p].link
                
                self.states[q].link = clone
                self.states[curr].link = clone
        
        self.last = curr
    
    def _precompute_counts(self):
        # Create states sorted by length descending
        states_by_len = sorted(range(len(self.states)), 
                             key=lambda i: self.states[i].length, reverse=True)
        
        for state_idx in states_by_len:
            if self.states[state_idx].link != -1:
                link_state = self.states[state_idx].link
                if not self.states[state_idx].is_clone:
                    self.states[link_state].count += self.states[state_idx].count
    
    def _precompute_end_positions(self):
        # Propagate end positions through suffix links
        states_by_len = sorted(range(len(self.states)), 
                             key=lambda i: self.states[i].length, reverse=True)
        
        for state_idx in states_by_len:
            link_state = self.states[state_idx].link
            if link_state != -1:
                # Propagate end positions to suffix link state
                self.states[link_state].end_positions |= self.states[state_idx].end_positions
    
    def find_pattern(self, pattern):
        """Find if pattern exists and return first state that matches"""
        current = 0
        for ch in pattern:
            if ch not in self.states[current].next:
                return -1
            current = self.states[current].next[ch]
        return current
    
    def count_occurrences(self, pattern):
        state = self.find_pattern(pattern)
        if state == -1:
            return 0
        return self.states[state].count
    
    def find_first_occurrence(self, pattern):
        state = self.find_pattern(pattern)
        if state == -1:
            return -1
        # First position is the end position of the pattern
        return self.states[state].first_pos - len(pattern) + 1
    
    def find_all_occurrences(self, pattern):
        state = self.find_pattern(pattern)
        if state == -1:
            return []
        
        # Convert end positions to start positions
        occurrences = set()
        for end_pos in self.states[state].end_positions:
            start_pos = end_pos - len(pattern) + 1
            if start_pos >= 0:
                occurrences.add(start_pos)
        
        return sorted(occurrences)

def solve_suffix_automaton():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return []
    
    idx = 0
    t = int(input_data[idx]); idx += 1
    results = []
    
    for case_num in range(1, t + 1):
        text = input_data[idx].strip(); idx += 1
        P = int(input_data[idx]); idx += 1
        
        patterns = []
        for _ in range(P):
            patterns.append(input_data[idx].strip()); idx += 1
        
        Q = int(input_data[idx]); idx += 1
        
        queries = []
        for _ in range(Q):
            parts = input_data[idx].split()
            idx += 1
            query_type = parts[0]
            pattern = ' '.join(parts[1:])
            queries.append((query_type, pattern))
        
        # Build suffix automaton for the text
        automaton = SuffixAutomaton(text)
        
        case_results = [f"Case #{case_num}:"]
        
        for query_type, pattern in queries:
            if query_type == "COUNT":
                count = automaton.count_occurrences(pattern)
                case_results.append(str(count))
            elif query_type == "FIRST":
                pos = automaton.find_first_occurrence(pattern)
                case_results.append(str(pos))
            elif query_type == "ALL":
                positions = automaton.find_all_occurrences(pattern)
                if positions:
                    case_results.append(" ".join(map(str, positions)))
                else:
                    case_results.append("")
        
        results.extend(case_results)
    
    return results