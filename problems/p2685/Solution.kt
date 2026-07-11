package p2685
/*
 * @lc app=leetcode id=2685 lang=kotlin
 *
 * [2685] Count the Number of Complete Components
 */
// @lc code=start
class Solution {
    fun countCompleteComponents(n: Int, edges: Array<IntArray>): Int {
        val graph = Array(n) { mutableListOf<Int>() }
        edges.forEach { (u, v) ->
            graph[u] += v
            graph[v] += u
        }

        val visited = BooleanArray(n)

        return (0 until n).count { start ->
            if (visited[start]) return@count false

            var vertexCount = 0
            var degreeSum = 0

            fun dfs(u: Int) {
                visited[u] = true
                vertexCount++
                degreeSum += graph[u].size

                graph[u].forEach { v ->
                    if (!visited[v]) dfs(v)
                }
            }

            dfs(start)
            degreeSum == vertexCount * (vertexCount - 1)
        }
    }
}
// @lc code=end
