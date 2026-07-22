package p3501

/*
 * @lc app=leetcode id=3501 lang=kotlin
 *
 * [3501] Maximize Active Section with Trade II
 */

// @lc code=start
class Solution {
    fun maxActiveSectionsAfterTrade(s: String, queries: Array<IntArray>): List<Int> {
        val runs = buildRuns(s)
        val runAt = IntArray(s.length)
        runs.forEachIndexed { index, run ->
            for (position in run.start..run.end) runAt[position] = index
        }

        val gain = IntArray(runs.size) { index ->
            if (runs[index].bit == '1' && index in 1..<runs.lastIndex) {
                runs[index - 1].length + runs[index + 1].length
            } else {
                0
            }
        }
        val rangeMax = RangeMax(gain)
        val activeSections = s.count { it == '1' }

        return queries.map { (left, right) ->
            val firstRun = runAt[left]
            val lastRun = runAt[right]
            val firstOneRun = firstRun + if (runs[firstRun].bit == '0') 1 else 2
            val lastOneRun = lastRun - if (runs[lastRun].bit == '0') 1 else 2

            val extra = when {
                firstOneRun > lastOneRun -> 0
                firstOneRun == lastOneRun -> gainWithinQuery(
                    runs,
                    firstOneRun,
                    left,
                    right,
                )
                else -> maxOf(
                    gainWithinQuery(runs, firstOneRun, left, right),
                    rangeMax.query(firstOneRun + 1, lastOneRun - 1),
                    gainWithinQuery(runs, lastOneRun, left, right),
                )
            }
            activeSections + extra
        }
    }

    private fun buildRuns(s: String): List<Run> = buildList {
        var start = 0
        for (end in 1..s.length) {
            if (end == s.length || s[end] != s[start]) {
                add(Run(s[start], start, end - 1))
                start = end
            }
        }
    }

    private fun gainWithinQuery(runs: List<Run>, oneRun: Int, left: Int, right: Int): Int {
        val one = runs[oneRun]
        val leftZeros = one.start - maxOf(left, runs[oneRun - 1].start)
        val rightZeros = minOf(right, runs[oneRun + 1].end) - one.end
        return leftZeros + rightZeros
    }

    private data class Run(val bit: Char, val start: Int, val end: Int) {
        val length: Int get() = end - start + 1
    }

    private class RangeMax(values: IntArray) {
        private val leafCount = values.size.takeHighestOneBit().let {
            if (it == values.size) it else it shl 1
        }
        private val tree = IntArray(leafCount * 2)

        init {
            values.copyInto(tree, destinationOffset = leafCount)
            for (node in leafCount - 1 downTo 1) {
                tree[node] = maxOf(tree[node * 2], tree[node * 2 + 1])
            }
        }

        fun query(from: Int, to: Int): Int {
            if (from > to) return 0

            var left = from + leafCount
            var right = to + leafCount
            var result = 0
            while (left <= right) {
                if (left % 2 == 1) result = maxOf(result, tree[left++])
                if (right % 2 == 0) result = maxOf(result, tree[right--])
                left /= 2
                right /= 2
            }
            return result
        }
    }
}
// @lc code=end
