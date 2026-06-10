package p3691

import java.util.PriorityQueue

/*
 * @lc app=leetcode id=3691 lang=kotlin
 *
 * [3691] Maximum Total Subarray Value II
 */

// @lc code=start
class Solution {
    fun maxTotalValue(nums: IntArray, k: Int): Long {
        val n = nums.size
        val log = IntArray(n + 1)
        for (i in 2..n) log[i] = log[i / 2] + 1

        val levels = log[n] + 1
        val maxSt = Array(levels) { IntArray(n) }
        val minSt = Array(levels) { IntArray(n) }
        nums.copyInto(maxSt[0])
        nums.copyInto(minSt[0])

        for (p in 1 until levels) {
            val half = 1 shl (p - 1)
            for (i in 0..n - (1 shl p)) {
                maxSt[p][i] = maxOf(maxSt[p - 1][i], maxSt[p - 1][i + half])
                minSt[p][i] = minOf(minSt[p - 1][i], minSt[p - 1][i + half])
            }
        }

        fun value(l: Int, r: Int): Long {
            val p = log[r - l + 1]
            val len = 1 shl p
            val mx = maxOf(maxSt[p][l], maxSt[p][r - len + 1])
            val mn = minOf(minSt[p][l], minSt[p][r - len + 1])
            return mx.toLong() - mn
        }

        data class Node(val v: Long, val l: Int, val r: Int)

        val pq = PriorityQueue<Node> { a, b -> b.v.compareTo(a.v) }
        for (l in 0 until n) pq += Node(value(l, n - 1), l, n - 1)

        var ans = 0L
        repeat(k) {
            val cur = pq.poll()
            ans += cur.v
            if (cur.r > cur.l) pq += Node(value(cur.l, cur.r - 1), cur.l, cur.r - 1)
        }
        return ans
    }
}
// @lc code=end
