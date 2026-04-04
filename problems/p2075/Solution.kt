package problems.p2075
/*
 * @lc app=leetcode id=2075 lang=kotlin
 *
 * [2075] Decode the Slanted Ciphertext
 */
// @lc code=start
class Solution {
    fun decodeCiphertext(encodedText: String, rows: Int): String {
        val cols = encodedText.length / rows
        val arr = Array(rows) { CharArray(cols) }
        for (i in 0 until rows) {
            for (j in 0 until cols) {
                arr[i][j] = encodedText[i * cols + j]
            }
        }
        val sb = StringBuilder()
        for (d in 0 until cols) {
            for (i in 0 until rows) {
                val j = d + i
                if (j < cols) {
                    sb.append(arr[i][j])
                }
            }
        }
        return sb.toString().trimEnd()
    }
}
// @lc code=end

