package p3700

/*
 * @lc app=leetcode id=3700 lang=kotlin
 *
 * [3700] Number of ZigZag Arrays II
 */

// @lc code=start
const val MOD = 1_000_000_007L

class Solution {
    fun zigZagArrays(n: Int, l: Int, r: Int): Int {
        val k = r - l + 1
        if (n == 1) return k

        val size = k * 2
        var matrix = Array(size) { LongArray(size) }

        for (i in 0 until k) {
            for (j in 0 until i) {
                matrix[i][k + j] = 1L
            }
            for (j in i + 1 until k) {
                matrix[k + i][j] = 1L
            }
        }

        var vector = LongArray(size) { 1L }
        var power = n - 1
        while (power > 0) {
            if (power and 1 == 1) {
                vector = multiply(matrix, vector)
            }
            matrix = multiply(matrix, matrix)
            power = power shr 1
        }

        var ans = 0L
        for (value in vector) {
            ans = (ans + value) % MOD
        }
        return ans.toInt()
    }

    private fun multiply(a: Array<LongArray>, b: LongArray): LongArray {
        val n = a.size
        val res = LongArray(n)
        for (i in 0 until n) {
            var sum = 0L
            for (j in 0 until n) {
                if (a[i][j] == 0L || b[j] == 0L) continue
                sum = (sum + a[i][j] * b[j]) % MOD
            }
            res[i] = sum
        }
        return res
    }

    private fun multiply(a: Array<LongArray>, b: Array<LongArray>): Array<LongArray> {
        val n = a.size
        val res = Array(n) { LongArray(n) }
        for (i in 0 until n) {
            for (mid in 0 until n) {
                if (a[i][mid] == 0L) continue
                for (j in 0 until n) {
                    if (b[mid][j] == 0L) continue
                    res[i][j] = (res[i][j] + a[i][mid] * b[mid][j]) % MOD
                }
            }
        }
        return res
    }
}
// @lc code=end
