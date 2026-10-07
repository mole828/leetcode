package p301
/*
 * @lc app=leetcode id=301 lang=kotlin
 *
 * [301] Remove Invalid Parentheses
 *
 * https://leetcode.com/problems/remove-invalid-parentheses/description/
 *
 * algorithms
 * Hard (50.13%)
 * Likes:    6116
 * Dislikes: 303
 * Total Accepted:    522.3K
 * Total Submissions: 1M
 * Testcase Example:  '"()())()"'
 *
 * Given a string s that contains parentheses and letters, remove the minimum
 * number of invalid parentheses to make the input string valid.
 * 
 * Return a list of unique strings that are valid with the minimum number of
 * removals. You may return the answer in any order.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "()())()"
 * Output: ["(())()","()()()"]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "(a)())()"
 * Output: ["(a())()","(a)()()"]
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = ")("
 * Output: [""]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 25
 * s consists of lowercase English letters and parentheses '(' and ')'.
 * There will be at most 20 parentheses in s.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun removeInvalidParentheses(s: String): List<String> {
        fun isValid(s: String): Boolean {
            var left = 0
            s.forEach { 
                when (it) {
                    '(' -> left+=1
                    ')' -> if (left==0) return false else left-=1
                }
            }
            return left == 0
        }
        var cur = setOf(s)
        while (true) {
            val ans = cur.filter { isValid(it) }
            if (ans.isNotEmpty()) return ans

            val nxt = mutableSetOf<String>()
            for (t in cur) {
                for (i in t.indices) {
                    val ch = t[i]
                    if (ch != '(' && ch != ')') continue
                    if (i > 0 && ch == t[i - 1]) continue
                    nxt.add(t.removeRange(i, i + 1))
                }
            }
            cur = nxt
        }
    }
}
// @lc code=end
