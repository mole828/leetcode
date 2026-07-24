/*
 * @lc app=leetcode id=3514 lang=kotlin
 *
 * [3514] Number of Unique XOR Triplets II
 *
 * https://leetcode.com/problems/number-of-unique-xor-triplets-ii/description/
 *
 * algorithms
 * Medium (32.73%)
 * Likes:    67
 * Dislikes: 13
 * Total Accepted:    20.4K
 * Total Submissions: 54.6K
 * Testcase Example:  '[1,3]'
 *
 * You are given an integer array nums.
 * 
 * A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j]
 * XOR nums[k] where i <= j <= k.
 * 
 * Return the number of unique XOR triplet values from all possible triplets
 * (i, j, k).
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,3]
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * The possible XOR triplet values are:
 * 
 * 
 * (0, 0, 0) → 1 XOR 1 XOR 1 = 1
 * (0, 0, 1) → 1 XOR 1 XOR 3 = 3
 * (0, 1, 1) → 1 XOR 3 XOR 3 = 1
 * (1, 1, 1) → 3 XOR 3 XOR 3 = 3
 * 
 * 
 * The unique XOR values are {1, 3}. Thus, the output is 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [6,7,8,9]
 * 
 * Output: 4
 * 
 * Explanation:
 * 
 * The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 1500
 * 1 <= nums[i] <= 1500
 * 
 * 
 */
package p3514
// @lc code=start
class Solution {
    fun uniqueXorTriplets(nums: IntArray): Int {
        // nums[i] < 2048, so every possible XOR value is also in [0, 2048).
        val xorStateCount = 2048
        var reachable = BooleanArray(xorStateCount)
        reachable[0] = true

        repeat(3) {
            val next = BooleanArray(xorStateCount)
            for (xorValue in 0..<xorStateCount) {
                if (!reachable[xorValue]) continue
                for (num in nums) {
                    next[xorValue xor num] = true
                }
            }
            reachable = next
        }

        return reachable.count { it }
    }
}
// @lc code=end
