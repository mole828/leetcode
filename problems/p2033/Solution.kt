package problems.p2033
/*
 * @lc app=leetcode id=2033 lang=kotlin
 *
 * [2033] Minimum Operations to Make a Uni-Value Grid
 */

// @lc code=start
class Solution {
    fun minOperations(grid: Array<IntArray>, x: Int): Int {
        val nums = grid.flatMap { it.asIterable() }.sorted()
        val remainder = nums.first() % x
        if (nums.any { it % x != remainder }) {
            return -1
        }

        val target = nums[nums.size / 2]
        return nums.sumOf { kotlin.math.abs(it - target) / x }
    }
}
// @lc code=end
