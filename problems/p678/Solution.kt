package p678

import kotlin.math.absoluteValue

/*
 * @lc app=leetcode id=678 lang=kotlin
 *
 * [678] Valid Parenthesis String
 *
 * https://leetcode.com/problems/valid-parenthesis-string/description/
 *
 * algorithms
 * Medium (40.46%)
 * Likes:    7225
 * Dislikes: 232
 * Total Accepted:    656.3K
 * Total Submissions: 1.6M
 * Testcase Example:  '"()"'
 *
 * Given a string s containing only three types of characters: '(', ')' and
 * '*', return true if s is valid.
 * 
 * The following rules define a valid string:
 * 
 * 
 * Any left parenthesis '(' must have a corresponding right parenthesis
 * ')'.
 * Any right parenthesis ')' must have a corresponding left parenthesis
 * '('.
 * Left parenthesis '(' must go before the corresponding right parenthesis
 * ')'.
 * '*' could be treated as a single right parenthesis ')' or a single left
 * parenthesis '(' or an empty string "".
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "()"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "(*)"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "(*))"
 * Output: true
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: s = "("
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 100
 * s[i] is '(', ')' or '*'.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun checkValidString(s: String): Boolean {
        run { 
            var left = 0
            var right = 0
            var any = 0
            s.forEach { char ->
                when (char) {
                    '(' -> left++
                    ')' -> right++
                    '*' -> any++
                }
                if (right > left+any) return false
            }
        }
        run {
            var left = 0
            var right = 0
            var any = 0
            s.reversed().forEach { char ->
                when (char) {
                    ')' -> left++
                    '(' -> right++
                    '*' -> any++
                }
                if (right > left+any) return false
            }
        }
        return true
    }
}
// @lc code=end

