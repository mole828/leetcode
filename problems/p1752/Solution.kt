/*
 * @lc app=leetcode id=1752 lang=kotlin
 *
 * [1752] Check if Array Is Sorted and Rotated
 *
 * https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
 *
 * algorithms
 * Easy (55.94%)
 * Likes:    5010
 * Dislikes: 294
 * Total Accepted:    879.8K
 * Total Submissions: 1.6M
 * Testcase Example:  '[3,4,5,1,2]'
 *
 * Given an array nums, return true if the array was originally sorted in
 * non-decreasing order, then rotated some number of positions (including
 * zero). Otherwise, return false.
 * 
 * There may be duplicates in the original array.
 * 
 * Note: An array A rotated by x positions results in an array B of the same
 * length such that B[i] == A[(i+x) % A.length] for every valid index i.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [3,4,5,1,2]
 * Output: true
 * Explanation: [1,2,3,4,5] is the original sorted array.
 * You can rotate the array by x = 2 positions to begin on the element of value
 * 3: [3,4,5,1,2].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [2,1,3,4]
 * Output: false
 * Explanation: There is no sorted array once rotated that can make nums.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,2,3]
 * Output: true
 * Explanation: [1,2,3] is the original sorted array.
 * You can rotate the array by x = 0 positions (i.e. no rotation) to make
 * nums.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 100
 * 1 <= nums[i] <= 100
 * 
 * `
 */
package p1752
// @lc code=start
class Solution {
    fun check(nums: IntArray): Boolean {
        var drops = 0
        for (i in nums.indices) {
            if (nums[i] > nums[(i + 1) % nums.size]) drops++
        }
        return drops <= 1
    }
}
// @lc code=end

