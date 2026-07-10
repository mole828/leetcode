package p3534

/*
 * @lc app=leetcode id=3534 lang=kotlin
 *
 * [3534] Path Existence Queries in a Graph II
 */

// @lc code=start
class Solution {
    // TODO
    fun pathExistenceQueries(
        n: Int,
        nums: IntArray,
        maxDiff: Int,
        queries: Array<IntArray>,
    ): IntArray {
        val order = nums.indices.sortedBy { nums[it] }
        val rank = IntArray(n)
        val sortedNums = IntArray(n)

        order.forEachIndexed { sortedIndex, originalIndex ->
            rank[originalIndex] = sortedIndex
            sortedNums[sortedIndex] = nums[originalIndex]
        }

        // jump[k][i]: 从排序位置 i 出发，走至多 2^k 条边能到达的最右位置。
        val levels = Int.SIZE_BITS - Integer.numberOfLeadingZeros(n)
        val jump = Array(levels) { IntArray(n) }

        var right = 0
        for (left in 0 until n) {
            right = maxOf(right, left)
            while (
                right + 1 < n &&
                sortedNums[right + 1].toLong() - sortedNums[left] <= maxDiff.toLong()
            ) {
                right++
            }
            jump[0][left] = right
        }

        for (level in 1 until levels) {
            for (i in 0 until n) {
                jump[level][i] = jump[level - 1][jump[level - 1][i]]
            }
        }

        return IntArray(queries.size) { queryIndex ->
            val (u, v) = queries[queryIndex]
            val start = minOf(rank[u], rank[v])
            val target = maxOf(rank[u], rank[v])

            minimumSteps(start, target, jump)
        }
    }

    private fun minimumSteps(start: Int, target: Int, jump: Array<IntArray>): Int {
        if (start == target) return 0

        var current = start
        var steps = 0

        for (level in jump.lastIndex downTo 0) {
            val next = jump[level][current]
            if (next in (current + 1) until target) {
                current = next
                steps += 1 shl level
            }
        }

        return if (jump[0][current] >= target) steps + 1 else -1
    }
}
// @lc code=end
