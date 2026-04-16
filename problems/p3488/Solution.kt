package problems.p3488
/*
 * @lc app=leetcode id=3488 lang=kotlin
 *
 * [3488] Closest Equal Element Queries
 */

// @lc code=start
import java.util.Collections

class Solution {
    fun solveQueries(nums: IntArray, queries: IntArray): IntArray {
        val n = nums.size
        val indicesMap = nums.withIndex()
            .groupBy({ it.value }, { it.index })
            .mapValues { (_, indices) ->
                buildList {
                    add(indices.last() - n) // 左哨兵
                    addAll(indices)
                    add(indices.first() + n) // 右哨兵
                }
            }
        return IntArray(queries.size) { qi ->
            val queryIdx = queries[qi]
            val targetValue = nums[queryIdx]
            val p = indicesMap[targetValue]!!

            // 如果长度为 3，说明原数组中该数字只出现了一次
            if (p.size == 3) {
                -1
            } else {
                // p 已经是有序的，直接进行二分查找
                val j = p.binarySearch(queryIdx)
                
                // Kotlin 的 minOf 可以接收多个参数，这里计算左右邻居的最小值
                minOf(queryIdx - p[j - 1], p[j + 1] - queryIdx)
            }
        }
    }
}
// @lc code=end

