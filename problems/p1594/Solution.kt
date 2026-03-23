package problems.p1594
/*
 * @lc app=leetcode id=1594 lang=kotlin
 *
 * [1594] Maximum Non Negative Product in a Matrix
 */

// @lc code=start
class Solution {
    fun maxProductPath(grid: Array<IntArray>): Int {
        val memo = Array(grid.size){Array<Pair<Long, Long>?>(grid.first().size){null} }
        fun dfs(x: Int, y: Int): Pair<Long, Long> {
            if (memo[x][y] != null) return memo[x][y]!!
            if (x == grid.size-1 && y == grid.first().size-1) return Pair(grid[x][y].toLong(), grid[x][y].toLong())
            val right = if (y+1 < grid.first().size) dfs(x, y+1) else null
            val down = if (x+1 < grid.size) dfs(x+1, y) else null
            val candidates = listOfNotNull(right, down).flatMap { listOf(it.first, it.second) }
            val maxCandidate = candidates.maxOrNull() ?: Long.MIN_VALUE
            val minCandidate = candidates.minOrNull() ?: Long.MAX_VALUE
            val currentValue = grid[x][y].toLong()
            memo[x][y] = if (currentValue >= 0){
                Pair(currentValue * maxCandidate, currentValue * minCandidate)
            } else {
                Pair(currentValue * minCandidate, currentValue * maxCandidate)
            }
            return memo[x][y]!!
        }
        val mod = 1_000_000_007L
        val result = dfs(0, 0).first
        return if (result < 0) -1 else (result % mod).toInt()
    }
}
// @lc code=end

