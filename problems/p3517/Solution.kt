/*
 * @lc app=leetcode id=3517 lang=kotlin
 *
 * [3517] Smallest Palindromic Rearrangement I
 *
 * https://leetcode.com/problems/smallest-palindromic-rearrangement-i/description/
 *
 * algorithms
 * Medium (63.92%)
 * Likes:    105
 * Dislikes: 3
 * Total Accepted:    41.1K
 * Total Submissions: 62.8K
 * Testcase Example:  '"z"'
 *
 * You are given a palindromic string s.
 * 
 * Return the lexicographically smallest palindromic permutation of s.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "z"
 * 
 * Output: "z"
 * 
 * Explanation:
 * 
 * A string of only one character is already the lexicographically smallest
 * palindrome.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "babab"
 * 
 * Output: "abbba"
 * 
 * Explanation:
 * 
 * Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "daccad"
 * 
 * Output: "acddca"
 * 
 * Explanation:
 * 
 * Rearranging "daccad" → "acddca" gives the smallest lexicographic
 * palindrome.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s consists of lowercase English letters.
 * s is guaranteed to be palindromic.
 * 
 * 
 */
package p3517
// @lc code=start
class Solution {
    fun smallestPalindrome(s: String): String {
        val count = IntArray(26)
        s.forEach { count[it - 'a']++ }
        val n = s.length
        val sb = StringBuilder()
        for (i in 0..25) {
            repeat(count[i] / 2) { sb.append('a' + i) }
        }
        val half = sb.toString()
        val middle = count.indexOfFirst { it % 2 == 1 }.let {
            if (it == -1) "" else ('a' + it).toString()
        }
        return half + middle + half.reversed()
    }
}
// @lc code=end

