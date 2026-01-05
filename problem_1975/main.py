"""
Approach:
1. Calculate the sum of absolute values of all elements.
2. Count the total number of negative elements.
3. Track the minimum absolute value in grid
4. Adjust the sum if the count of negatives is odd
"""

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int | float:
        total_sum = 0
        min_abs_val = float("inf")
        negative_count = 0
        for row in matrix:
            for col in row:
                total_sum += abs(col)
                if col < 0:
                    negative_count += 1
                min_abs_val = min(min_abs_val, abs(col))

        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs_val
        return total_sum

def main():
    matrix: List[List[int]] = [[1,-1],[-1,1]]
    result = Solution().maxMatrixSum(matrix)
    print(f"result: {result}")

if __name__ == '__main__':
    main()

