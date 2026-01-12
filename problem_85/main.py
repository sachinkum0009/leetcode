"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
"""

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols+1)

        mx = 0

        for row in matrix:
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
        
            stack = [-1]
            for i in range(cols+1):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] -1
                    mx = max(mx, h*w)
                stack.append(i)
        return mx


def main():
    matrix: List[List[str]] = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    result = Solution().maximalRectangle(matrix)
    print(f"result: {result}")

if __name__ == '__main__':
    main()
