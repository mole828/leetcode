package p3505

import kotlin.math.abs
import java.util.TreeMap

/*
 * @lc app=leetcode id=3505 lang=kotlin
 *
 * [3505] Minimum Operations to Make Elements Within K Subarrays Equal
 *
 * https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/description/
 *
 * algorithms
 * Hard (28.79%)
 * Likes:    80
 * Dislikes: 4
 * Total Accepted:    7.3K
 * Total Submissions: 20.3K
 * Testcase Example:  '[5,-2,1,3,7,3,6,4,-1]\n3\n2'
 *
 * You are given an integer array nums and two integers, x and k. You can
 * perform the following operation any number of times (including zero):
 * 
 * 
 * Increase or decrease any element of nums by 1.
 * 
 * 
 * Return the minimum number of operations needed to have at least k
 * non-overlapping subarrays of size exactly x in nums, where all elements
 * within each subarray are equal.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2
 * 
 * Output: 8
 * 
 * Explanation:
 * 
 * 
 * Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from
 * nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
 * Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from
 * nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
 * Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and
 * [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were
 * used, 8 is the output.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2
 * 
 * Output: 3
 * 
 * Explanation:
 * 
 * 
 * Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2,
 * -2, -2, -2, 5].
 * Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and
 * [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is
 * the output.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= nums.length <= 10^5
 * -10^6 <= nums[i] <= 10^6
 * 2 <= x <= nums.length
 * 1 <= k <= 15
 * 2 <= k * x <= nums.length
 * 
 * 
 */

// @lc code=start
// 切换父类即可切换提交版本；各版本均提供 minOperations。
// Solution1：滑动中位数 + 循环 DP（正式版本）
// Solution2：逐窗口排序 + 记忆化 DFS（第二版暴力）
// Solution3：有序 MutableList + 记忆化 DFS（bisect 扩展版）
// Solution4：枚举目标值的逐元素 DFS（最初版本）
class Solution : Solution1()

open class Solution1 {
    // 正式版本：滑动中位数计算窗口代价，再用循环 DP 选择不重叠的窗口。
    fun minOperations(nums: IntArray, x: Int, k: Int): Long {
        val costs = LongArray(nums.size - x + 1)
        val window = MedianWindow()
        for (i in nums.indices) {
            window.add(nums[i])
            if (i >= x) window.remove(nums[i - x])
            if (i >= x - 1) costs[i - x + 1] = window.cost()
        }

        val inf = Long.MAX_VALUE / 2
        // previous[i]：在前 i 个元素中选出 count - 1 段的最小代价。
        var previous = LongArray(nums.size + 1)
        for (count in 1..k) {
            val current = LongArray(nums.size + 1) { inf }
            for (i in 1..nums.size) {
                current[i] = current[i - 1]
                if (i >= x) {
                    current[i] = minOf(current[i], previous[i - x] + costs[i - x])
                }
            }
            previous = current
        }
        return previous[nums.size]
    }

    private class MedianWindow {
        private val lower = SortedMultiset()
        private val upper = SortedMultiset()

        fun add(value: Int) {
            if (lower.size == 0 || value <= lower.last()) lower.add(value)
            else upper.add(value)
            rebalance()
        }

        fun remove(value: Int) {
            if (value <= lower.last()) lower.remove(value)
            else upper.remove(value)
            rebalance()
        }

        private fun rebalance() {
            // lower 保存较小的一半，数量与 upper 相同或多一个。
            while (lower.size > upper.size + 1) {
                val value = lower.last()
                lower.remove(value)
                upper.add(value)
            }
            while (lower.size < upper.size) {
                val value = upper.first()
                upper.remove(value)
                lower.add(value)
            }
        }

        fun cost(): Long {
            val median = lower.last().toLong()
            return median * lower.size - lower.sum + upper.sum - median * upper.size
        }
    }

    private class SortedMultiset {
        private val counts = TreeMap<Int, Int>()
        var size = 0
            private set
        var sum = 0L
            private set

        fun first(): Int = counts.firstKey()
        fun last(): Int = counts.lastKey()

        fun add(value: Int) {
            counts[value] = (counts[value] ?: 0) + 1
            size++
            sum += value
        }

        fun remove(value: Int) {
            val count = counts.getValue(value)
            if (count == 1) counts.remove(value)
            else counts[value] = count - 1
            size--
            sum -= value
        }
    }
}

// 第二版暴力：独立保留完整流程，便于与 Solution1 对照阅读。
@Deprecated("仅供阅读和小规模对照；预处理为 O(nx log x)，深递归可能栈溢出。正式调用请使用 Solution1。")
open class Solution2 {
    fun minOperations(nums: IntArray, x: Int, k: Int): Long {
        val costs = LongArray(nums.size - x + 1) { start ->
            val sorted = nums.copyOfRange(start, start + x)
            sorted.sort()
            val median = sorted[x / 2].toLong()
            sorted.sumOf { abs(it.toLong() - median) }
        }

        val inf = Long.MAX_VALUE / 2
        val memo = Array(k + 1) { LongArray(nums.size) { -1L } }
        // 从 i 开始，还需要选择 remaining 段的最小代价。
        fun dfs(i: Int, remaining: Int): Long =
            when {
                remaining == 0 -> 0L
                nums.size - i < remaining * x -> inf
                memo[remaining][i] != -1L -> memo[remaining][i]
                else -> {
                    val skip = dfs(i + 1, remaining)
                    val pick = costs[i] + dfs(i + x, remaining - 1)
                    minOf(skip, pick).also { memo[remaining][i] = it }
                }
            }
        return dfs(0, k)
    }
}

// bisect 扩展版：列表始终有序，滑动时删除旧元素、插入新元素。
@Deprecated("仅供阅读和小规模对照；预处理为 O(nx)，深递归可能栈溢出。正式调用请使用 Solution1。")
open class Solution3 {
    fun minOperations(nums: IntArray, x: Int, k: Int): Long {
        val window = nums.take(x).sorted().toMutableList()
        val costs = LongArray(nums.size - x + 1) { start ->
            if (start > 0) {
                window.bisectRemove(nums[start - 1])
                window.bisectAdd(nums[start + x - 1])
            }
            val median = window[x / 2].toLong()
            window.sumOf { abs(it.toLong() - median) }
        }

        val inf = Long.MAX_VALUE / 2
        val memo = Array(k + 1) { LongArray(nums.size) { -1L } }
        // 从 i 开始，还需要选择 remaining 段的最小代价。
        fun dfs(i: Int, remaining: Int): Long =
            when {
                remaining == 0 -> 0L
                nums.size - i < remaining * x -> inf
                memo[remaining][i] != -1L -> memo[remaining][i]
                else -> {
                    val skip = dfs(i + 1, remaining)
                    val pick = costs[i] + dfs(i + x, remaining - 1)
                    minOf(skip, pick).also { memo[remaining][i] = it }
                }
            }
        return dfs(0, k)
    }

    private fun MutableList<Int>.bisectAdd(value: Int) {
        val index = binarySearch(value)
        add(if (index >= 0) index else -index - 1, value)
    }

    private fun MutableList<Int>.bisectRemove(value: Int) {
        val index = binarySearch(value)
        require(index >= 0) { "Cannot remove missing value: $value" }
        removeAt(index)
    }
}

// 最初版本：枚举每段的目标值，逐个元素完成当前段。
@Deprecated("仅供理解原始递归；枚举目标值且搜索规模呈指数增长，深递归可能栈溢出。正式调用请使用 Solution1。")
open class Solution4 {
    fun minOperations(nums: IntArray, x: Int, k: Int): Long {
        val minNum = nums.min()
        val maxNum = nums.max()
        val inf = Long.MAX_VALUE / 2
        fun dfs(i: Int, lastK: Int, lastX: Int, pickValue: Int): Long =
            when {
                lastK == 0 && lastX == 0 -> 0L
                i == nums.size -> inf
                lastX > 0 -> {
                    // 当前子数组尚未选完，必须继续选择。
                    val cost = abs(nums[i] - pickValue).toLong()
                    cost + dfs(i + 1, lastK, lastX - 1, pickValue)
                }
                else -> {
                    val skip = dfs(i + 1, lastK, 0, 0)
                    val start = (minNum..maxNum).minOf { pick ->
                        val cost = abs(nums[i] - pick).toLong()
                        cost + dfs(i + 1, lastK - 1, x - 1, pick)
                    }
                    minOf(skip, start)
                }
            }
        return dfs(0, k, 0, 0)
    }
}
// @lc code=end
