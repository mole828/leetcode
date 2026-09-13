package p835
/*
 * @lc app=leetcode id=835 lang=kotlin
 *
 * [835] Image Overlap
 */
// @lc code=start
class Solution {
    fun oneByOneOverlap(img1: Array<IntArray>, img2: Array<IntArray>): Int {
        val n = img1.size
        var maxOverlap = 0
        for (xShift in -n + 1 until n) {
            for (yShift in -n + 1 until n) {
                var overlap = 0
                for (i in 0 until n) {
                    for (j in 0 until n) {
                        val newI = i + xShift
                        val newJ = j + yShift
                        if (newI in 0 until n && newJ in 0 until n) {
                            overlap += img1[i][j] * img2[newI][newJ]
                        }
                    }
                }
                maxOverlap = maxOf(maxOverlap, overlap)
            }
        }
        return maxOverlap
    }
    fun largestOverlap(img1: Array<IntArray>, img2: Array<IntArray>): Int {
        return oneByOneOverlap(img1, img2)
    }
}
// @lc code=end

