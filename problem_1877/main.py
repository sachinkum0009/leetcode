"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.
"""

from typing import List
from math import inf


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = -inf

        for i in range(n // 2):
            res = max(res, nums[i] + nums[-i-1])

        return res


def main():
    nums = [3, 5, 2, 3]
    result = Solution().minPairSum(nums)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
