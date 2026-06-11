package p3558

/*
 * @lc app=leetcode id=3558 lang=kotlin
 *
 * [3558] Number of Ways to Assign Edge Weights I
 */

// @lc code=start
class Solution {
    val mod = 1_000_000_007
    companion object {
        fun modPow(a: Long, b: Long, mod: Long): Long {
            require(mod > 0)
            require(b >= 0)

            var base = ((a % mod) + mod) % mod
            var exp = b
            var result = 1L % mod

            while (exp > 0) {
                if ((exp and 1L) != 0L) {
                    result = result * base % mod
                }
                base = base * base % mod
                exp = exp shr 1
            }

            return result
        }
    }
    fun assignEdgeWeights(edges: Array<IntArray>): Int {
        val n = edges.size + 1
        val graph = Array(n + 1) { mutableListOf<Int>() }
        edges.forEach { (a, b) ->
            graph[a].add(b)
            graph[b].add(a)
        }
        fun dfs(x: Int, parent: Int): Int {
            var d = 0
            for (y in graph[x]) {
                if (y != parent) {
                    d = maxOf(d, dfs(y, x) + 1)
                }
            }
            return d
        }
        val k = dfs(1, 0)
        return modPow(2L, (k-1).toLong(), mod.toLong()).toInt()
    }
}
// @lc code=end

