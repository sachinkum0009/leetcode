"""
Problem 59
Spiral Matrix II

Given a positive integer `n`, generate an `n x n` `matrix` filled with elements from 1 to n^2 in spiral order
"""

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result: List[List[int]] = [[0 for _ in range(n)] for _ in range(n)]
        val = 1
        indexes: List[int] = [0, 0]
        direction: bool = True
        upper: bool = True
        flag: bool = True
        layer: int = 1
        for i in range(n**2):
            result[indexes[0]][indexes[1]] = val

            if upper and (indexes[0] + indexes[1] == n-1):
                direction = not direction
                flag = not flag

            if not upper and (indexes[0] + indexes[1] == n-1):
                direction = not direction
                flag = not flag

            if indexes[0] + indexes[1] == (n-layer) + (n-layer):
                direction = not direction
                upper = not upper
            
            if flag and (indexes[0] - indexes[1] == 1):
                upper = True
                direction = not direction
                layer += 1

            if upper:
                indexes[direction] += 1
            else:
                indexes[direction] -= 1
            val += 1
        return result
    
def main():
    n = 3
    spiral_matrix = Solution().generateMatrix(n)
    
    print(f"spiral matrix: {spiral_matrix}")

if __name__ == '__main__':
    main()
       