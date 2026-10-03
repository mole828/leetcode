package p32
/*
 * @lc app=leetcode id=32 lang=kotlin
 *
 * [32] Longest Valid Parentheses
 *
 * https://leetcode.com/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (39.65%)
 * Likes:    13604
 * Dislikes: 479
 * Total Accepted:    1.2M
 * Total Submissions: 3M
 * Testcase Example:  '"(()"'
 *
 * Given a string containing just the characters '(' and ')', return the length
 * of the longest valid (well-formed) parentheses substring.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "(()"
 * Output: 2
 * Explanation: The longest valid parentheses substring is "()".
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = ")()())"
 * Output: 4
 * Explanation: The longest valid parentheses substring is "()()".
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = ""
 * Output: 0
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= s.length <= 3 * 10^4
 * s[i] is '(', or ')'.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun longestValidParentheses(s: String): Int {
        var left = 0
        var right = 0
        var maxLen = 0

        for (char in s) {
            if (char == '(') left++ else right++

            if (left == right) {
                maxLen = maxOf(maxLen, left * 2)
            } else if (right > left) {
                left = 0
                right = 0
            }
        }

        left = 0
        right = 0

        for (i in s.lastIndex downTo 0) {
            if (s[i] == '(') left++ else right++

            if (left == right) {
                maxLen = maxOf(maxLen, left * 2)
            } else if (left > right) {
                left = 0
                right = 0
            }
        }

        return maxLen
    }
}
// @lc code=end
