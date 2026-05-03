package problems.p796
/*
 * @lc app=leetcode id=796 lang=kotlin
 *
 * [796] Rotate String
 */
// @lc code=start
class Solution {
    fun rotateString(s: String, goal: String): Boolean {
        return (s in goal + goal) and (s.length == goal.length)
    }
}
// @lc code=end

