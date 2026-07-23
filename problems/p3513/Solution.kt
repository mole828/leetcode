/*
 * @lc app=leetcode id=3513 lang=kotlin
 *
 * [3513] Number of Unique XOR Triplets I
 *
 * https://leetcode.com/problems/number-of-unique-xor-triplets-i/description/
 *
 * algorithms
 * Medium (26.95%)
 * Likes:    66
 * Dislikes: 16
 * Total Accepted:    19.8K
 * Total Submissions: 65.8K
 * Testcase Example:  '[1,2]'
 *
 * You are given an integer array nums of length n, where nums is a permutation
 * of the numbers in the range [1, n].
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
 * Input: nums = [1,2]
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * The possible XOR triplet values are:
 * 
 * 
 * (0, 0, 0) → 1 XOR 1 XOR 1 = 1
 * (0, 0, 1) → 1 XOR 1 XOR 2 = 2
 * (0, 1, 1) → 1 XOR 2 XOR 2 = 1
 * (1, 1, 1) → 2 XOR 2 XOR 2 = 2
 * 
 * 
 * The unique XOR values are {1, 2}, so the output is 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [3,1,2]
 * 
 * Output: 4
 * 
 * Explanation:
 * 
 * The possible XOR triplet values include:
 * 
 * 
 * (0, 0, 0) → 3 XOR 3 XOR 3 = 3
 * (0, 0, 1) → 3 XOR 3 XOR 1 = 1
 * (0, 0, 2) → 3 XOR 3 XOR 2 = 2
 * (0, 1, 2) → 3 XOR 1 XOR 2 = 0
 * 
 * 
 * The unique XOR values are {0, 1, 2, 3}, so the output is 4.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n == nums.length <= 10^5
 * 1 <= nums[i] <= n
 * nums is a permutation of integers from 1 to n.
 * 
 * 
 */
package p3513

// @lc code=start
class Solution {
    fun uniqueXorTriplets0(nums: IntArray): Int {
        val resultSet = mutableSetOf<Int>()
        for (i in 0..<nums.size) {
            val a = nums[i]
            for (j in i..<nums.size) {
                val b = nums[j]
                val ab = a xor b
                for (k in j..<nums.size) {
                    val c = nums[k]
                    val abc = ab xor c
                    resultSet.add(abc)
                }
            }
        }
        return resultSet.size
    }

    fun uniqueXorTriplets(nums: IntArray): Int {
        val n = nums.size
        if (n <= 2) return n
        return n.takeHighestOneBit() shl 1
    }
}
// @lc code=end

