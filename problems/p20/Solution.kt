package p20
/*
 * @lc app=leetcode id=20 lang=kotlin
 *
 * [20] Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (44.83%)
 * Likes:    28667
 * Dislikes: 2050
 * Total Accepted:    8.3M
 * Total Submissions: 18.3M
 * Testcase Example:  '"()"'
 *
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * 
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Every close bracket has a corresponding open bracket of the same type.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "()"
 * 
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "()[]{}"
 * 
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "(]"
 * 
 * Output: false
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: s = "([])"
 * 
 * Output: true
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: s = "([)]"
 * 
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^4
 * s consists of parentheses only '()[]{}'.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun isValid0(s: String): Boolean {
        val count = IntArray(3)
        runCatching { 
            s.forEach {
                when (it) {
                    '(' -> count[0]++
                    ')' -> require(--count[0] >= 0)
                    '[' -> count[1]++
                    ']' -> require(--count[1] >= 0)
                    '{' -> count[2]++
                    '}' -> require(--count[2] >= 0)
                }
            }
        }.onFailure { return false }
        return true
    }

    fun isValid(s: String): Boolean {
        val stack = mutableListOf<Char>()
        runCatching { 
            s.forEach { char ->
                when (char) {
                    '(', '[', '{' -> stack.add(char)
                    else -> require(
                        stack.removeLast()
                        == when (char) {
                            ')' -> '('
                            ']' -> '['
                            '}' -> '{'
                            else -> error("?")
                        }
                    )
                }
            }
        }.onFailure { return false }
        return stack.isEmpty()
    }
}
// @lc code=end

