"""
You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.

You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. Note that other bars are fixed and cannot be removed.

Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).
"""

from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_max_gap(bars):
            bars.sort()
            max_consecutive = 1
            current_consecutive = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    current_consecutive += 1
                else:
                    current_consecutive = 1
                max_consecutive = max(max_consecutive, current_consecutive)
            
            return max_consecutive + 1

        side = min(get_max_gap(hBars), get_max_gap(vBars))
        return side * side
    

def main():
    n = 2
    m = 1
    hBars = [2,3]
    vBars = [2]
    result = Solution().maximizeSquareHoleArea(n, m, hBars, vBars)
    print(f"result: {result}")

if __name__ == '__main__':
    main()
