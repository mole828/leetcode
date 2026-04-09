package problems.p3655
/*
 * @lc app=leetcode id=3655 lang=kotlin
 *
 * [3655] XOR After Range Multiplication Queries II
 */

// @lc code=start
const val MOD = 1_000_000_007L

class Solution {
    fun xorAfterQueries(nums: IntArray, queries: Array<IntArray>): Int {
        val n = nums.size
        val block = kotlin.math.sqrt(queries.size.toDouble()).toInt().coerceAtLeast(1)
        val values = nums.copyOf()
        val lazyDiff = arrayOfNulls<IntArray>(block)

        for (query in queries) {
            val left = query[0]
            val right = query[1]
            val step = query[2]
            val multiplier = query[3]

            if (step < block) {
                val d = lazyDiff[step] ?: IntArray(n) { 1 }.also { lazyDiff[step] = it }
                d[left] = modMul(d[left], multiplier)
                val end = right - (right - left) % step + step
                if (end < n) d[end] = modMul(d[end], modInverse(multiplier))
            } else {
                for (idx in left..right step step) {
                    values[idx] = modMul(values[idx], multiplier)
                }
            }
        }

        for (step in lazyDiff.indices) {
            val d = lazyDiff[step] ?: continue
            for (start in 0 until step) {
                var prefixMul = 1
                for (idx in start until n step step) {
                    prefixMul = modMul(prefixMul, d[idx])
                    values[idx] = modMul(values[idx], prefixMul)
                }
            }
        }

        return values.fold(0) { acc, value -> acc xor value }
    }

    private fun modMul(a: Int, b: Int): Int = ((a.toLong() * b) % MOD).toInt()

    private fun modInverse(x: Int): Int = modPow(x.toLong(), MOD - 2).toInt()

    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) != 0L) {
                res = res * b % MOD
            }
            b = b * b % MOD
            e = e shr 1
        }
        return res
    }
}
// @lc code=end
