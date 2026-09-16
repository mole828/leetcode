package p1621

/*
 * @lc app=leetcode id=1621 lang=kotlin
 *
 * [1621] Number of Sets of K Non-Overlapping Line Segments
 */

// @lc code=start
class Solution {
    val mod = 1_000_000_007

    fun numberOfSets(n: Int, k: Int): Int {
        val memo = Array(n + 1) { IntArray(k + 1) }
        for (i in 0..n) memo[i][0] = 1

        for (need in 1..k) {
            var endpointSum = 0
            for (i in (n - 2) downTo 0) {
                endpointSum = (endpointSum + memo[i + 1][need - 1]) % mod
                memo[i][need] = (memo[i + 1][need] + endpointSum) % mod
            }
        }

        return memo[0][k]
    }
}
// @lc code=end
