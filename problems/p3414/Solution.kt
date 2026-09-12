package p3414
/*
 * @lc app=leetcode id=3414 lang=kotlin
 *
 * [3414] Maximum Score of Non-overlapping Intervals
 */
// @lc code=start
class Solution {
    private data class State(val weight: Long = 0, val indices: List<Int> = emptyList())

    fun maximumWeight(intervals: List<List<Int>>): IntArray {
        val arr = intervals.withIndex().sortedBy { it.value[1] }
        val bestFirst = compareByDescending<State> { it.weight }.thenComparator { a, b ->
            for (i in 0 until minOf(a.indices.size, b.indices.size)) {
                val cmp = a.indices[i].compareTo(b.indices[i])
                if (cmp != 0) return@thenComparator cmp
            }
            a.indices.size.compareTo(b.indices.size)
        }
        val dp = Array(arr.size + 1) { Array(5) { State() } }

        for ((i, entry) in arr.withIndex()) {
            val (idx, interval) = entry
            val (start, _, weight) = interval
            var left = 0
            var right = i
            while (left < right) {
                val mid = (left + right) ushr 1
                if (arr[mid].value[1] < start) left = mid + 1 else right = mid
            }
            for (j in 1..4) {
                val prev = dp[left][j - 1]
                val take = State(prev.weight + weight, (prev.indices + idx).sorted())
                dp[i + 1][j] = minOf(dp[i][j], take, bestFirst)
            }
        }
        return dp.last()[4].indices.toIntArray()
    }
}
// @lc code=end
