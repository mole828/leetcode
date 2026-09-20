package p3498

/*
 * @lc app=leetcode id=3498 lang=kotlin
 *
 * [3498] Reverse Degree of a String
 */

// @lc code=start
class Solution {
    fun reverseDegree(s: String): Int {
        return s.mapIndexed { index, char ->
            val re = 27 - (char - 'a' + 1)
            (index + 1) * re
        }.sum()
    }
}
// @lc code=end

