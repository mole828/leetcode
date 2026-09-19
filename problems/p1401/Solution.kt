package p1401
/*
 * @lc app=leetcode id=1401 lang=kotlin
 *
 * [1401] Circle and Rectangle Overlapping
 */
// @lc code=start
class Solution {
    fun checkOverlap(radius: Int, xCenter: Int, yCenter: Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean {
        val closestX = xCenter.coerceIn(x1, x2)
        val closestY = yCenter.coerceIn(y1, y2)
        val distanceX = xCenter - closestX
        val distanceY = yCenter - closestY
        return distanceX * distanceX + distanceY * distanceY <= radius * radius
    }
}
// @lc code=end

