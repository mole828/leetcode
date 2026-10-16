package p2916

/*
 * @lc app=leetcode id=2916 lang=kotlin
 *
 * [2916] Subarrays Distinct Element Sum of Squares II
 *
 * https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/description/
 *
 * algorithms
 * Hard (23.56%)
 * Likes:    185
 * Dislikes: 14
 * Total Accepted:    8.7K
 * Total Submissions: 27.6K
 * Testcase Example:  '[1,2,1]'
 *
 * You are given a 0-indexed integer array nums.
 * 
 * The distinct count of a subarray of nums is defined as:
 * 
 * 
 * Let nums[i..j] be a subarray of nums consisting of all the indices from i to
 * j such that 0 <= i <= j < nums.length. Then the number of distinct values in
 * nums[i..j] is called the distinct count of nums[i..j].
 * 
 * 
 * Return the sum of the squares of distinct counts of all subarrays of nums.
 * 
 * Since the answer may be very large, return it modulo 10^9 + 7.
 * 
 * A subarray is a contiguous non-empty sequence of elements within an
 * array.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,2,1]
 * Output: 15
 * Explanation: Six possible subarrays are:
 * [1]: 1 distinct value
 * [2]: 1 distinct value
 * [1]: 1 distinct value
 * [1,2]: 2 distinct values
 * [2,1]: 2 distinct values
 * [1,2,1]: 2 distinct values
 * The sum of the squares of the distinct counts in all subarrays is equal to
 * 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [2,2]
 * Output: 3
 * Explanation: Three possible subarrays are:
 * [2]: 1 distinct value
 * [2]: 1 distinct value
 * [2,2]: 1 distinct value
 * The sum of the squares of the distinct counts in all subarrays is equal to
 * 1^2 + 1^2 + 1^2 = 3.
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^5
 * 
 * 
 */
// TODO: 线段树
// @lc code=start
class Solution {
    val mod = 1_000_000_007
    fun sumCounts(nums: IntArray): Int {
        // 树维护原来的 distinct 数组，初始全为 0。
        // 处理 right 之前，distinct[left] 是 [left, right - 1] 的不同元素个数。
        val distinct = RangeAddSumTree(nums.size)
        val lastMeet = mutableMapOf<Int, Int>()
        var endingSum = 0L // 所有以当前 right 结尾的子数组，其不同元素个数的平方和
        var ans = 0L

        nums.forEachIndexed { right, num ->
            val previous = lastMeet[num] ?: -1

            // 只有 left 在 [previous + 1, right] 内时，加入 num 才会多一种元素。
            // 先查询这些子数组在变化前的不同元素个数之和。
            val rangeSum = distinct.query(previous + 1, right)

            // 每个受影响的子数组，平方值从 d² 变成 (d + 1)²，增加 2d + 1。
            val increase = 2L * rangeSum + (right - previous)
            endingSum = (endingSum + increase) % mod

            // 再更新这些子数组的不同元素个数，供下一轮使用。
            distinct.add(previous + 1, right, 1L)

            ans = (ans + endingSum) % mod
            lastMeet[num] = right
        }
        return ans.toInt()
    }

    private class RangeAddSumTree(private val size: Int) {
        // 节点表示一个区间，两个孩子分别表示它的左半段和右半段。
        // sum 已包含本节点收到的所有更新；lazy 是尚未传给孩子的加法。
        private val sum = LongArray(size * 4)
        private val lazy = LongArray(size * 4)

        fun query(from: Int, to: Int): Long = query(1, 0, size - 1, from, to)

        fun add(from: Int, to: Int, delta: Long) {
            add(1, 0, size - 1, from, to, delta)
        }

        private fun apply(node: Int, left: Int, right: Int, delta: Long) {
            // 整段每个数加 delta，总和就增加「长度 × delta」。
            sum[node] += (right - left + 1).toLong() * delta
            lazy[node] += delta
        }

        private fun pushDown(node: Int, left: Int, right: Int) {
            val delta = lazy[node]
            if (delta == 0L || left == right) return
            val mid = left + (right - left) / 2
            apply(node * 2, left, mid, delta)
            apply(node * 2 + 1, mid + 1, right, delta)
            lazy[node] = 0L
        }

        private fun query(node: Int, left: Int, right: Int, from: Int, to: Int): Long {
            // 查询范围完全覆盖当前段，直接返回总和，不用访问每个元素。
            if (from <= left && right <= to) return sum[node]

            // 只查询其中一部分时，先让孩子收到之前欠着的更新。
            pushDown(node, left, right)
            val mid = left + (right - left) / 2
            var result = 0L
            if (from <= mid) result += query(node * 2, left, mid, from, to)
            if (to > mid) result += query(node * 2 + 1, mid + 1, right, from, to)
            return result
        }

        private fun add(node: Int, left: Int, right: Int, from: Int, to: Int, delta: Long) {
            // 更新范围完全覆盖当前段，就整段记账，到这里停止递归。
            if (from <= left && right <= to) {
                apply(node, left, right, delta)
                return
            }

            pushDown(node, left, right)
            val mid = left + (right - left) / 2
            if (from <= mid) add(node * 2, left, mid, from, to, delta)
            if (to > mid) add(node * 2 + 1, mid + 1, right, from, to, delta)
            sum[node] = sum[node * 2] + sum[node * 2 + 1]
        }
    }

    @Deprecated("time limit")
    fun sumCountsBySortedLastPositions(nums: IntArray): Int {
        var ans = 0L
        val n = nums.size
        val lastMeet = mutableMapOf<Int,Int>()
        nums.forEachIndexed { rightIndex, rightNum ->
            lastMeet[rightNum] = rightIndex
            var left = -1 
            val jumpPlace = lastMeet.values.sorted()
            jumpPlace.forEachIndexed { i, v -> 
                val lastNum = jumpPlace.size - i
                val square = lastNum * lastNum.toLong()
                val windowSize = v - left
                left = v
                ans += windowSize*square
                ans %= mod
            }
        }
        return ans.toInt()
    }
}
// @lc code=end

