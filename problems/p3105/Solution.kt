package p3105

/*
 * @lc app=leetcode id=3105 lang=kotlin
 *
 * [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
 *
 * https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/
 *
 * algorithms
 * Easy (64.92%)
 * Likes:    681
 * Dislikes: 35
 * Total Accepted:    228.9K
 * Total Submissions: 351.6K
 * Testcase Example:  '[1,4,3,3,2]'
 *
 * You are given an array of integers nums. Return the length of the longest
 * subarray of nums which is either strictly increasing or strictly
 * decreasing.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,4,3,3,2]
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and
 * [1,4].
 * 
 * The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4],
 * [3,2], and [4,3].
 * 
 * Hence, we return 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [3,3,3,3]
 * 
 * Output: 1
 * 
 * Explanation:
 * 
 * The strictly increasing subarrays of nums are [3], [3], [3], and [3].
 * 
 * The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
 * 
 * Hence, we return 1.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [3,2,1]
 * 
 * Output: 3
 * 
 * Explanation:
 * 
 * The strictly increasing subarrays of nums are [3], [2], and [1].
 * 
 * The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1],
 * and [3,2,1].
 * 
 * Hence, we return 3.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 50
 * 1 <= nums[i] <= 50
 * 
 * 
 */

// @lc code=start
class Solution {
    private enum class Status {
        Inc,
        Dec,
        Eq;

        companion object {
            fun from(oldNum: Int, newNum: Int): Status = when {
                oldNum == newNum -> Eq
                oldNum < newNum -> Inc
                else -> Dec
            }
        }
    }

    fun longestMonotonicSubarray(nums: IntArray): Int {
        var left = 0
        var previousStatus = Status.Eq
        var maxLength = 1

        for (right in 1 until nums.size) {
            val currentStatus = Status.from(nums[right - 1], nums[right])
            left = when {
                currentStatus == Status.Eq -> right
                currentStatus != previousStatus -> right - 1
                else -> left
            }
            previousStatus = currentStatus
            maxLength = maxOf(maxLength, right - left + 1)
        }

        return maxLength
    }
}
// @lc code=end

