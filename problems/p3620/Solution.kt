package p3620

/*
 * @lc app=leetcode id=3620 lang=kotlin
 *
 * [3620] Network Recovery Pathways
 */

// @lc code=start
class Solution {
    fun findMaxPathScore(edges: Array<IntArray>, online: BooleanArray, k: Long): Int {
        val n = online.size; val graph = Array(n) { mutableListOf<Pair<Int, Int>>() }
        var maxWeight = -1
        for ((from, to, weight) in edges) if (online[from] && online[to]) {
            graph[from].add(to to weight)
            if (from == 0) maxWeight = maxOf(maxWeight, weight)
        }

        fun check(lower: Int): Boolean {
            val memo = LongArray(n) { -1 }
            fun dfs(node: Int): Long {
                if (node == n - 1) return 0
                if (memo[node] != -1L) return memo[node]
                var result = k + 1
                for ((next, weight) in graph[node]) if (weight >= lower) result = minOf(result, dfs(next) + weight)
                return result.also { memo[node] = it }
            }
            return dfs(0) <= k
        }

        var left = -1; var right = maxWeight + 1
        while (left + 1 < right) {
            val mid = (left + right) / 2; if (check(mid)) left = mid else right = mid
        }
        return left
    }
}
// @lc code=end
