package problems.p3474
/*
 * @lc app=leetcode id=3474 lang=kotlin
 *
 * [3474] Lexicographically Smallest Generated String
 */

// @lc code=start
class Solution {
    fun generateString(s: String, t: String): String {
        val (n, m) = s.length to t.length
        val totalLen = n + m - 1
        val ans = CharArray(totalLen) { '?' }
        val isFixed = BooleanArray(totalLen)

        // 1. 处理 'T'：使用 repeat 和 lambda 让逻辑更紧凑
        for (i in s.indices) {
            if (s[i] == 'T') {
                repeat(m) { j ->
                    val pos = i + j
                    if (ans[pos] != '?' && ans[pos] != t[j]) return ""
                    ans[pos] = t[j]
                    isFixed[pos] = true
                }
            }
        }

        // 2. 默认填充 'a'
        for (i in ans.indices) {
            if (ans[i] == '?') ans[i] = 'a'
        }

        // 3. 处理 'F'：利用 indices 和扩展思想
        for (i in s.indices) {
            if (s[i] == 'F') {
                // 检查子串是否完全匹配 t
                val isMatch = (0 until m).all { j -> ans[i + j] == t[j] }

                if (isMatch) {
                    // 寻找该区间内最后一个非固定的位置
                    val posToChange = (m - 1 downTo 0)
                        .map { i + it }
                        .firstOrNull { !isFixed[it] } 
                        ?: return "" // 如果全部被固定且匹配，则无解

                    ans[posToChange] = 'b'
                }
            }
        }

        return String(ans)
    }
}
// @lc code=end

