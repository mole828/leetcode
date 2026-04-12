package problems.p1320

import kotlin.math.abs

/*
 * @lc app=leetcode id=1320 lang=kotlin
 *
 * [1320] Minimum Distance to Type a Word Using Two Fingers
 */
// @lc code=start
fun <P1, P2, P3, R> ((P1, P2, P3) -> R).memoize(): (P1, P2, P3) -> R {
    val cache = mutableMapOf<Triple<P1, P2, P3>, R>()
    return { p1, p2, p3 ->
        cache.getOrPut(Triple(p1, p2, p3)) { this(p1, p2, p3) }
    }
}
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
        lateinit var dfs: (Int, Char, Char) -> Int
    
        dfs = { index: Int, c1: Char, c2: Char ->
            if (index == word.length) 0
            else {
                val c = word[index]
                val res1 = getDist(c1, c) + dfs(index + 1, c, c2)
                val res2 = getDist(c2, c) + dfs(index + 1, c1, c)
                res1.coerceAtMost(res2)
            }
        }.memoize()

        return ('A'..'Z').minOf { dfs(1, word[0], it) } 
    }
}
// @lc code=end

