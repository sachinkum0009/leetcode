"""
You are given an array nums consisting of n prime integers.

You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].

Additionally, you must minimize each value of ans[i] in the resulting array.

If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.
"""

from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue
            temp = n
            bit = 0
            while (temp >> bit) & 1:
                bit += 1
            ans.append(n ^ (1 << (bit - 1)))
            
        return ans
        
def main():
    nums = [2,3,5,7]
    result = Solution().minBitwiseArray(nums)
    print(f"result: {result}")

if __name__ == '__main__':
    main()
