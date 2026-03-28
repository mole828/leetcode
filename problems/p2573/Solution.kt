package problems.p2573
/*
 * @lc app=leetcode id=2573 lang=kotlin
 *
 * [2573] Find the String with LCP
 */
// @lc code=start
class Solution {
    fun findTheString(lcp: Array<IntArray>): String {
        val n = lcp.size
        val s = CharArray(n)
        var i = 0

        for (c in 'a'..'z') {
            for (j in i until n) {
                if (lcp[i][j] > 0) s[j] = c
            }
            while (i < n && s[i] != '\u0000') i++
            if (i == n) break
        }

        if (i < n) return ""

        fun calc(i: Int, j: Int): Int =
            if (s[i] != s[j]) 0
            else if (i == n - 1 || j == n - 1) 1
            else lcp[i + 1][j + 1] + 1

        for (i in n - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                if (lcp[i][j] != calc(i, j)) return ""
            }
        }

        return String(s)
    }
}

// @lc code=end

