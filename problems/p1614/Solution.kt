package p1614

/*
 * @lc app=leetcode id=1614 lang=kotlin
 *
 * [1614] Maximum Nesting Depth of the Parentheses
 */

// @lc code=start
class Solution {
    fun maxDepth(s: String): Int {
        var maxDepth = 0
        var currentDepth = 0
        for (char in s) {
            when (char) {
                '(' -> maxDepth = maxOf(maxDepth, ++currentDepth)
                ')' -> currentDepth--
            }
        }
        return maxDepth
    }
}
// @lc code=end

