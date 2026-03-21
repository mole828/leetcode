package problems.p3643
/*
 * @lc app=leetcode id=3643 lang=kotlin
 *
 * [3643] Flip Square Submatrix Vertically
 */
// @lc code=start
class Solution {
    fun reverseSubmatrix(grid: Array<IntArray>, x: Int, y: Int, k: Int): Array<IntArray> {
        var l = x
        var r = x + k - 1
        while (l <= r) {
            for (j in y until y + k) {
                grid[l][j] = grid[r][j].also { grid[r][j] = grid[l][j] }
            }
            l++
            r--
        }
        return grid
    }
}
// @lc code=end

