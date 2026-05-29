/*
 * @lc app=leetcode id=3300 lang=kotlin
 *
 * [3300] Minimum Element After Replacement With Digit Sum
 *
 * https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/
 *
 * algorithms
 * Easy (84.58%)
 * Likes:    114
 * Dislikes: 4
 * Total Accepted:    81.4K
 * Total Submissions: 95.1K
 * Testcase Example:  '[10,12,13,14]'
 *
 * You are given an integer array nums.
 * 
 * You replace each element in nums with the sum of its digits.
 * 
 * Return the minimum element in nums after all replacements.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [10,12,13,14]
 * 
 * Output: 1
 * 
 * Explanation:
 * 
 * nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,2,3,4]
 * 
 * Output: 1
 * 
 * Explanation:
 * 
 * nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [999,19,199]
 * 
 * Output: 10
 * 
 * Explanation:
 * 
 * nums becomes [27, 10, 19] after all replacements, with minimum element
 * 10.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 100
 * 1 <= nums[i] <= 10^4
 * 
 * 
 */
package p3300
// @lc code=start
class Solution {
    fun minElement(nums: IntArray): Int {
        return nums.minOf { num ->
            num.toString().sumOf { char -> char - '0' }
        }
    }
}
// @lc code=end

