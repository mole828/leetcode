package p22
/*
 * @lc app=leetcode id=22 lang=kotlin
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (79.14%)
 * Likes:    23733
 * Dislikes: 1102
 * Total Accepted:    3.2M
 * Total Submissions: 4M
 * Testcase Example:  '3'
 *
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 * 
 * 
 * Example 1:
 * Input: n = 3
 * Output: ["((()))","(()())","(())()","()(())","()()()"]
 * Example 2:
 * Input: n = 1
 * Output: ["()"]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 8
 * 
 * 
 */

// @lc code=start
class Solution {
    @Deprecated("列举不全")
    fun generateParenthesis0(n: Int): List<String> {
        return when (n) {
            1 -> listOf("()")
            else -> {
                val res = mutableSetOf<String>()
                val lessList = generateParenthesis(n-1)
                lessList.forEach { less ->
                    res.add("($less)")
                    res.add("()$less")
                    res.add("$less()")
                }
                res.toList()
            }
        }
    }
    fun generateParenthesis(n: Int): List<String> {
        val res = mutableListOf<String>()
        fun dfs(s: String, left: Int, right: Int) {
            if (s.length == 2*n) {
                res.add(s)
                return
            }
            if (left < n) dfs("$s(",left+1,right)
            if (right < left) dfs("$s)",left,right+1)
        }
        dfs("",0,0)
        return res
    }
}
// @lc code=end

