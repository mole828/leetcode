package p3838
/*
 * @lc app=leetcode id=3838 lang=kotlin
 *
 * [3838] Weighted Word Mapping
 */
// @lc code=start
class Solution {
    fun mapWordWeights(words: Array<String>, weights: IntArray): String {
        fun String.weight() = sumOf { weights[it - 'a'] } % 26
        return words.map { Char('z'.code - it.weight()) }.joinToString("")
    }
}
// @lc code=end

