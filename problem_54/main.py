from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result: List[int] = []
        row_size = len(matrix)
        col_size = len(matrix[0])

        indexes: List[int] = [0, 0] 
        direction: bool = True
        upper: bool = True
        flag: bool = True
        i: int = 1

        for _ in range(row_size*col_size):
            result.append(matrix[indexes[0]][indexes[1]])

            if upper and (indexes[0] + indexes[1] == col_size-1):
                direction = not direction
                flag = not flag

            if not upper and (indexes[0] + indexes[1] == row_size-1):
                direction = not direction
                flag = not flag

            if indexes[0] + indexes[1] == (row_size-i) + (col_size-i):
                direction = not direction
                upper = not upper
            
            if flag and (indexes[0] - indexes[1] == 1):
                upper = True
                direction = not direction
                i += 1

            if upper:
                indexes[direction] += 1
            else:
                indexes[direction] -= 1

        return result

def main():
    # matrix: List[List[int]] = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    new_matrix = Solution().spiralOrder(matrix)
    print(new_matrix)

if __name__ == '__main__':
    main()
        