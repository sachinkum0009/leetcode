"""
1653. Minimum Deletions to Make String Balanced

You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.
"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        b_count = 0
        
        for char in s:
            if char == 'b':
                # Just keep track of 'b's we might need to delete later
                b_count += 1
            else:
                # We found an 'a'. We have two choices:
                # 1. Delete this 'a' (deletions + 1)
                # 2. Keep this 'a', which means we MUST have deleted all previous 'b's
                deletions = min(deletions + 1, b_count)
                
        return deletions
    
def main():
    s = "aababbab"
    res = Solution().minimumDeletions(s)
    print(f"res: {res}")

if __name__ == "__main__":
    main()
