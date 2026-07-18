package p1979
/*
 * @lc app=leetcode id=1979 lang=kotlin
 *
 * [1979] Find Greatest Common Divisor of Array
 */
// @lc code=start
class Solution {
    private fun gcd(a: Int, b: Int): Int {
        return if (b == 0) a else gcd(b, a % b)
    }
    fun findGCD(nums: IntArray): Int {
        val a = nums.min()
        val b = nums.max()
        return gcd(a, b)
    }
}
// @lc code=end

