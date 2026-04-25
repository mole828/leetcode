package problems.p3464
/*
 * @lc app=leetcode id=3464 lang=kotlin
 *
 * [3464] Maximize the Distance Between Points on a Square
 */
// @lc code=start
class Solution {
    fun maxDistance(side: Int, points: Array<IntArray>, k: Int): Int {
        val sideL = side.toLong()
        val perimeter = sideL * 4
        val mapped = points.map { (x, y) ->
            when {
                x == 0 -> y.toLong()
                y == side -> sideL + x
                x == side -> sideL * 3 - y
                else -> perimeter - x
            }
        }.sorted()

        fun lowerBound(target: Long) =
            mapped.binarySearch(target).let { if (it >= 0) it else -it - 1 }

        fun check(dist: Long): Boolean {
            val need = dist + 1

            for (start in mapped) {
                val end = start + perimeter - need
                var cur = start

                for (i in 1 until k) {
                    val next = lowerBound(cur + need)
                    if (next == mapped.size || mapped[next] > end) break
                    cur = mapped[next]
                    if (i == k - 1) return false
                }
            }

            return true
        }

        var left = 0L
        var right = perimeter / k
        while (left < right) {
            val mid = (left + right) / 2
            if (check(mid)) right = mid else left = mid + 1
        }
        return left.toInt()
    }
}
// @lc code=end
