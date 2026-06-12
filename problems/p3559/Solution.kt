package p3559

/*
 * @lc app=leetcode id=3559 lang=kotlin
 *
 * [3559] Number of Ways to Assign Edge Weights II
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
    fun assignEdgeWeights(edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val n = edges.size + 1
        val graph = Array(n + 1) { mutableListOf<Int>() }
        edges.forEach { (a, b) ->
            graph[a].add(b)
            graph[b].add(a)
        }

        var log = 1
        while ((1 shl log) <= n) log++
        val up = Array(log) { IntArray(n + 1) }
        val depth = IntArray(n + 1)
        val queue = java.util.ArrayDeque<Int>()
        queue.add(1)

        while (!queue.isEmpty()) {
            val u = queue.removeFirst()
            for (v in graph[u]) {
                if (v != up[0][u]) {
                    up[0][v] = u
                    depth[v] = depth[u] + 1
                    queue.add(v)
                }
            }
        }

        for (i in 1 until log) {
            for (node in 1..n) {
                up[i][node] = up[i - 1][up[i - 1][node]]
            }
        }

        fun lca(a: Int, b: Int): Int {
            var u = a
            var v = b
            if (depth[u] < depth[v]) {
                val temp = u
                u = v
                v = temp
            }

            var diff = depth[u] - depth[v]
            var bit = 0
            while (diff > 0) {
                if ((diff and 1) == 1) {
                    u = up[bit][u]
                }
                diff = diff shr 1
                bit++
            }

            if (u == v) return u

            for (i in log - 1 downTo 0) {
                if (up[i][u] != up[i][v]) {
                    u = up[i][u]
                    v = up[i][v]
                }
            }
            return up[0][u]
        }

        return queries.map { (a, b) ->
            val distance = depth[a] + depth[b] - 2 * depth[lca(a, b)]
            if (distance == 0) 0 else modPow(2L, (distance - 1).toLong(), mod.toLong()).toInt()
        }.toIntArray()
    }
}
// @lc code=end
