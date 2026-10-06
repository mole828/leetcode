package p921
/*
 * @lc app=leetcode id=921 lang=kotlin
 *
 * [921] Minimum Add to Make Parentheses Valid
 *
 * https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
 *
 * algorithms
 * Medium (74.26%)
 * Likes:    5046
 * Dislikes: 252
 * Total Accepted:    746.6K
 * Total Submissions: 1M
 * Testcase Example:  '"())"'
 *
 * A parentheses string is valid if and only if:
 * 
 * 
 * It is the empty string,
 * It can be written as AB (A concatenated with B), where A and B are valid
 * strings, or
 * It can be written as (A), where A is a valid string.
 * 
 * 
 * You are given a parentheses string s. In one move, you can insert a
 * parenthesis at any position of the string.
 * 
 * 
 * For example, if s = "()))", you can insert an opening parenthesis to be
 * "(()))" or a closing parenthesis to be "())))".
 * 
 * 
 * Return the minimum number of moves required to make s valid.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "())"
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "((("
 * Output: 3
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 1000
 * s[i] is either '(' or ')'.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun minAddToMakeValid(s: String): Int {
        val stack = mutableListOf<Char>()
        var need = 0
        s.forEach { 
            when (it) {
                '(' -> stack.add(it)
                ')' -> {
                    if (stack.isNotEmpty() && stack.last() == '(') {
                        stack.removeLast()
                    } else need+=1
                }
            }
        }
        return need + stack.size
    }
}
// @lc code=end

