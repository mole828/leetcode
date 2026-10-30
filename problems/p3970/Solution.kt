package p3970

import java.util.PriorityQueue

/*
 * @lc app=leetcode id=3970 lang=kotlin
 *
 * [3970] Shortest Path With At Most K Consecutive Identical Characters
 *
 * https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/description/
 *
 * algorithms
 * Medium (45.31%)
 * Likes:    105
 * Dislikes: 6
 * Total Accepted:    21.7K
 * Total Submissions: 46.9K
 * Testcase Example:  '3\n[[0,1,1],[1,2,1],[0,2,3]]\n"aab"\n1'
 *
 * You are given an integer n representing the number of nodes in a directed
 * weighted graph, numbered from 0 to n - 1. This is represented by a 2D
 * integer array edges, where edges[i] = [ui, vi, wi] represents a directed
 * edge from node ui to node vi with weight wi.
 * 
 * You are also given a string labels of length n, where labels[i] is the
 * character assigned to node i, and an integer k.
 * 
 * Return the minimum total edge weight of a path from node 0 to node n - 1
 * such that the concatenation of the labels of the nodes along the path
 * contains at most k consecutive identical characters. If no valid path
 * exists, return -1.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1
 * 
 * Output: 3
 * 
 * Explanation:
 * 
 * The optimal valid path from node 0 to node 2 is as follows:
 * 
 * 
 * Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.
 * 
 * The corresponding concatenation of labels is "ab", which satisfies at most k
 * = 1 consecutive identical characters. Thus, the answer is 3.
 * 
 * Example 2:
 * 
 * 
 * Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * The optimal valid path from node 0 to node 2 is as follows:
 * 
 * 
 * Use edges[0] = [0, 1, 1] to reach node 1 with weight wi = 1.
 * Use edges[1] = [1, 2, 1] to reach node 2 with weight wi = 1.
 * 
 * The corresponding concatenation of labels is "aab", which satisfies at most
 * k = 2 consecutive identical characters. Thus, the answer is 2.
 * 
 * Example 3:
 * 
 * 
 * Input: n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2
 * 
 * Output: -1
 * 
 * Explanation:
 * 
 * There is no valid path from node 0 to node 2 that satisfies at most k = 2
 * consecutive identical characters. Thus, the answer is -1.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n == labels.length <= 5 * 10^4
 * 0 <= edges.length <= 5 * 10^4
 * edges[i] == [ui, vi, wi]
 * 0 <= ui, vi <= n - 1
 * ui != vi
 * 1 <= wi <= 10^4
 * labels consists of lowercase English letters
 * 1 <= k <= 50
 * 
 * 
 */

// @lc code=start
class Solution {
    private data class State(val node: Int, val k: Int, val weight: Int)
    private data class Edge(val to: Int, val weight: Int)

    fun shortestPath(n: Int, edges: Array<IntArray>, labels: String, k: Int): Int {
        val graph = Array(n) { mutableListOf<Edge>() }
        for ((u, v, w) in edges) {
            graph[u].add(Edge(v, w))
        }
        return search(n, labels, k) { node -> graph[node] }
    }

    @Deprecated(
        "memory limit"
    )
    fun shortestPathReference(n: Int, edges: Array<IntArray>, labels: String, k: Int): Int {
        val maxInt = 1_000_000_000
        val graph = Array(n) { IntArray(n) { maxInt } }
        edges.forEach { edge ->
            val (u, v, w) = edge
            graph[u][v] = minOf(graph[u][v], w)
        }
        return search(n, labels, k) { node ->
            graph[node].withIndex()
                .filter { it.value != maxInt }
                .map { Edge(it.index, it.value) }
        }
    }

    private fun search(
        n: Int,
        labels: String,
        k: Int,
        neighbors: (Int) -> List<Edge>,
    ): Int {
        val que = PriorityQueue<State>(compareBy { it.weight })
        que.add(State(node = 0, k = 1, weight = 0))
        val visited = mutableSetOf<Pair<Int, Int>>()
        while (que.isNotEmpty()) {
            val state = que.poll()
            // 同一节点、同一连续字符数，第一次出队时的权重最小。
            if (!visited.add(state.node to state.k)) continue
            if (state.node == n - 1) return state.weight

            val thisNodeChar = labels[state.node]
            for (edge in neighbors(state.node)) {
                val newK = if (thisNodeChar == labels[edge.to]) state.k + 1 else 1
                if (newK > k) continue
                que.add(
                    State(node = edge.to, k = newK, weight = state.weight + edge.weight)
                )
            }
        }
        return -1
    }
}
// @lc code=end

