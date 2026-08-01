package p486
/*
 * @lc app=leetcode id=486 lang=kotlin
 *
 * [486] Predict the Winner
 */
// @lc code=start
class Solution {
    fun predictTheWinner(nums: IntArray): Boolean {
        val memo = Array(nums.size) { IntArray(nums.size) }
        fun dfs(l: Int, r: Int): Int {
            if (l == r) return nums[l]
            if (memo[l][r] != 0) return memo[l][r]
            val a = nums[l] - dfs(l + 1, r)
            val b = nums[r] - dfs(l, r - 1)
            memo[l][r] = maxOf(a, b)
            return memo[l][r]
        }
        return dfs(0, nums.size - 1) >= 0
    }
}
// @lc code=end

