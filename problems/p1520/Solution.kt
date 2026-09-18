package p1520


/*
 * @lc app=leetcode id=1520 lang=kotlin
 *
 * [1520] Maximum Number of Non-Overlapping Substrings
 */

// TODO: 图的部分

// @lc code=start
class Solution {
    // 找到第一个 >= target 的位置；不存在时返回 positions.size。
    private fun bisectLeft(positions: List<Int>, target: Int): Int {
        var left = 0
        var right = positions.size
        while (left < right) {
            val mid = left + (right - left) / 2
            if (positions[mid] < target) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }

    fun maxNumOfSubstrings(s: String): List<String> {
        val pos = Array(26) { mutableListOf<Int>() }
        for (i in s.indices) {
            pos[s[i] - 'a'].add(i)
        }

        val graph = Array(26) { mutableListOf<Int>() }
        for (i in 0 until 26) {
            if (pos[i].isEmpty()) continue
            val left = pos[i].first()
            val right = pos[i].last()
            for (j in 0 until 26) {
                if (j == i || pos[j].isEmpty()) continue
                val q = pos[j]
                val k = bisectLeft(q, left)
                if (k < q.size && q[k] <= right) {
                    graph[i].add(j)
                }
            }
        }

        val intervals = mutableListOf<Pair<Int, Int>>()
        for (i in 0 until 26) {
            if (pos[i].isEmpty()) continue

            val vis = BooleanArray(26)
            var left = s.length
            var right = -1

            fun dfs(x: Int) {
                vis[x] = true
                // 所有递归调用共同扩展本轮的 left、right。
                left = minOf(left, pos[x].first())
                right = maxOf(right, pos[x].last())
                for (y in graph[x]) {
                    if (!vis[y]) dfs(y)
                }
            }

            dfs(i)
            intervals.add(left to right)
        }

        intervals.sortWith(compareBy<Pair<Int, Int>> { it.second }.thenByDescending { it.first })
        val ans = mutableListOf<String>()
        var preRight = -1
        for ((left, right) in intervals) {
            if (left > preRight) {
                ans.add(s.substring(left, right + 1))
                preRight = right
            }
        }
        return ans
    }
}
// @lc code=end
