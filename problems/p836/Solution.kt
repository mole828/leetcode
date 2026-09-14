package p836

/*
 * @lc app=leetcode id=836 lang=kotlin
 *
 * [836] Rectangle Overlap
 */

// @lc code=start
class Solution {
    fun isRectangleOverlap(rec1: IntArray, rec2: IntArray): Boolean {
        val (x1, y1, x2, y2) = rec1
        val (x3, y3, x4, y4) = rec2
        return x1 < x4 && x3 < x2 && y1 < y4 && y3 < y2
    }
}
// @lc code=end

