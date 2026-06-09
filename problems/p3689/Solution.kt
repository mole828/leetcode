package p3689

/*
 * @lc app=leetcode id=3689 lang=kotlin
 *
 * [3689] Maximum Total Subarray Value I
 */

// @lc code=start
class Solution {
    fun maxTotalValue(nums: IntArray, k: Int): Long {
        return (nums.max() - nums.min()) * k.toLong()
    }
}
// @lc code=end

