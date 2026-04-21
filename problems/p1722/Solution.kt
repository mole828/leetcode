package problems.p1722

import kotlin.math.absoluteValue

/*
 * @lc app=leetcode id=1722 lang=kotlin
 *
 * [1722] Minimize Hamming Distance After Swap Operations
 */

// @lc code=start
class Solution {
    fun minimumHammingDistance(source: IntArray, target: IntArray, allowedSwaps: Array<IntArray>): Int {
        val n = source.size
        
        val g = Array(n) { mutableListOf<Int>() }.apply {
            allowedSwaps.forEach { (u, v) ->
                this[u].add(v)
                this[v].add(u)
            }
        }

        val vis = BooleanArray(n)
        val diffMap = mutableMapOf<Int, Int>()

        fun dfs(u: Int) {
            vis[u] = true
            // 使用 Kotlin Map 扩展函数：getOrDefault 或 compute
            diffMap[source[u]] = (diffMap[source[u]] ?: 0) + 1
            diffMap[target[u]] = (diffMap[target[u]] ?: 0) - 1
            
            g[u].forEach { v ->
                if (!vis[v]) dfs(v)
            }
        }

        return (0 until n).fold(0) { total, i ->
            if (!vis[i]) {
                diffMap.clear()
                dfs(i)
                total + diffMap.values.sumOf { it.absoluteValue }
            } else {
                total
            }
        } / 2
    }
}
// @lc code=end

