package problems.p2574
/*
 * @lc app=leetcode id=2574 lang=kotlin
 *
 * [2574] Left and Right Sum Differences
 */
// @lc code=start
class Solution {
    fun leftRightDifference(nums: IntArray): IntArray {
        var leftSum = 0
        var rightSum = nums.sum()
        return nums.map {
            rightSum -= it
            val diff = kotlin.math.abs(leftSum - rightSum)
            leftSum += it
            diff
        }.toIntArray()
    }
}
// @lc code=end

