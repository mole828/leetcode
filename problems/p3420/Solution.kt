package p3420

/*
 * @lc app=leetcode id=3420 lang=kotlin
 *
 * [3420] Count Non-Decreasing Subarrays After K Operations
 *
 * https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/description/
 *
 * algorithms
 * Hard (24.97%)
 * Likes:    94
 * Dislikes: 5
 * Total Accepted:    8.5K
 * Total Submissions: 23.7K
 * Testcase Example:  '[6,3,1,2,4,4]\n7'
 *
 * You are given an array nums of n integers and an integer k.
 * 
 * For each subarray of nums, you can apply up to k operations on it. In each
 * operation, you increment any element of the subarray by 1.
 * 
 * Note that each subarray is considered independently, meaning changes made to
 * one subarray do not persist to another.
 * 
 * Return the number of subarrays that you can make non-decreasing ​​​​​after
 * performing at most k operations.
 * 
 * An array is said to be non-decreasing if each element is greater than or
 * equal to its previous element, if it exists.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [6,3,1,2,4,4], k = 7
 * 
 * Output: 17
 * 
 * Explanation:
 * 
 * Out of all 21 possible subarrays of nums, only the subarrays [6, 3, 1], [6,
 * 3, 1, 2], [6, 3, 1, 2, 4] and [6, 3, 1, 2, 4, 4] cannot be made
 * non-decreasing after applying up to k = 7 operations. Thus, the number of
 * non-decreasing subarrays is 21 - 4 = 17.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [6,3,1,3,6], k = 4
 * 
 * Output: 12
 * 
 * Explanation:
 * 
 * The subarray [3, 1, 3, 6] along with all subarrays of nums with three or
 * fewer elements, except [6, 3, 1], can be made non-decreasing after k
 * operations. There are 5 subarrays of a single element, 4 subarrays of two
 * elements, and 2 subarrays of three elements except [6, 3, 1], so there are 1
 * + 5 + 4 + 2 = 12 subarrays that can be made non-decreasing.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 * 1 <= k <= 10^9
 * 
 * 
 */

// @lc code=start
class Solution {
    @Deprecated("保留作暴力对照验证；时间复杂度 O(n³)，大输入会超时，请使用 countNonDecreasingSubarrays")
    fun countNonDecreasingSubarrays0(nums: IntArray, k: Int): Long {
        fun toNonDecreasingNeed(list: List<Int>): Long {
            var last = 0
            var need = 0L
            list.forEach { 
                if (it < last) need += last - it
                else last = it
            }
            return need
        }
        val nums = nums.toList()
        var count = 0L
        for (left in nums.indices) {
            for (right in left..<nums.size) {
                val sub = nums.subList(left, right+1)
                if (toNonDecreasingNeed(sub) <= k) count += 1
            }
        }
        return count
    }

    @Deprecated("保留作 Map 合并思路参考；最坏时间复杂度 O(n³)，请使用 countNonDecreasingSubarrays")
    fun countNonDecreasingSubarraysMapReference(nums: IntArray, k: Int): Long {
        var count = 0L
        nums.withIndex().reversed().forEach { right ->
            var needK = 0L
            val numMap = mutableMapOf<Int, Int>()
            for (leftIndex in right.index downTo 0) {
                val leftNum = nums[leftIndex]
                val keys = numMap.keys.filter { it < leftNum }
                var leftCount = numMap.getOrDefault(leftNum, 0) + 1 
                keys.forEach { key -> 
                    val d = leftNum - key
                    val countOfNum = numMap[key]!!
                    needK += d * countOfNum.toLong()
                    numMap.remove(key)
                    leftCount += countOfNum
                }
                numMap[leftNum] = leftCount

                if (needK <= k) count += 1
                else break
            }
        }
        return count
    }

    fun countNonDecreasingSubarrays(nums: IntArray, k: Int): Long {
        data class Group(val value: Int, var count: Int)

        // 按窗口中的顺序保存调整后的各组，组的值严格递增。
        val groups = ArrayDeque<Group>()
        var right = nums.lastIndex
        var needK = 0L
        var count = 0L

        for (left in nums.lastIndex downTo 0) {
            val leftNum = nums[left]
            var mergedCount = 1

            // 向左加入元素，把前面较小的组统一抬高到 leftNum。
            while (groups.isNotEmpty() && groups.first().value <= leftNum) {
                val group = groups.removeFirst()
                needK += (leftNum.toLong() - group.value) * group.count
                mergedCount += group.count
            }
            groups.addFirst(Group(leftNum, mergedCount))

            // 删除右端元素，只需扣除这个元素原本的抬高成本。
            while (needK > k) {
                val group = groups.last()
                needK -= group.value - nums[right]
                group.count--
                if (group.count == 0) groups.removeLast()
                right--
            }

            // [left, left] 到 [left, right] 都是合法子数组。
            count += right - left + 1
        }
        return count
    }
}
// @lc code=end

