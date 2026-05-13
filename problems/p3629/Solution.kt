package p3629
/*
 * @lc app=leetcode id=3629 lang=kotlin
 *
 * [3629] Minimum Jumps to Reach End via Prime Teleportation
 */
// @lc code=start
class Solution {
    fun minJumps(nums: IntArray): Int {
        val n = nums.size
        val groups = mutableMapOf<Int, MutableList<Int>>().apply {
            nums.indices.forEach { i ->
                PRIME_FACTORS[nums[i]].forEach { p ->
                    getOrPut(p) { mutableListOf() }.add(i)
                }
            }
        }

        val vis = BooleanArray(n)
        vis[0] = true
        val q = IntArray(n)
        var left = 0
        var right = 0
        q[right++] = 0

        var step = 0
        while (left < right) {
            repeat(right - left) {
                val i = q[left++]
                if (i == n - 1) return step

                val next = groups.getOrPut(nums[i]) { mutableListOf() }
                next += i + 1
                if (i > 0) next += i - 1
                next.forEach { j ->
                    if (!vis[j]) {
                        vis[j] = true
                        q[right++] = j
                    }
                }
                next.clear()
            }
            step++
        }
        return -1
    }

    companion object {
        private const val MX = 1_000_001
        private val PRIME_FACTORS = Array(MX) { mutableListOf<Int>() }.also { factors ->
            for (i in 2 until MX) {
                if (factors[i].isEmpty()) {
                    for (j in i until MX step i) {
                        factors[j].add(i)
                    }
                }
            }
        }
    }
}
// @lc code=end
