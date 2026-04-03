package problems.p3661
/*
 * @lc app=leetcode id=3661 lang=kotlin
 *
 * [3661] Maximum Walls Destroyed by Robots
 */

// @lc code=start
class Solution {
    fun maxWalls(robots: IntArray, distance: IntArray, walls: IntArray): Int {
        val n = robots.size

        // 构造 a
        val a = mutableListOf<Pair<Int, Int>>()
        a.add(0 to 0)
        a.addAll(robots.zip(distance).sortedBy { it.first })
        a.add(Int.MAX_VALUE to 0)

        walls.sort()

        val memo = mutableMapOf<Pair<Int, Int>, Int>()

        fun dfs(i: Int, j: Int): Int {
            if (i == 0) return 0

            val key = i to j
            memo[key]?.let { return it }

            val (x, d) = a[i]

            // ---- 左射 ----
            val leftX = maxOf(x - d, a[i - 1].first + 1)
            val left = lowerBound(walls, leftX)
            val curL = upperBound(walls, x)
            val resLeft = dfs(i - 1, 0) + (curL - left)

            // ---- 右射 ----
            val (x2, d2) = a[i + 1]
            val newX2 = if (j == 0) x2 - d2 else x2

            val rightX = minOf(x + d, newX2 - 1)
            val right = upperBound(walls, rightX)
            val curR = lowerBound(walls, x)
            val resRight = dfs(i - 1, 1) + (right - curR)

            val res = maxOf(resLeft, resRight)
            memo[key] = res
            return res
        }

        return dfs(n, 1)
    }

    // Kotlin 手写 lowerBound
    private fun lowerBound(arr: IntArray, target: Int): Int {
        var l = 0
        var r = arr.size
        while (l < r) {
            val mid = (l + r) ushr 1
            if (arr[mid] < target) l = mid + 1 else r = mid
        }
        return l
    }

    // Kotlin 手写 upperBound
    private fun upperBound(arr: IntArray, target: Int): Int {
        var l = 0
        var r = arr.size
        while (l < r) {
            val mid = (l + r) ushr 1
            if (arr[mid] <= target) l = mid + 1 else r = mid
        }
        return l
    }
}
// @lc code=end

