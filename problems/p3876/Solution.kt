package p3876

/*
 * @lc app=leetcode id=3876 lang=kotlin
 *
 * [3876] Construct Uniform Parity Array II
 */

// @lc code=start
class Solution {
    fun uniformArray(nums1: IntArray): Boolean {
        val minOdd = nums1.filter { it % 2 != 0 }.minOrNull() ?: Int.MAX_VALUE
        val minEven = nums1.filter { it % 2 == 0 }.minOrNull() ?: Int.MAX_VALUE
        return minOdd == Int.MAX_VALUE || minEven == Int.MAX_VALUE || minOdd < minEven
    }
}
// @lc code=end

