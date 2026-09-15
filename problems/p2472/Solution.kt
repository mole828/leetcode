package p2472
/*
 * @lc app=leetcode id=2472 lang=kotlin
 *
 * [2472] Maximum Number of Non-overlapping Palindrome Substrings
 */
// @lc code=start
class Solution {
    fun maxPalindromes(s: String, k: Int): Int {
        fun isPalindrome(start: Int, end: Int): Boolean {
            var left = start
            var right = end
            while (left < right) {
                if (s[left++] != s[right--]) return false
            }
            return true
        }

        var count = 0
        var start = 0
        for (end in s.indices) {
            val shortStart = end - k + 1
            val longStart = end - k
            if ((shortStart >= start && isPalindrome(shortStart, end)) ||
                (longStart >= start && isPalindrome(longStart, end))
            ) {
                count++
                start = end + 1
            }
        }
        return count
    }
}
// @lc code=end

fun main() {
    val solution = Solution()
    val examples = listOf(
        Triple("abaccdbbd", 3, 2), // 可以选 "aba" 和 "dbbd"。
        Triple("adbcda", 2, 0),   // 没有长度至少为 2 的回文。
        Triple("aaaaa", 2, 2),    // 可以选两个不重叠的 "aa"。
        Triple("abba", 3, 1),     // 回文长度可以大于 k。
        Triple("abc", 1, 3),      // 每个单字符都是回文。
        Triple("aba", 4, 0)       // k 大于字符串长度。
    )
    for ((s, k, expected) in examples) {
        val actual = solution.maxPalindromes(s, k)
        println("s=\"$s\", k=$k -> $actual（预期：$expected）")
        check(actual == expected)
    }
}
