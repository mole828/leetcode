package p3612

/*
 * @lc app=leetcode id=3612 lang=kotlin
 *
 * [3612] Process String with Special Operations I
 */

// @lc code=start
class Solution {
    fun processStr(s: String): String {
        val sb = StringBuilder()
        for (cmdChar in s) {
            when (cmdChar) {
                '#' -> sb.append(sb.toString())
                '%' -> sb.reverse()
                '*' -> if(sb.isNotEmpty()) sb.deleteCharAt(sb.length - 1)
                else -> sb.append(cmdChar)
            }
            println(sb)
        }
        return sb.toString()
    }
}
// @lc code=end

