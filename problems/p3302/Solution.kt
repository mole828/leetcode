/*
 * @lc app=leetcode id=3302 lang=kotlin
 *
 * [3302] Find the Lexicographically Smallest Valid Sequence
 *
 * https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/description/
 *
 * algorithms
 * Medium (21.79%)
 * Likes:    410
 * Dislikes: 101
 * Total Accepted:    67.9K
 * Total Submissions: 120.2K
 * Testcase Example:    '"vbcca"\n"abc"'
 *
 * You are given two strings word1 and word2.
 * 
 * A string x is called almost equal to y if you can change at most one
 * character in x to make it identical to y.
 * 
 * A sequence of indices seq is called valid if:
 * 
 *
 * The indices are sorted in ascending order.
 * Concatenating the characters at these indices in word1 in the same order
 * results in a string that is almost equal to word2.
 *
 *
 * Return an array of size word2.length representing the lexicographically
 * smallest valid sequence of indices. If no such sequence of indices exists,
 * return an empty array.
 * 
 * Note that the answer must represent the lexicographically smallest array,
 * not the corresponding string formed from those indices.
 * 
 *
 * Example 1:
 *
 *
 * Input: word1 = "vbcca", word2 = "abc"
 *
 * Output: [0, 1, 2]
 *
 * Explanation:
 *
 * The lexicographically smallest valid sequence of indices is [0, 1, 2]:
 *
 *
 * Change word1[0] to 'a'.
 * word1[1] is already 'b'.
 * word1[2] is already 'c'.
 *
 *
 *
 * Example 2:
 *
 *
 * Input: word1 = "bacdc", word2 = "abc"
 *
 * Output: [1, 2, 4]
 *
 * Explanation:
 *
 * word1[1] is already 'a'.
 * Change word1[2] to 'b'.
 * word1[4] is already 'c'.
 *
 *
 *
 * Example 3:
 *
 *
 * Input: word1 = "aaaaaa", word2 = "aaabc"
 *
 * Output: []
 *
 * Explanation: There is no valid sequence of indices.
 *
 *
 * Example 4:
 *
 *
 * Input: word1 = "abc", word2 = "ab"
 *
 * Output: [0, 1]
 *
 *
 * Constraints:
 *
 *
 * 1 <= word2.length < word1.length <= 3 * 10^5
 * word1 and word2 consist only of lowercase English letters.
 *
 *
 */
package p3302
// @lc code=start
class Solution {
    fun validSequence(word1: String, word2: String): IntArray {
        val n = word1.length
        val m = word2.length
        val suffix = IntArray(n + 1) { m }
        var target = m - 1

        for (i in n - 1 downTo 0) {
            if (target >= 0 && word1[i] == word2[target]) {
                target--
            }
            suffix[i] = target + 1
        }

        val result = IntArray(m)
        var matched = 0
        var changed = false

        for (i in 0 until n) {
            if (matched == m) {
                break
            }

            if (word1[i] == word2[matched]) {
                result[matched++] = i
            } else if (!changed && suffix[i + 1] <= matched + 1) {
                result[matched++] = i
                changed = true
            }
        }

        return if (matched == m) result else intArrayOf()
    }
}
// @lc code=end
