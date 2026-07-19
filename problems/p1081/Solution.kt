package p1081
/*
 * @lc app=leetcode id=1081 lang=kotlin
 *
 * [1081] Smallest Subsequence of Distinct Characters
 */
// @lc code=start
class Solution {
    fun smallestSubsequence(s: String): String {
        val left = IntArray(26) { 0 }
        for (c in s) {
            left[c - 'a'] += 1
        }
        val ans = mutableListOf<Char>()
        val inAns = BooleanArray(26) { false }
        for (c in s) {
            left[c - 'a'] -= 1
            if (inAns[c - 'a']) continue
            while (ans.isNotEmpty() && ans.last() > c && left[ans.last() - 'a'] > 0) {
                inAns[ans.removeAt(ans.size - 1) - 'a'] = false
            }
            ans.add(c)
            inAns[c - 'a'] = true
        }
        return ans.joinToString("")
    }
}
// @lc code=end

