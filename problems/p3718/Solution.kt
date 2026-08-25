/*
 * @lc app=leetcode id=3718 lang=kotlin
 *
 * [3718] Smallest Missing Multiple of K
 *
 * https://leetcode.com/problems/smallest-missing-multiple-of-k/description/
 *
 * algorithms
 * Easy (63.34%)
 * Likes:    80
 * Dislikes: 4
 * Total Accepted:    57.3K
 * Total Submissions: 89.2K
 * Testcase Example:  '[8,2,3,4,6]\n2'
 *
 * Given an integer array nums and an integer k, return the smallest positive
 * multiple of k that is missing from nums.
 * 
 * A multiple of k is any positive integer divisible by k.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [8,2,3,4,6], k = 2
 * 
 * Output: 10
 * 
 * Explanation:
 * 
 * The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple
 * missing from nums is 10.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,4,7,10,15], k = 5
 * 
 * Output: 5
 * 
 * Explanation:
 * 
 * The multiples of k = 5 are 5, 10, 15, 20... and the smallest multiple
 * missing from nums is 5.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 100
 * 1 <= nums[i] <= 100
 * 1 <= k <= 100
 * 
 * 
 */
package p3718
// @lc code=start
class Solution {
    fun missingMultiple(nums: IntArray, k: Int): Int {
        var x = k
        while (x in nums) x += k
        return x
    }
}
// @lc code=end

