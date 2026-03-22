package problems.p1886
/*
 * @lc app=leetcode id=1886 lang=kotlin
 *
 * [1886] Determine Whether Matrix Can Be Obtained By Rotation
 */
// @lc code=start
class Solution {
    fun findRotation(mat: Array<IntArray>, target: Array<IntArray>): Boolean {
        repeat(4) {
            if (mat.contentDeepEquals(target)) return true
            rotate(mat)
        }
        return false
    }

    private fun rotate(matrix: Array<IntArray>) {
        val n = matrix.size
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                matrix[i][j] = matrix[j][i].also { matrix[j][i] = matrix[i][j]}
            }
            matrix[i].reverse()
        }
    }
}
// @lc code=end

