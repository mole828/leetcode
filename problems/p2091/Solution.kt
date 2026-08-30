package p2091
/*
 * @lc app=leetcode id=2091 lang=kotlin
 *
 * [2091] Removing Minimum and Maximum From Array
 */
// @lc code=start
class Solution {
    fun minimumDeletions(nums: IntArray): Int {
        var maxIndex = 0
        var minIndex = 0
        for (i in nums.indices) {
            if (nums[i] > nums[maxIndex]) maxIndex = i
            if (nums[i] < nums[minIndex]) minIndex = i
        }
        val left = minOf(maxIndex, minIndex) 
        val right = nums.size - maxOf(maxIndex, minIndex) - 1
        val middle = nums.size - left - right - 2
        return minOf(
            left + right,
            left + middle,
            right + middle,
        ) + 2 
    }
}
// @lc code=end

