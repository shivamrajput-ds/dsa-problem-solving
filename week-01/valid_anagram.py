from collections import defaultdict


# Approach 1: Fixed Frequency Array
class SolutionArray:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        for ch in t:
            freq[ord(ch) - ord("a")] -= 1

        for count in freq:
            if count != 0:
                return False

        return True


# Approach 2: Hash Map
class SolutionHashMap:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = defaultdict(int)

        for ch in s:
            freq[ch] += 1

        for ch in t:
            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        return True


# Approach 1:
# Time Complexity: O(n + m)
# Space Complexity: O(1)

# Approach 2:
# Time Complexity: O(n + m)
# Space Complexity: O(k)
# k = number of unique characters