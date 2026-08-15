package p3702
/*
 * @lc app=leetcode id=3702 lang=kotlin
 *
 * [3702] Longest Subsequence With Non-Zero Bitwise XOR
 */
// @lc code=start
class Solution {
    fun longestSubsequence(nums: IntArray): Int {
        var totalXor = 0
        var hasNonZero = false

        for (num in nums) {
            totalXor = totalXor xor num
            if (num != 0) {
                hasNonZero = true
            }
        }

        return when {
            totalXor != 0 -> nums.size
            !hasNonZero -> 0
            else -> nums.size - 1
        }
    }
}
// @lc code=end
