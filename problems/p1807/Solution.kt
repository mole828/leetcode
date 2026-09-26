package p1807
/*
 * @lc app=leetcode id=1807 lang=kotlin
 *
 * [1807] Evaluate the Bracket Pairs of a String
 */
// @lc code=start
class Solution {
    fun evaluate(s: String, knowledge: List<List<String>>): String {
        val map = knowledge.associate { it[0] to it[1] }
        val result = StringBuilder(s.length)
        var keyStart = -1

        for (i in s.indices) {
            when (s[i]) {
                '(' -> keyStart = i + 1
                ')' -> {
                    val key = s.substring(keyStart, i)
                    result.append(map[key] ?: "?")
                    keyStart = -1
                }
                else -> {
                    if (keyStart == -1) {
                        result.append(s[i])
                    }
                }
            }
        }
        return result.toString()
    }
}
// @lc code=end
