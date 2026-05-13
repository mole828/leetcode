package p1914
/*
 * @lc app=leetcode id=1914 lang=kotlin
 *
 * [1914] Cyclically Rotating a Grid
 */

// @lc code=start
class Solution {
    fun rotateGrid(grid: Array<IntArray>, k: Int): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val ans = Array(m) { grid[it].clone() }

        repeat(minOf(m, n) / 2) { layer ->
            val top = layer
            val left = layer
            val bottom = m - 1 - layer
            val right = n - 1 - layer
            val places = buildList {
                for (j in left..right) add(top to j)
                for (i in top + 1..bottom) add(i to right)
                for (j in right - 1 downTo left) add(bottom to j)
                for (i in bottom - 1 downTo top + 1) add(i to left)
            }
            val values = places.map { (i, j) -> grid[i][j] }
            val shift = k % values.size

            places.forEachIndexed { index, (i, j) ->
                ans[i][j] = values[(index + shift) % values.size]
            }
        }

        return ans
    }
}
// @lc code=end
