package p1861
/*
 * @lc app=leetcode id=1861 lang=kotlin
 *
 * [1861] Rotating the Box
 */

// @lc code=start
class Solution {
    fun rotateTheBox(boxGrid: Array<CharArray>): Array<CharArray> {
        val rows = boxGrid.size
        val cols = boxGrid[0].size
        val ans = Array(cols) { CharArray(rows) { '.' } }

        for (r in 0 until rows) {
            var drop = cols - 1
            for (c in cols - 1 downTo 0) {
                when (boxGrid[r][c]) {
                    '*' -> {
                        ans[c][rows - 1 - r] = '*'
                        drop = c - 1
                    }
                    '#' -> {
                        ans[drop][rows - 1 - r] = '#'
                        drop--
                    }
                }
            }
        }

        return ans
    }
}
// @lc code=end
