package problems.p3418

/*
 * @lc app=leetcode id=3418 lang=kotlin
 *
 * [3418] Maximum Amount of Money Robot Can Earn
 */

// @lc code=start
class Solution {
    fun maximumAmount(coins: Array<IntArray>): Int {
        val rows = coins.size
        val cols = coins[0].size
        val maxNeutralize = 2
        val negInf = Int.MIN_VALUE / 4

        // dp[i][j][k]: max coins when reaching (i, j) after using exactly k neutralizations.
        val dp = Array(rows) { Array(cols) { IntArray(maxNeutralize + 1) { negInf } } }

        fun bestFromTopOrLeft(i: Int, j: Int, used: Int): Int {
            val fromTop = if (i > 0) dp[i - 1][j][used] else negInf
            val fromLeft = if (j > 0) dp[i][j - 1][used] else negInf
            return maxOf(fromTop, fromLeft)
        }

        val start = coins[0][0]
        dp[0][0][0] = start
        if (start < 0) dp[0][0][1] = 0

        for (i in 0 until rows) {
            for (j in 0 until cols) {
                if (i == 0 && j == 0) continue

                val cell = coins[i][j]
                for (used in 0..maxNeutralize) {
                    val keepCell = bestFromTopOrLeft(i, j, used)
                    if (keepCell != negInf) {
                        dp[i][j][used] = maxOf(dp[i][j][used], keepCell + cell)
                    }

                    if (cell < 0 && used > 0) {
                        val neutralized = bestFromTopOrLeft(i, j, used - 1)
                        if (neutralized != negInf) {
                            dp[i][j][used] = maxOf(dp[i][j][used], neutralized)
                        }
                    }
                }
            }
        }

        return dp[rows - 1][cols - 1].max()
    }
}
// @lc code=end
