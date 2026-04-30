package problems.p3225
/*
 * @lc app=leetcode id=3225 lang=kotlin
 *
 * [3225] Maximum Score From Grid Operations
 */

// @lc code=start
class Solution {
    fun maximumScore(grid: Array<IntArray>): Long {
        val n = grid.size
        val prefix = Array(n) { LongArray(n + 1) }

        for (col in 0 until n) {
            for (row in 0 until n) {
                prefix[col][row + 1] = prefix[col][row] + grid[row][col].toLong()
            }
        }

        var prevPick = LongArray(n + 1)
        var prevSkip = LongArray(n + 1)

        for (col in 1 until n) {
            val currPick = LongArray(n + 1)
            val currSkip = LongArray(n + 1)

            for (curr in 0..n) {
                for (prev in 0..n) {
                    if (curr > prev) {
                        val score = prefix[col - 1][curr] - prefix[col - 1][prev]
                        currPick[curr] = maxOf(currPick[curr], prevSkip[prev] + score)
                        currSkip[curr] = maxOf(currSkip[curr], prevSkip[prev] + score)
                    } else {
                        val score = prefix[col][prev] - prefix[col][curr]
                        currPick[curr] = maxOf(currPick[curr], prevPick[prev] + score)
                        currSkip[curr] = maxOf(currSkip[curr], prevPick[prev])
                    }
                }
            }

            prevPick = currPick
            prevSkip = currSkip
        }

        return prevPick.maxOrNull() ?: 0L
    }
}
// @lc code=end
