"""
1200. Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
"""

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if len(arr) < 2:
            return []

        arr.sort()
        res: List[List[int]] = []
        min_diff = float("inf")

        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1]
            if d < min_diff:
                min_diff = d
                res = [[arr[i-1], arr[i]]]
            elif d == min_diff:
                res.append([arr[i-1], arr[i]])

        return res


def main():
    arr = [4, 2, 1, 3]
    res = Solution().minimumAbsDifference(arr)
    print(f"res: {res}")


if __name__ == "__main__":
    main()
