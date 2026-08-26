package p2904

/*
 * @lc app=leetcode id=2904 lang=kotlin
 *
 * [2904] Shortest and Lexicographically Smallest Beautiful String
 */

// @lc code=start
class Solution {
    fun shortestBeautifulSubstring(s: String, k: Int): String {
        var right = 0
        var left = 0
        var count1 = 0
        val set = mutableSetOf<String>()
        while (right < s.length) {
            val char = s[right]
            if (char == '1') count1++
            while (count1 > k) {
                if (s[left] == '1') count1--
                left++
            }
            if (count1 == k) {
                while (left < right && s[left] != '1') {
                    left++
                }
                
                val substring = s.substring(left, right + 1)
                println("$left, $right, $substring")
                set.add(substring)
            }
            right++
        }
        println(set)
        return set.minWithOrNull(
            compareBy<String> { it.length }.thenBy { it }
        ) ?: ""
    }
}
// @lc code=end

