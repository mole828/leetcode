/*
 * @lc app=leetcode id=3518 lang=kotlin
 *
 * [3518] Smallest Palindromic Rearrangement II
 *
 * https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/description/
 *
 * algorithms
 * Hard (14.47%)
 * Likes:    170
 * Dislikes: 16
 * Total Accepted:    25.5K
 * Total Submissions: 78K
 * Testcase Example:  '"abba"\n2'
 *
 * You are given a palindromic string s and an integer k.
 * 
 * Return the k-th lexicographically smallest palindromic permutation of s. If
 * there are fewer than k distinct palindromic permutations, return an empty
 * string.
 * 
 * Note: Different rearrangements that yield the same palindromic string are
 * considered identical and are counted once.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "abba", k = 2
 * 
 * Output: "baab"
 * 
 * Explanation:
 * 
 * 
 * The two distinct palindromic rearrangements of "abba" are "abba" and
 * "baab".
 * Lexicographically, "abba" comes before "baab". Since k = 2, the output is
 * "baab".
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "aa", k = 2
 * 
 * Output: ""
 * 
 * Explanation:
 * 
 * 
 * There is only one palindromic rearrangement: "aa".
 * The output is an empty string since k = 2 exceeds the number of possible
 * rearrangements.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "bacab", k = 1
 * 
 * Output: "abcba"
 * 
 * Explanation:
 * 
 * 
 * The two distinct palindromic rearrangements of "bacab" are "abcba" and
 * "bacab".
 * Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is
 * "abcba".
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^4
 * s consists of lowercase English letters.
 * s is guaranteed to be palindromic.
 * 1 <= k <= 10^6
 * 
 * 
 */
package p3518
// @lc code=start
class Solution {
    fun smallestPalindrome(s: String, k: Int): String {
        val n = s.length
        val m = n / 2
        var k = k
        val count = IntArray(26)
        // 回文串的右半部分由左半部分唯一确定，因此只排列左半部分。
        for (i in 0 until m) {
            count[s[i] - 'a']++
        }
        
        fun comb(n: Int, m: Int): Int {
            val m = minOf(m, n - m)
            var res = 1L
            for (i in 1..m) {
                // 必须先乘再除；先除会丢失不能整除的部分。
                res = res * (n + 1 - i) / i
                if (res >= k.toLong()) return k
            }
            return res.toInt()
        }
        
        fun perm(size: Int): Int {
            var res = 1L
            var size = size
            count.forEach { c ->
                if (c > 0) {
                    res *= comb(size, c).toLong()
                    if (res >= k.toLong()) return k
                }
                size -= c
            }
            return res.toInt()
        }
        
        if (perm(m) < k) return ""
        
        val left = CharArray(m)
        for (i in 0 until m) {
            for (j in 0 until 26) {
                if (count[j] <= 0) continue
                count[j]--
                val p = perm(m - i - 1)
                if (p >= k) {
                    left[i] = 'a' + j
                    break
                }
                k -= p
                count[j]++
            }
        }
        
        val leftString = left.concatToString()
        var ans = leftString
        if (n % 2 == 1) {
            ans += s[n / 2]
        }
        ans += leftString.reversed()
        return ans
    }
}
// @lc code=end
