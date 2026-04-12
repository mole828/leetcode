package problems.p1320

import kotlin.math.abs

/*
 * @lc app=leetcode id=1320 lang=kotlin
 *
 * [1320] Minimum Distance to Type a Word Using Two Fingers
 */
// @lc code=start
class Solution {
    val getCoord = { c: Char ->
        val index = c - 'A'
        val row = index / 6
        val col = index % 6
        row to col
    }
    val getDist = { c1: Char, c2: Char ->
        val (r1, c1) = getCoord(c1)
        val (r2, c2) = getCoord(c2)
        abs(r1 - r2) + abs(c1 - c2)
    }
    fun minimumDistance(word: String): Int {
        val cache = mutableMapOf<Triple<Int, Char, Char>, Int>()
        fun dfs(index: Int, c1: Char, c2: Char): Int = cache.getOrPut(Triple(index, c1, c2)) {
            if (index == word.length) return 0
            
            val c = word[index]
            val d1 = getDist(c1, c) + dfs(index + 1, c, c2)
            val d2 = getDist(c2, c) + dfs(index + 1, c1, c)
            
            d1.coerceAtMost(d2)
        }
        return ('A'..'Z').minOf { dfs(1, word[0], it) } 
    }
}
// @lc code=end

