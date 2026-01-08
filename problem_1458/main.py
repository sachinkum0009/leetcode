from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int | float:
        m = len(nums1)
        n = len(nums2)

        dp = [[-float('inf')] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                current_prod = nums1[i-1] * nums2[j-1]

                dp[i][j] = max(
                    current_prod,
                    current_prod + dp[i-1][j-1],
                    dp[i-1][j],
                    dp[i][j-1]
                )
        return dp[m][n]


        # subseq_size = len(nums1) - 1 if len(nums1) < len(nums2) else len(nums2) - 1
        # max_product = [0]*subseq_size
        # for 
        # return 10


def main():
    nums1 = [3, -2]
    nums2 = [2, -6, 7]

    result = Solution().maxDotProduct(nums1, nums2)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
