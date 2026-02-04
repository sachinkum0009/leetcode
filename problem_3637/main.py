"""
3637. Trionic Array I

You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n -s 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n - 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.
"""

from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False
        
        # Find p: end of first strictly increasing phase
        p = 0
        while p < n - 1 and nums[p + 1] > nums[p]:
            p += 1
        
        # Need at least one element in increasing phase (p > 0)
        # and p should not be at the end or second to last
        if p == 0 or p >= n - 2:
            return False
        
        # Find q: end of strictly decreasing phase
        q = p
        while q < n - 1 and nums[q + 1] < nums[q]:
            q += 1
        
        # Need at least one element in decreasing phase (q > p)
        # and q should not be at the end
        if q == p or q >= n - 1:
            return False
        
        # Check the rest is strictly increasing
        for i in range(q, n - 1):
            if nums[i + 1] <= nums[i]:
                return False
        
        return True


def main():
    nums = [1, 3, 5, 4, 2, 6]
    res = Solution().isTrionic(nums)
    print(f"res: {res}")


if __name__ == "__main__":
    main()
