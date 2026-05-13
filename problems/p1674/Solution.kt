package p1674

/*
 * @lc app=leetcode id=1674 lang=kotlin
 *
 * [1674] Minimum Moves to Make Array Complementary
 */

// @lc code=start
class Solution {
    fun minMoves(nums: IntArray, limit: Int): Int {
        val n = nums.size
        val diff = IntArray(2 * limit + 2)
        for (i in 0 until n / 2) {
            val x = nums[i]
            val y = nums[n - 1 - i]
            val l = minOf(x, y) + 1
            val r = maxOf(x, y) + limit
            diff[l]--
            diff[x + y]--
            diff[x + y + 1]++
            diff[r + 1]++
        }
        var ans = Int.MAX_VALUE
        var sum = n
        for (i in 2..2 * limit) {
            sum += diff[i]
            ans = minOf(ans, sum)
        }
        return ans
    }
}
// @lc code=end

