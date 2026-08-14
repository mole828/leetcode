/*
 * @lc app=leetcode id=3090 lang=kotlin
 *
 * [3090] Maximum Length Substring With Two Occurrences
 *
 * https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/
 *
 * algorithms
 * Easy (65.84%)
 * Likes:    282
 * Dislikes: 23
 * Total Accepted:    73.8K
 * Total Submissions: 110.1K
 * Testcase Example:  '"bcbbbcba"'
 *
 * Given a string s, return the maximum length of a substring such that it
 * contains at most two occurrences of each character.
 * 
 * Example 1:
 * 
 * 
 * Input: s = "bcbbbcba"
 * 
 * Output: 4
 * 
 * Explanation:
 * The following substring has a length of 4 and contains at most two
 * occurrences of each character: "bcbbbcba".
 * 
 * Example 2:
 * 
 * 
 * Input: s = "aaaa"
 * 
 * Output: 2
 * 
 * Explanation:
 * The following substring has a length of 2 and contains at most two
 * occurrences of each character: "aaaa".
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= s.length <= 100
 * s consists only of lowercase English letters.
 * 
 * 
 */
package p3090
// @lc code=start
class Solution {
    fun maximumLengthSubstring(s: String): Int {
        val count = IntArray(26)
        fun d(char: Char, v: Int): Int {
            val i = char - 'a'
            val oldValue = count[i]
            val newValue = oldValue + v
            count[i] = newValue
            return newValue
        }
        var left = 0
        var right = 0
        val n = s.length
        var maxLen = 0
        while (right < n) {
            val rightChar = s[right]
            right += 1
            var cc = d(rightChar, 1)
            while (cc > 2) {
                val leftChar = s[left]
                left += 1
                val leftCount = d(leftChar, -1)
                if (leftChar == rightChar) cc = leftCount
            }
            val len = right - left
            if (len > maxLen) maxLen = len
        }
        return maxLen
    }
}
// @lc code=end

