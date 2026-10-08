package p1021

/*
 * @lc app=leetcode id=1021 lang=kotlin
 *
 * [1021] Remove Outermost Parentheses
 *
 * https://leetcode.com/problems/remove-outermost-parentheses/description/
 *
 * algorithms
 * Easy (87.28%)
 * Likes:    3918
 * Dislikes: 1744
 * Total Accepted:    765.7K
 * Total Submissions: 874.4K
 * Testcase Example:  '"(()())(())"'
 *
 * A valid parentheses string is either empty "", "(" + A + ")", or A + B,
 * where A and B are valid parentheses strings, and + represents string
 * concatenation.
 * 
 * 
 * For example, "", "()", "(())()", and "(()(()))" are all valid parentheses
 * strings.
 * 
 * 
 * A valid parentheses string s is primitive if it is nonempty, and there does
 * not exist a way to split it into s = A + B, with A and B nonempty valid
 * parentheses strings.
 * 
 * Given a valid parentheses string s, consider its primitive decomposition: s
 * = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
 * 
 * Return s after removing the outermost parentheses of every primitive string
 * in the primitive decomposition of s.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "(()())(())"
 * Output: "()()()"
 * Explanation: 
 * The input string is "(()())(())", with primitive decomposition "(()())" +
 * "(())".
 * After removing outer parentheses of each part, this is "()()" + "()" =
 * "()()()".
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "(()())(())(()(()))"
 * Output: "()()()()(())"
 * Explanation: 
 * The input string is "(()())(())(()(()))", with primitive decomposition
 * "(()())" + "(())" + "(()(()))".
 * After removing outer parentheses of each part, this is "()()" + "()" +
 * "()(())" = "()()()()(())".
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "()()"
 * Output: ""
 * Explanation: 
 * The input string is "()()", with primitive decomposition "()" + "()".
 * After removing outer parentheses of each part, this is "" + "" = "".
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s[i] is either '(' or ')'.
 * s is a valid parentheses string.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun removeOuterParentheses(s: String): String {
        val arr = mutableListOf<String>()
        var stack = mutableListOf<Char>()
        var deep = 0
        s.forEach { char ->
            when (char) {
                '(' -> deep += 1
                ')' -> deep -= 1
            }
            stack.add(char)
            if (deep==0) {
                stack.removeFirst()
                stack.removeLast()
                arr.add(stack.joinToString(""))
                stack = mutableListOf()
            }
        }
        println(arr)
        return arr.joinToString("")
    }
}
// @lc code=end

fun main() {
    println(Solution().removeOuterParentheses("(()())(())"))
}