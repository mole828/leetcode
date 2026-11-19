package p2567

import kotlin.math.abs

/*
 * @lc app=leetcode id=2567 lang=kotlin
 *
 * [2567] Minimum Score by Changing Two Elements
 *
 * https://leetcode.com/problems/minimum-score-by-changing-two-elements/description/
 *
 * algorithms
 * Medium (50.15%)
 * Likes:    338
 * Dislikes: 326
 * Total Accepted:    40.8K
 * Total Submissions: 70.2K
 * Testcase Example:  '[1,4,7,8,5]'
 *
 * You are given an integer array nums.
 * 
 * 
 * The low score of nums is the minimum absolute difference between any two
 * integers.
 * The high score of nums is the maximum absolute difference between any two
 * integers.
 * The score of nums is the sum of the high and low scores.
 * 
 * 
 * Return the minimum score after changing two elements of nums.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,4,7,8,5]
 * 
 * Output: 3
 * 
 * Explanation:
 * 
 * 
 * Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].
 * The low score is the minimum absolute difference: |6 - 6| = 0.
 * The high score is the maximum absolute difference: |8 - 5| = 3.
 * The sum of high and low score is 3.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,4,3]
 * 
 * Output: 0
 * 
 * Explanation:
 * 
 * 
 * Change nums[1] and nums[2] to 1 so that nums becomes [1,1,1].
 * The sum of maximum absolute difference and minimum absolute difference is
 * 0.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 3 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 * 
 * 
 */

// @lc code=start
class Solution {
    fun minimizeSum(nums: IntArray): Int {
        if (nums.size <= 3) return 0
        val nums = nums.toMutableList()
        nums.sort()
        val leftPick = mutableListOf<Int>()
        val rightPick = mutableListOf<Int>()
        rightPick.add(nums.removeLast())
        rightPick.add(nums.removeLast())
        var ans = abs(nums.first() - nums.last())
        while (rightPick.isNotEmpty()) {
            nums.addLast(rightPick.removeLast())
            leftPick.add(nums.removeFirst())
            ans = minOf(ans, abs(nums.first() - nums.last()))
        }
        return ans
    }
}
// @lc code=end

