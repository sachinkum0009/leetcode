"""
3713. Longest Balanced Substring I

You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s
"""

class Solution:
    def longestBalanced(self, s: str) -> int:
        max_length = 0
        n = len(s)
        
        # Try all possible starting positions
        for i in range(n):
            char_count = {}
            
            # Extend substring from position i
            for j in range(i, n):
                char = s[j]
                char_count[char] = char_count.get(char, 0) + 1
                
                # Check if all characters appear the same number of times
                counts = list(char_count.values())
                if len(set(counts)) == 1:  # All counts are equal
                    max_length = max(max_length, j - i + 1)
        
        return max_length
    

def main():
    s = "abbac"
    res = Solution().longestBalanced(s)
    print(f"res: {res}")

if __name__ == '__main__':
    main()
