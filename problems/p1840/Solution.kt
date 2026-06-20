package p1840
/*
 * @lc app=leetcode id=1840 lang=kotlin
 *
 * [1840] Maximum Building Height
 */
// @lc code=start
class Solution {
    fun maxBuilding(n: Int, restrictions: Array<IntArray>): Int {
        val limits = ArrayList<IntArray>()
        limits.add(intArrayOf(1, 0))
        for (restriction in restrictions) {
            limits.add(intArrayOf(restriction[0], restriction[1]))
        }
        limits.add(intArrayOf(n, n - 1))
        limits.sortBy { it[0] }

        for (i in 1 until limits.size) {
            val distance = limits[i][0] - limits[i - 1][0]
            limits[i][1] = minOf(limits[i][1], limits[i - 1][1] + distance)
        }

        for (i in limits.size - 2 downTo 0) {
            val distance = limits[i + 1][0] - limits[i][0]
            limits[i][1] = minOf(limits[i][1], limits[i + 1][1] + distance)
        }

        var answer = 0
        for (i in 1 until limits.size) {
            val distance = limits[i][0] - limits[i - 1][0]
            val lower = minOf(limits[i - 1][1], limits[i][1])
            val higher = maxOf(limits[i - 1][1], limits[i][1])
            answer = maxOf(answer, higher + (distance - (higher - lower)) / 2)
        }
        return answer
    }
}
// @lc code=end
