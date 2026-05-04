package problems.p48
/*
 * @lc app=leetcode id=48 lang=kotlin
 *
 * [48] Rotate Image
 */
// @lc code=start
class Solution {
    fun rotate(matrix: Array<IntArray>): Unit {
        val n = matrix.size
        for (i in 0..<n) {
            for (j in 0..<n) {
                if (i < j) {
                    val temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                }
            }
        }
        matrix.forEach { it.reverse() }
    }
}
// @lc code=end

