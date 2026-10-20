package p3886

/*
 * @lc app=leetcode id=3886 lang=kotlin
 *
 * [3886] Sum of Sortable Integers
 *
 * https://leetcode.com/problems/sum-of-sortable-integers/description/
 *
 * algorithms
 * Hard (31.62%)
 * Likes:    108
 * Dislikes: 7
 * Total Accepted:    15.9K
 * Total Submissions: 45.2K
 * Testcase Example:  '[3,1,2]'
 *
 * You are given an integer array nums of length n.
 * 
 * An integer k is called sortable if k divides n and you can sort nums in
 * non-decreasing order by sequentially performing the following
 * operations:
 * 
 * 
 * Partition nums into consecutive subarrays of length k.
 * Cyclically rotate each subarray independently any number of times to the
 * left or to the right.
 * 
 * 
 * Return an integer denoting the sum of all possible sortable integers k.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [3,1,2]
 * 
 * Output: 3
 * 
 * Explanation:​​​​​​​
 * 
 * 
 * For n = 3, possible divisors are 1 and 3.
 * For k = 1: each subarray has one element. No rotation can sort the
 * array.
 * For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1,
 * 2, 3], which is sorted.
 * Only k = 3 is sortable. Hence, the answer is 3.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [7,6,5]
 * 
 * Output: 0
 * 
 * Explanation:
 * 
 * 
 * For n = 3, possible divisors are 1 and 3.
 * For k = 1: each subarray has one element. No rotation can sort the
 * array.
 * For k = 3: the single subarray [7, 6, 5] cannot be rotated into
 * non-decreasing order.
 * No k is sortable. Hence, the answer is 0.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [5,8]
 * 
 * Output: 3
 * 
 * Explanation:​​​​​​​
 * 
 * 
 * For n = 2, possible divisors are 1 and 2.
 * Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer
 * is 1 + 2 = 3.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n == nums.length <= 10^5
 * 1 <= nums[i] <= 10^5
 *
 * 
 */

// @lc code=start
class Solution {
    fun List<Int>.passed(): Boolean {
        val nums = this.asSequence() + this.asSequence()
        var uptime = 0
        var last = Int.MIN_VALUE
        nums.forEach {
            uptime = if (it >= last) uptime + 1 else 1
            if (uptime == this.size) return true
            last = it
        }
        return false
    }
    fun sortableIntegers(nums: IntArray): Int {
        val n = nums.size
        val nums = nums.toList()
        val sortedNums = nums.sorted()
        var ans = 0
        (1..n).forEach ws@{ windowSize ->
            if (n%windowSize != 0) return@ws

            val windows = nums.chunked(windowSize).map { window ->
                if (window.passed().not()) return@ws
                window.sorted()
            }

            var index = 0
            windows.forEach { w -> w.forEach { c ->
                if (c != sortedNums[index]) return@ws
                index+=1
            } }
            ans += windowSize
        }
        return ans
    } 
}
// @lc code=end

