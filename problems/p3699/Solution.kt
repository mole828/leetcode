package p3699

/*
 * @lc app=leetcode id=3699 lang=kotlin
 *
 * [3699] Number of ZigZag Arrays I
 */

// @lc code=start
const val MOD = 1_000_000_007L

class Solution {
    @Deprecated("TLE")
    fun zigZagArrays0(n: Int, l: Int, r: Int): Int {
        if (n == 1) return (r - l + 1)

        val memo = mutableMapOf<Triple<Int, Int, Boolean>, Int>()

        fun dfs(i: Int, prev: Int, isUp: Boolean): Int {
            if (i == n) return 1

            val key = Triple(i, prev, isUp)
            memo[key]?.let { return it }

            var count = 0L
            for (j in l..r) {
                if ((isUp && j > prev) || (!isUp && j < prev)) {
                    count = (count + dfs(i + 1, j, !isUp)) % MOD
                }
            }

            memo[key] = count.toInt()
            return count.toInt()
        }

        var totalCount = 0L
        for (j in l..r) {
            totalCount = (totalCount + dfs(1, j, true)) % MOD
            totalCount = (totalCount + dfs(1, j, false)) % MOD
        }

        return totalCount.toInt()
    }
    
    fun zigZagArrays(n: Int, l: Int, r: Int): Int {
        val m = r - l + 1
        if (n == 1) return m

        var up = LongArray(m)
        var down = LongArray(m)

        for (x in 0 until m) {
            up[x] = x.toLong()
            down[x] = (m - 1 - x).toLong()
        }

        for (len in 3..n) {
            val prefixDown = LongArray(m)
            val suffixUp = LongArray(m)

            var sum = 0L
            for (x in 0 until m) {
                sum = (sum + down[x]) % MOD
                prefixDown[x] = sum
            }

            sum = 0L
            for (x in m - 1 downTo 0) {
                sum = (sum + up[x]) % MOD
                suffixUp[x] = sum
            }

            val newUp = LongArray(m)
            val newDown = LongArray(m)

            for (x in 0 until m) {
                newUp[x] = if (x > 0) prefixDown[x - 1] else 0L
                newDown[x] = if (x + 1 < m) suffixUp[x + 1] else 0L
            }

            up = newUp
            down = newDown
        }

        var ans = 0L
        for (x in 0 until m) {
            ans = (ans + up[x] + down[x]) % MOD
        }

        return ans.toInt()
    }
}
// @lc code=end

// 果然还是不擅长前缀和