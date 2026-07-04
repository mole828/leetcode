package p2492
/*
 * @lc app=leetcode id=2492 lang=kotlin
 *
 * [2492] Minimum Score of a Path Between Two Cities
 */
// @lc code=start
class Solution {
    data class Edge(
        val to: Int,
        val score: Int
    )

    fun minScore(n: Int, roads: Array<IntArray>): Int {
        val graph = Array(n + 1) { mutableListOf<Edge>() }

        for ((u, v, score) in roads) {
            graph[u].add(Edge(v, score))
            graph[v].add(Edge(u, score))
        }

        val visited = BooleanArray(n + 1)
        val queue = ArrayDeque<Int>()

        queue.addLast(1)
        visited[1] = true

        var answer = Int.MAX_VALUE

        while (queue.isNotEmpty()) {
            val city = queue.removeFirst()

            for (edge in graph[city]) {
                answer = minOf(answer, edge.score)

                if (!visited[edge.to]) {
                    visited[edge.to] = true
                    queue.addLast(edge.to)
                }
            }
        }

        return answer
    }
}
// @lc code=end

