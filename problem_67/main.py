"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

def main():
    # a = "11"
    # b = "1"

    a = "1010"
    b = "1011"
    
    res = Solution().addBinary(a, b)
    print(res)
if __name__ == "__main__":
    main()
