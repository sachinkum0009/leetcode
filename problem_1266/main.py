"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

"""

from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_steps = 0
        current_pt = points[0]
        for point in points[1:]:
            while True:
                # move diagonally
                if current_pt[0] != point[0] and current_pt[1] != point[1]:
                    if current_pt[0] > point[0]:
                        current_pt[0] -= 1
                    else:
                        current_pt[0] += 1
                    if current_pt[1] > point[1]:
                        current_pt[1] -= 1
                    else:
                        current_pt[1] += 1
                
                    total_steps += 1
                
                # move straight
                else:
                    if current_pt[0] == point[0]:
                        if current_pt[1] > point[1]:
                            current_pt[1] -= 1
                        else:
                            current_pt[1] += 1

                    elif current_pt[1] == point[1]:
                        if current_pt[0] > point[0]:
                            current_pt[0] -= 1
                        else:
                            current_pt[0] += 1
                    total_steps += 1
                
                if current_pt[0] == point[0] and current_pt[1] == point[1]:
                    break

        return total_steps
        
def main():
    points = [[1,1],[3,4],[-1,0]]
    result = Solution().minTimeToVisitAllPoints(points)
    print(f"resut: {result}")

if __name__ == '__main__':
    main()
