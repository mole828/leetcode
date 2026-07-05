package p1301
/*
 * @lc app=leetcode id=1301 lang=kotlin
 *
 * [1301] Number of Paths with Max Score
 */
// @lc code=start
const val MOD = 1000000007L
class Solution {
    fun pathsWithMaxScore(board: List<String>): IntArray {
        val memo = Array(board.size) { Array(board[0].length) { Pair(-1, -1L) } }
        fun dfs(x: Int, y: Int): Pair<Int, Long> {
            if (x == 0 && y == 0) return Pair(0, 1)
            if (x < 0 || y < 0 || board[x][y] == 'X') return Pair(Int.MIN_VALUE, 0)
            if (memo[x][y] != Pair(-1, -1L)) return memo[x][y]

            val (score1, count1) = dfs(x - 1, y)
            val (score2, count2) = dfs(x, y - 1)
            val (score3, count3) = dfs(x - 1, y - 1)

            val maxScore = maxOf(score1, score2, score3)
            val totalCount = (if (score1 == maxScore) count1 else 0) +
                    (if (score2 == maxScore) count2 else 0) +
                    (if (score3 == maxScore) count3 else 0)

            val result = Pair(
                maxScore + if (board[x][y] == 'E' || board[x][y] == 'S') 0 else board[x][y].digitToInt(), 
                totalCount % MOD
            )
            memo[x][y] = result
            return result
        }
        val (maxScore, totalCount) = dfs(board.size - 1, board[0].length - 1)
        if (maxScore < 0) return intArrayOf(0, 0)
        return intArrayOf(maxScore, totalCount.toInt())
    }
}
// @lc code=end

fun main() {
    println(Solution().pathsWithMaxScore(listOf("E23", "2X2", "12S")).contentToString()) // Output: [7, 1]
}
