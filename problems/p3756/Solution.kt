package p3756

/*
 * @lc app=leetcode id=3756 lang=kotlin
 *
 * [3756] Concatenate Non-Zero Digits and Multiply by Sum II
 */

// @lc code=start
const val MOD = 1_000_000_007L
class Solution {
    fun sumAndMultiply(s: String, queries: Array<IntArray>): IntArray {
        val n = s.length
        val values = LongArray(n + 1)
        val sums = LongArray(n + 1)
        val nonZeroCounts = IntArray(n + 1)
        val powersOfTen = LongArray(n + 1)
        powersOfTen[0] = 1L

        for (i in s.indices) {
            val digit = s[i] - '0'
            values[i + 1] = if (digit == 0) {
                values[i]
            } else {
                (values[i] * 10 + digit) % MOD
            }
            sums[i + 1] = sums[i] + digit
            nonZeroCounts[i + 1] = nonZeroCounts[i] + if (digit == 0) 0 else 1
            powersOfTen[i + 1] = powersOfTen[i] * 10 % MOD
        }

        return IntArray(queries.size) { i ->
            val l = queries[i][0]
            val r = queries[i][1]
            val nonZeroCount = nonZeroCounts[r + 1] - nonZeroCounts[l]
            val x = (
                values[r + 1] - values[l] * powersOfTen[nonZeroCount] % MOD + MOD
            ) % MOD
            val sum = sums[r + 1] - sums[l]
            (x * sum % MOD).toInt()
        }
    }
}
// @lc code=end
