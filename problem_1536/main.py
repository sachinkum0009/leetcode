"""
Problem 1536. Minimum Swaps to Arrange a Binary Grid
"""

from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = [0] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    count[i] += 1
                else:
                    break

        ans = 0
        for i in range(n):
            j = i
            while j < n and count[j] < n - 1 - i:
                j += 1
            if j == n:
                return -1
            ans += j - i
            while j > i:
                count[j], count[j - 1] = count[j - 1], count[j]
                j -= 1

        return ans


def main():
    grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
    print(Solution().minSwaps(grid))


if __name__ == "__main__":
    main()
