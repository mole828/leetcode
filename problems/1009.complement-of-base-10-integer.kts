/*
 * @lc app=leetcode id=1009 lang=kotlin
 *
 * [1009] Complement of Base 10 Integer
 */

// @lc code=start
class Solution {
    fun bitwiseComplement(n: Int): Int =
        n.toString(radix=2)
            .map {
                return@map when (it) {
                    '0' -> '1'
                    '1' -> '0'
                    else -> '0'
                }
            }
            .joinToString("")
            .toInt(radix=2)
}
// @lc code=end

println(Solution().bitwiseComplement(5))