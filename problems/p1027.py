from typing import List


class Solution:
    def longestArithSeqLength(self, nums:List[int]):
        """
        Returns the length of the longest arithmetic subsequence in nums
        TODO
        """
        n = len(nums)
        if n < 2:
            return n
        # Create a dictionary to store the longest arithmetic subsequence ending at each index
        dp = [{} for _ in range(n)]
        ans = 2  # Initialize the answer to 2 (minimum length of arithmetic subsequence)
        # Iterate over each pair of elements in nums and update the corresponding dp value
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[j] - nums[i]
                if diff not in dp[j]:
                    dp[j][diff] = 1  # Initialize the length to 1 (minimum length of arithmetic subsequence)
                dp[j][diff] = max(dp[j][diff], dp[i].get(diff, 1) + 1)
                ans = max(ans, dp[j][diff])
        return ans

if __name__ == '__main__':
    Solution().longestArithSeqLength(nums = [9,4,7,2,10])