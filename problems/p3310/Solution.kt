package p3310

/*
 * @lc app=leetcode id=3310 lang=kotlin
 *
 * [3310] Remove Methods From Project
 */

// @lc code=start
class Solution {
    fun remainingMethods(n: Int, k: Int, invocations: Array<IntArray>): List<Int> {
        val graph = Array(n + 1) { mutableListOf<Int>() }
        invocations.forEach { (from, to) ->
            graph[from].add(to)
        }
        val suspicious = mutableSetOf<Int>()
        fun dfs(node: Int) {
            if (node in suspicious) return
            suspicious.add(node)
            graph[node].forEach { dfs(it) }
        }
        dfs(k)
        invocations.forEach { (from, to) ->
            if (suspicious.contains(from).not() and suspicious.contains(to)) {
                return (0..<n).toList()
            }
        }
        return (0..<n).filter { it !in suspicious }
    }
}
// @lc code=end

