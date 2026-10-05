package p856
/*
 * @lc app=leetcode id=856 lang=kotlin
 *
 * [856] Score of Parentheses
 *
 * https://leetcode.com/problems/score-of-parentheses/description/
 *
 * algorithms
 * Medium (63.48%)
 * Likes:    5741
 * Dislikes: 254
 * Total Accepted:    251.3K
 * Total Submissions: 393.3K
 * Testcase Example:  '"()"'
 *
 * Given a balanced parentheses string s, return the score of the string.
 * 
 * The score of a balanced parentheses string is based on the following
 * rule:
 * 
 * 
 * "()" has score 1.
 * AB has score A + B, where A and B are balanced parentheses strings.
 * (A) has score 2 * A, where A is a balanced parentheses string.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "()"
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "(())"
 * Output: 2
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "()()"
 * Output: 2
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= s.length <= 50
 * s consists of only '(' and ')'.
 * s is a balanced parentheses string.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun scoreOfParentheses(s: String): Int {
        var depth = 0
        var ans = 0
        s.forEachIndexed { i, char ->
            when (char) {
                '(' -> depth++
                ')' -> {
                    depth--
                    if (s[i-1]=='(') ans += 1.shl(depth)
                }
            }
        }
        return ans
    }
}
// @lc code=end

