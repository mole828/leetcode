package p3550

/*
 * @lc app=leetcode id=3550 lang=kotlin
 *
 * [3550] Smallest Index With Digit Sum Equal to Index
 */

// @lc code=start
class Solution {
    fun smallestIndex(nums: IntArray): Int {
        return nums.mapIndexed { index, num ->
            val digitSum = num.toString().sumOf { it - '0' }
            index to digitSum
        }.firstOrNull { it.first == it.second }
            ?.first ?: -1
    }
}
// @lc code=end

