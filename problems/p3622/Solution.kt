package p3622
/*
 * @lc app=leetcode id=3622 lang=kotlin
 *
 * [3622] Check Divisibility by Digit Sum and Product
 */
// @lc code=start
class Solution {
    fun checkDivisibility(n: Int): Boolean {
        val digits = n.toString().map { it - '0' }
        val sum = digits.sum()
        val product = digits.fold(1) { acc, d -> acc * d }
        return n % (sum + product) == 0
    }
}
// @lc code=end

