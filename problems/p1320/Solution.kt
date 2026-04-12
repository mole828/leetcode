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
        fun dfs(index: Int, c1: Char, c2: Char): Int { 
            if (index == word.length) return 0
            val key = Triple(index, c1, c2)
            cache[key]?.let { return it }
            val c = word[index]
            val dist1 = getDist(c1, c) + dfs(index + 1, c, c2)
            val dist2 = getDist(c2, c) + dfs(index + 1, c1, c)
            val res = dist1.coerceAtMost(dist2)
            cache[key] = res
            return res
        }
        val firstChar = word[0]
        return ('A'..'Z').minOf {
            dfs(1, firstChar, it)
        }
    }

}
// @lc code=end

