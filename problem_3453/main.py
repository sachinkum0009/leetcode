"""
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted multiple times.
"""

from typing import List
from functools import cache


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        y_bounds = [(y, y + L, L) for _, y, L in squares]

        def area_split(y_line: float) -> tuple[float, float]:
            above = 0.0
            below = 0.0
            for y_bot, y_top, L in y_bounds:
                if y_top <= y_line:
                    below += L * L
                elif y_bot >= y_line:
                    above += L * L
                else:
                    above_part = y_top - y_line
                    below_part = y_line - y_bot
                    above += L * above_part
                    below += L * below_part
            return above, below

        min_y = min(y_bot for y_bot, _, _ in y_bounds)
        max_y = max(y_top for _, y_top, _ in y_bounds)

        left, right = min_y, max_y
        for _ in range(60):
            mid = (left + right) / 2
            above, below = area_split(mid)
            if above > below:
                left = mid
            else:
                right = mid
        return (left + right) / 2


def main():
    squares = [[0, 0, 1], [2, 2, 1]]
    result = Solution().separateSquares(squares)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
