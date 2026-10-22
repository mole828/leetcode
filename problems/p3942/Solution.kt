package p3942

import sun.jvm.hotspot.oops.java_lang_Class

/*
 * @lc app=leetcode id=3942 lang=kotlin
 *
 * [3942] Minimum Operations to Sort a Permutation
 *
 * https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/description/
 *
 * algorithms
 * Medium (27.64%)
 * Likes:    104
 * Dislikes: 11
 * Total Accepted:    18.5K
 * Total Submissions: 60.7K
 * Testcase Example:  '[0,2,1]'
 *
 * You are given an integer array nums of length n, where nums is a permutation
 * of the integers from 0 to n - 1.
 * 
 * You may perform only the following operations:
 * 
 * 
 * Reverse the entire array.
 * Rotate Left by One: Move the first element to the end of the array, and rest
 * elements to left by one position.
 * 
 * 
 * Return an integer denoting the minimum number of operations required to sort
 * the array in increasing order. If it is not possible to sort the array using
 * only the given operations, return -1.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [0,2,1]
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * 
 * Rotate Left by one: [2, 1, 0]
 * Reverse the array: [0, 1, 2]
 * 
 * 
 * The array becomes sorted in 2 operations, which is minimal
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,0,2]
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * 
 * Reverse the array: [2, 0, 1]
 * Rotate Left by one: [0, 1, 2]
 * 
 * 
 * The array becomes sorted in 2 operations, which is minimal.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [2,0,1,3]
 * 
 * Output: -1
 * 
 * Explanation:
 * 
 * It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n == nums.length <= 10^5
 * 0 <= nums[i] <= n - 1
 * nums is a permutation of integers from 0 to n - 1.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun minOperations(nums: IntArray): Int {
        val nums = nums.toList()
        val sorted = nums.sorted()
        val reserved = sorted.reversed()
        val double = nums + nums
        fun List<Int>.indexOf(target: List<Int>): Int {
            var left = 0
            while (left + target.size <= this.size) {
                var d = 0
                while (this[left + d] == target[d]) {
                    d += 1
                    if (d == target.size) return left
                }
                left += 1
            }
            return -1
        }
        // println("${mapOf(
        //     "re" to reserved,
        //     "sorted" to sorted,
        //     "double" to double,
        // )}")
        val n = nums.size
        val index = double.indexOf(sorted)
        if (index != -1) return minOf(index, n - index + 2)
        val reservedIndex = double.indexOf(reserved)
        if (reservedIndex != -1) return minOf(reservedIndex + 1, n - reservedIndex + 1)
        return -1
    }
}
// @lc code=end

