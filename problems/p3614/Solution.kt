package p3614

/*
 * @lc app=leetcode id=3614 lang=kotlin
 *
 * [3614] Process String with Special Operations II
 */

// @lc code=start
class Solution {
    fun processStr(s: String, k: Long): Char {
        var charAt: (Long) -> Char = { '.' }
        var length = 0L

        for (cmdChar in s) {
            when (cmdChar) {
                '#' -> {
                    val prevCharAt = charAt
                    val prevLength = length
                    charAt = { index -> prevCharAt(index % prevLength) }
                    length *= 2
                }
                '%' -> {
                    val prevCharAt = charAt
                    val prevLength = length
                    charAt = { index -> prevCharAt(prevLength - 1 - index) }
                }
                '*' -> if (length > 0) {
                    length--
                }
                else -> {
                    val prevCharAt = charAt
                    val prevLength = length
                    charAt = { index ->
                        if (index == prevLength) cmdChar else prevCharAt(index)
                    }
                    length++
                }
            }
        }

        return if (k < length) charAt(k) else '.'
    }
}
// @lc code=end
