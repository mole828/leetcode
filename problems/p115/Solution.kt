package p115
/*
 * @lc app=leetcode id=115 lang=kotlin
 *
 * [115] Distinct Subsequences
 */
// @lc code=start
class Solution {
    fun numDistinct(s: String, t: String): Int {
        val dp = Array(s.length + 1) { IntArray(t.length + 1) }
        for (i in dp.indices) {
            dp[i][0] = 1
        }
        for (i in 1..s.length) {
            for (j in 1..t.length) {
                dp[i][j] = dp[i - 1][j]
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] += dp[i - 1][j - 1]
                }
            }
        }
        return dp[s.length][t.length]
    }
}
// @lc code=end

