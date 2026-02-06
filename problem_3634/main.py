"""3634. Minimum Removals to Balance Array

You are given an integer array nums and an integer k.

An array is considered balanced if the value of its maximum element is at most k times the minimum element.

You may remove any number of elements from nums​​​​​​​ without making it empty.

Return the minimum number of elements to remove so that the remaining array is balanced.

Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.
"""

from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        max_len = 1
        l = 0

        for r in range(n):
            while nums[r] > k * nums[l]:
                l += 1
            max_len = max(max_len, r - l + 1)

        return n - max_len


def main():
    nums = [2, 1, 5]
    k = 2
    res = Solution().minRemoval(nums, k)
    print(f"res: {res}")


if __name__ == "__main__":
    main()
