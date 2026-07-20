package p1260

/*
 * @lc app=leetcode id=1260 lang=kotlin
 *
 * [1260] Shift 2D Grid
 */

// @lc code=start
class Solution {
    fun shiftGrid(grid: Array<IntArray>, k: Int): List<List<Int>> {
        val m = grid.size
        val n = grid[0].size
        var grid: Array<IntArray> = grid
        repeat(k) {
            val newGrid = Array(m) { IntArray(n) }
            for (i in 0 until m) {
                for (j in 0 until n) {
                    when (j) {
                        n - 1 -> {
                            when (i) {
                                m - 1 -> newGrid[0][0] = grid[i][j]
                                else -> newGrid[i + 1][0] = grid[i][j]
                            }
                        }
                        else -> newGrid[i][j + 1] = grid[i][j]
                    }
                }
            }
            grid = newGrid
        }
        return grid.map { it.toList() }
    }
}
// @lc code=end

