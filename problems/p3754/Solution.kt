package p3754
/*
 * @lc app=leetcode id=3754 lang=kotlin
 *
 * [3754] Concatenate Non-Zero Digits and Multiply by Sum I
 */
// @lc code=start
class Solution {
    fun sumAndMultiply(n: Int): Long {
        val digits = n.toString().filter { it != '0' }
        val x = if (digits.isNotEmpty()) digits.toLong() else 0
        val sum = digits.sumOf { it.digitToInt() }
        return x * sum
    }
}
// @lc code=end

