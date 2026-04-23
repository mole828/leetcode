package problems.p2615
/*
 * @lc app=leetcode id=2615 lang=kotlin
 *
 * [2615] Sum of Distances
 */

// @lc code=start
class Solution {
    @Deprecated("Time Limit Exceeded")
    fun distance0(nums: IntArray): LongArray {
        val indexedNums = nums.mapIndexed { i, num -> Pair(i, num) }
        val groupedByValue = indexedNums.groupBy { it.second }
        val result = LongArray(nums.size).apply { 
            groupedByValue.forEach { (_, group) -> 
                group.forEach { (index, _) ->
                    val sumDistances = group.sumOf { (otherIndex, _) -> kotlin.math.abs(index - otherIndex).toLong() }
                    this[index] = sumDistances
                }
            }
        }
        return result
    }
    @Deprecated("Time Limit Exceeded")
    fun distance1(nums: IntArray): LongArray {
        val groups = mutableMapOf<Int, MutableList<Int>>().withDefault { mutableListOf<Int>() }
        val result = LongArray(nums.size)
        nums.forEachIndexed { index, num ->
            val group = groups.getValue(num)
            var sumDistances = 0L
            group.forEach { 
                val d = kotlin.math.abs(index - it).toLong()
                result[it] += d
                sumDistances += d
            }
            result[index] = sumDistances
            group.add(index)
            groups[num] = group
            // println(groups)
        }
        return result
    }
    fun distance(nums: IntArray): LongArray {
        val n = nums.size
        val result = LongArray(n)
        nums.withIndex().groupBy { it.value }.forEach { (_, indexedValues) ->
            val k = indexedValues.size
            val totalSum = indexedValues.fold(0L) { acc, (i, _) -> acc + i }
            var prefixSum = 0L

            indexedValues.forEachIndexed { j, (currentIndex, _) ->
                val cur = currentIndex.toLong()
                val sumDist = (2 * j - k + 1) * cur + totalSum - 2 * prefixSum - cur
                result[currentIndex] = sumDist
                prefixSum += cur
            }
        }
        return result
    }
}
// @lc code=end

