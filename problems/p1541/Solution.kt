package p1541

/*
 * @lc app=leetcode id=1541 lang=kotlin
 *
 * [1541] Minimum Insertions to Balance a Parentheses String
 *
 * https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/
 *
 * algorithms
 * Medium (53.62%)
 * Likes:    1310
 * Dislikes: 303
 * Total Accepted:    90.7K
 * Total Submissions: 167K
 * Testcase Example:  '"(()))"'
 *
 * Given a parentheses string s containing only the characters '(' and ')'. A
 * parentheses string is balanced if:
 * 
 * 
 * Any left parenthesis '(' must have a corresponding two consecutive right
 * parenthesis '))'.
 * Left parenthesis '(' must go before the corresponding two consecutive right
 * parenthesis '))'.
 * 
 * 
 * In other words, we treat '(' as an opening parenthesis and '))' as a closing
 * parenthesis.
 * 
 * 
 * For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))"
 * and "(()))" are not balanced.
 * 
 * 
 * You can insert the characters '(' and ')' at any position of the string to
 * balance it if needed.
 * 
 * Return the minimum number of insertions needed to make s balanced.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "(()))"
 * Output: 1
 * Explanation: The second '(' has two matching '))', but the first '(' has
 * only ')' matching. We need to add one more ')' at the end of the string to
 * be "(())))" which is balanced.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "())"
 * Output: 0
 * Explanation: The string is already balanced.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "))())("
 * Output: 3
 * Explanation: Add '(' to match the first '))', Add '))' to match the last
 * '('.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s consists of '(' and ')' only.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun minInsertions(s: String): Int {
        var left = 0
        var ans = 0
        var i = 0
        val n = s.length
        while (i < n) {
            val char = s[i]
            when (char) {
                '(' -> {
                    left += 1
                    i += 1
                }
                else -> {
                    if (left>0) left -= 1
                    else ans += 1
                    
                    i += if (i < n-1 && s[i+1]==')')
                        2
                    else {
                        ans += 1
                        1
                    }
                }
            }    
        }
        return ans + left * 2
    }
}
// @lc code=end

