"""
1984. Minimum Difference Between Highest and Lowest of K Scores

You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.
"""


from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k <= 1 or not nums:
            return 0
        nums.sort()
        n = len(nums)
        if k > n:
            return 0
        res = float('inf')
        for i in range(n - k + 1):
            res = min(res, nums[i + k - 1] - nums[i])
        return res
        
def main():
    nums = [9,4,1,7]
    k = 3
    result = Solution().minimumDifference(nums, k)
    print(f"result: {result}")

if __name__ == '__main__':
    main()
